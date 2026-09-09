from geopy.distance import geodesic


class CheckpointTracker:

    def __init__(self, checkpoints, threshold=15):

        # All checkpoints received from route.py
        self.checkpoints = checkpoints

        # Index of the checkpoint currently being tracked
        self.current_checkpoint_index = 0

        # Distance in meters required to consider
        # a checkpoint as reached
        self.threshold = threshold

        # Store all passed checkpoints
        self.passed_checkpoints = []


    # ==========================================
    # GET CURRENT CHECKPOINT
    # ==========================================

    def get_current_checkpoint(self):

        if self.current_checkpoint_index >= len(
            self.checkpoints
        ):
            return None

        return self.checkpoints[
            self.current_checkpoint_index
        ]


    # ==========================================
    # CHECK USER LOCATION
    # ==========================================

    def check_location(
        self,
        current_latitude,
        current_longitude
    ):

        # Check whether all checkpoints are completed
        if self.current_checkpoint_index >= len(
            self.checkpoints
        ):

            return {
                "status": "destination_reached",

                "message": (
                    "All checkpoints have been completed."
                ),

                "passed_checkpoints": self.passed_checkpoints
            }


        # ==========================================
        # GET CURRENT CHECKPOINT
        # ==========================================

        checkpoint = self.get_current_checkpoint()


        # User's current GPS location
        current_location = (
            current_latitude,
            current_longitude
        )


        # Checkpoint location from OSRM
        checkpoint_location = (
            checkpoint["latitude"],
            checkpoint["longitude"]
        )


        # ==========================================
        # CALCULATE DISTANCE
        # ==========================================

        distance = geodesic(
            current_location,
            checkpoint_location
        ).meters


        print(
            f"\nTracking Checkpoint "
            f"{checkpoint['checkpoint_number']}"
        )

        print(
            f"Distance to checkpoint: "
            f"{distance:.2f} meters"
        )


        # ==========================================
        # CHECKPOINT REACHED
        # ==========================================

        if distance <= self.threshold:

            # Save the passed checkpoint
            passed_checkpoint = checkpoint

            self.passed_checkpoints.append(
                passed_checkpoint
            )


            # Move to the next checkpoint
            self.current_checkpoint_index += 1


            # Check if destination / all checkpoints completed
            if self.current_checkpoint_index >= len(
                self.checkpoints
            ):

                return {
                    "status": "destination_reached",

                    "checkpoint": passed_checkpoint,

                    "distance": distance,

                    "message": (
                        "Final checkpoint passed. "
                        "You have reached your destination."
                    ),

                    "passed_checkpoints": (
                        self.passed_checkpoints
                    )
                }


            # Get next checkpoint
            next_checkpoint = self.get_current_checkpoint()


            return {
                "status": "checkpoint_passed",

                "passed_checkpoint": passed_checkpoint,

                "next_checkpoint": next_checkpoint,

                "distance": distance,

                "message": (
                    f"Checkpoint "
                    f"{passed_checkpoint['checkpoint_number']} "
                    f"passed successfully."
                )
            }


        # ==========================================
        # USER IS STILL MOVING
        # ==========================================

        return {
            "status": "moving",

            "current_checkpoint": checkpoint,

            "distance": distance,

            "message": (
                f"Moving towards checkpoint "
                f"{checkpoint['checkpoint_number']}."
            )
        }


    # ==========================================
    # GET ALL PASSED CHECKPOINTS
    # ==========================================

    def get_passed_checkpoints(self):

        return self.passed_checkpoints