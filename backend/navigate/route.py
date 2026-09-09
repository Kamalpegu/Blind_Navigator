import requests


def get_route(
    start_latitude,
    start_longitude,
    destination_latitude,
    destination_longitude
):

    # OSRM expects coordinates in:
    # longitude,latitude format

    url = (
        "https://router.project-osrm.org/route/v1/foot/"
        f"{start_longitude},{start_latitude};"
        f"{destination_longitude},{destination_latitude}"
    )

    parameters = {
        "overview": "full",
        "geometries": "geojson",
        "steps": "true"
    }

    try:

        print("Finding route...")

        response = requests.get(
            url,
            params=parameters,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        if data.get("code") != "Ok":

            print("Route not found.")

            return None

        route = data["routes"][0]

        print("\nRoute Found!")

        print(
            "Distance:",
            round(route["distance"] / 1000, 2),
            "km"
        )

        print(
            "Duration:",
            round(route["duration"] / 60, 2),
            "minutes"
        )

        return route


    except requests.RequestException as error:

        print("Routing error:", error)

        return None


# ==========================================
# EXTRACT CHECKPOINTS / NAVIGATION STEPS
# ==========================================

def get_checkpoints(route):

    checkpoints = []

    if not route:

        return checkpoints

    for leg in route["legs"]:

        for step in leg["steps"]:

            maneuver = step["maneuver"]

            checkpoint = {
                "checkpoint_number": len(checkpoints) + 1,

                "instruction_type": maneuver.get(
                    "type",
                    "continue"
                ),

                "direction": maneuver.get(
                    "modifier",
                    "straight"
                ),

                "distance": step["distance"],

                "duration": step["duration"],

                # OSRM returns:
                # [longitude, latitude]
                "longitude": maneuver["location"][0],
                "latitude": maneuver["location"][1]
            }

            checkpoints.append(checkpoint)

    return checkpoints