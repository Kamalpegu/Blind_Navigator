import sys
import os
import time

# Add speech module directory to import path
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "speech"
    )
)

from geo_search import search_location
from route import get_route, get_checkpoints
from checkpoint_tracker import CheckpointTracker
from gps import get_current_location
from st import text_to_speech
from ts import voice_to_text


# ==========================================
# SPEAK HELPER — PRINTS AND SPEAKS ALOUD
# ==========================================

def speak(message):
    """Print a message and speak it aloud."""

    print(message)
    text_to_speech(message)


# ==========================================
# GET USER'S CURRENT LOCATION
# ==========================================

def fetch_user_location():
    """Fetch the user's current GPS location."""

    speak("Getting your current location.")

    latitude, longitude = get_current_location()

    if latitude is None:

        speak(
            "Sorry, I could not find your location. "
            "Please check your internet connection."
        )
        return None, None

    speak(
        f"Your current location is "
        f"{latitude}, {longitude}."
    )

    return latitude, longitude


# ==========================================
# ASK USER FOR DESTINATION VIA VOICE
# ==========================================

def ask_destination():
    """
    Ask the user to speak their destination.
    Retries up to 3 times if voice is not detected.
    """

    max_retries = 3

    for attempt in range(max_retries):

        speak(
            "Where do you want to go? "
            "Please say your destination."
        )

        destination_name = voice_to_text()

        if destination_name:

            speak(
                f"You said: {destination_name}. "
                "Searching for this location."
            )

            return destination_name

        speak(
            "I could not hear you. "
            "Please try again."
        )

    speak(
        "I was unable to hear your destination "
        "after multiple attempts. "
        "Please restart and try again."
    )

    return None


# ==========================================
# SEARCH AND CONFIRM DESTINATION
# ==========================================

def find_destination():
    """
    Ask the user for a destination via voice,
    search for it, and confirm.
    Retries if the location is not found.
    """

    max_search_retries = 3

    for attempt in range(max_search_retries):

        destination_name = ask_destination()

        if not destination_name:
            return None

        destination = search_location(destination_name)

        if destination:

            speak(
                f"Destination found. "
                f"{destination['address']}."
            )

            return destination

        speak(
            f"Sorry, I could not find "
            f"{destination_name}. "
            "Please say a different destination."
        )

    speak(
        "I was unable to find your destination "
        "after multiple attempts. "
        "Please restart and try again."
    )

    return None


# ==========================================
# GET WALKING ROUTE
# ==========================================

def fetch_route(
    start_latitude,
    start_longitude,
    destination
):
    """Fetch walking route from start to destination."""

    speak("Finding walking route to your destination.")

    route = get_route(
        start_latitude,
        start_longitude,
        destination["latitude"],
        destination["longitude"]
    )

    if not route:

        speak(
            "Sorry, I could not find a walking route "
            "to your destination."
        )
        return None

    distance_km = round(route["distance"] / 1000, 2)
    duration_min = round(route["duration"] / 60, 2)

    speak(
        f"Route found. "
        f"Distance is {distance_km} kilometers. "
        f"Estimated walking time is "
        f"{duration_min} minutes."
    )

    return route


# ==========================================
# LIVE NAVIGATION LOOP
# ==========================================

def start_navigation(checkpoints):
    """
    Run the live navigation loop.
    Speaks turn-by-turn directions as the user walks.
    """

    tracker = CheckpointTracker(
        checkpoints,
        threshold=20
    )

    speak(
        f"Navigation started. "
        f"There are {len(checkpoints)} checkpoints. "
        "Follow my instructions."
    )

    # Announce the first checkpoint
    first_checkpoint = checkpoints[0]

    speak(
        f"Head towards checkpoint 1. "
        f"{first_checkpoint['instruction_type']} "
        f"{first_checkpoint['direction']}."
    )

    # Track time for throttling distance announcements
    last_distance_announcement = 0

    # Time interval between distance updates (seconds)
    distance_announce_interval = 10

    try:

        while True:

            # Get current GPS location
            current_latitude, current_longitude = (
                get_current_location()
            )

            if current_latitude is None:

                speak(
                    "Unable to get your location. "
                    "Trying again."
                )
                time.sleep(3)
                continue

            # Check position against checkpoints
            result = tracker.check_location(
                current_latitude,
                current_longitude
            )

            current_time = time.time()


            # ======================================
            # USER IS MOVING TOWARDS CHECKPOINT
            # ======================================

            if result["status"] == "moving":

                # Throttle distance announcements
                time_since_last = (
                    current_time - last_distance_announcement
                )

                if time_since_last >= distance_announce_interval:

                    checkpoint = result[
                        "current_checkpoint"
                    ]

                    distance = result["distance"]

                    speak(
                        f"Moving towards checkpoint "
                        f"{checkpoint['checkpoint_number']}. "
                        f"{distance:.0f} meters remaining. "
                        f"Next action: "
                        f"{checkpoint['instruction_type']} "
                        f"{checkpoint['direction']}."
                    )

                    last_distance_announcement = (
                        current_time
                    )


            # ======================================
            # CHECKPOINT PASSED
            # ======================================

            elif result["status"] == "checkpoint_passed":

                passed = result["passed_checkpoint"]
                next_cp = result["next_checkpoint"]

                speak(
                    f"Checkpoint "
                    f"{passed['checkpoint_number']} "
                    f"passed!"
                )

                speak(
                    f"Now "
                    f"{next_cp['instruction_type']} "
                    f"{next_cp['direction']}. "
                    f"Head towards checkpoint "
                    f"{next_cp['checkpoint_number']}."
                )

                # Reset throttle so next distance
                # update comes soon
                last_distance_announcement = 0


            # ======================================
            # DESTINATION REACHED
            # ======================================

            elif result["status"] == "destination_reached":

                speak(
                    "Congratulations! "
                    "You have reached your destination. "
                    "Navigation complete."
                )

                total_passed = len(
                    result["passed_checkpoints"]
                )

                speak(
                    f"Total checkpoints passed: "
                    f"{total_passed}."
                )

                break


            # Wait before next GPS check
            time.sleep(2)


    except KeyboardInterrupt:

        speak("Navigation stopped. Goodbye.")


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    speak("Welcome to Blind Navigator.")

    # Step 1: Get current location
    start_latitude, start_longitude = (
        fetch_user_location()
    )

    if start_latitude is None:
        exit()


    # Step 2: Ask for destination via voice
    destination = find_destination()

    if not destination:
        exit()


    # Step 3: Get walking route
    route = fetch_route(
        start_latitude,
        start_longitude,
        destination
    )

    if not route:
        exit()


    # Step 4: Extract checkpoints
    checkpoints = get_checkpoints(route)

    if not checkpoints:

        speak(
            "No navigation steps found "
            "for this route."
        )
        exit()

    speak(
        f"Route has {len(checkpoints)} "
        f"navigation checkpoints."
    )


    # Step 5: Start live navigation
    start_navigation(checkpoints)