import sys
import os

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

# ==========================================
# ADD BACKEND MODULES TO IMPORT PATH
# ==========================================

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "backend",
        "navigate"
    )
)

from geo_search import search_location
from route import get_route, get_checkpoints
from checkpoint_tracker import CheckpointTracker
from gps import get_current_location


# ==========================================
# INITIALIZE FLASK APP
# ==========================================

app = Flask(__name__)


# Server-side navigation state
navigation_state = {
    "tracker": None,
    "checkpoints": [],
    "route_geometry": None
}


# ==========================================
# SERVE MAIN PAGE
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# API: GET CURRENT LOCATION
# ==========================================

@app.route("/api/location", methods=["GET"])
def api_location():
    """
    Get user's current location via IP geolocation.
    Used as a fallback when browser geolocation
    is unavailable.
    """

    latitude, longitude = get_current_location()

    if latitude is None:

        return jsonify({
            "error": "Could not determine location."
        }), 500

    return jsonify({
        "latitude": latitude,
        "longitude": longitude
    })


# ==========================================
# API: SEARCH DESTINATION
# ==========================================

@app.route("/api/search", methods=["POST"])
def api_search():
    """
    Geocode a place name into coordinates.
    Expects JSON: {"place": "Silchar Medical College"}
    """

    data = request.get_json()

    place = data.get("place", "").strip()

    if not place:

        return jsonify({
            "error": "No destination provided."
        }), 400

    result = search_location(place)

    if not result:

        return jsonify({
            "error": (
                f"Could not find '{place}'. "
                "Please try a different name."
            )
        }), 404

    return jsonify(result)


# ==========================================
# API: GET WALKING ROUTE
# ==========================================

@app.route("/api/route", methods=["POST"])
def api_route():
    """
    Get walking route from start to destination.
    Expects JSON: {
        "start_latitude", "start_longitude",
        "dest_latitude", "dest_longitude"
    }
    Returns route info, checkpoints, and geometry.
    """

    data = request.get_json()

    start_lat = data["start_latitude"]
    start_lng = data["start_longitude"]
    dest_lat = data["dest_latitude"]
    dest_lng = data["dest_longitude"]

    route = get_route(
        start_lat, start_lng,
        dest_lat, dest_lng
    )

    if not route:

        return jsonify({
            "error": "Could not find a walking route."
        }), 404

    checkpoints = get_checkpoints(route)

    # Initialize the checkpoint tracker on the server
    navigation_state["tracker"] = CheckpointTracker(
        checkpoints,
        threshold=20
    )

    navigation_state["checkpoints"] = checkpoints
    navigation_state["route_geometry"] = route.get(
        "geometry"
    )

    return jsonify({
        "distance_km": round(
            route["distance"] / 1000, 2
        ),
        "duration_min": round(
            route["duration"] / 60, 2
        ),
        "checkpoints": checkpoints,
        "geometry": route.get("geometry")
    })


# ==========================================
# API: CHECK POSITION AGAINST CHECKPOINT
# ==========================================

@app.route("/api/check", methods=["POST"])
def api_check():
    """
    Check user's current position against
    the active checkpoint.
    Expects JSON: {"latitude", "longitude"}
    Returns navigation status.
    """

    tracker = navigation_state.get("tracker")

    if not tracker:

        return jsonify({
            "error": "No active navigation session."
        }), 400

    data = request.get_json()

    latitude = data["latitude"]
    longitude = data["longitude"]

    result = tracker.check_location(
        latitude, longitude
    )

    return jsonify(result)


# ==========================================
# API: STOP NAVIGATION
# ==========================================

@app.route("/api/stop", methods=["POST"])
def api_stop():
    """Stop the current navigation session."""

    navigation_state["tracker"] = None
    navigation_state["checkpoints"] = []
    navigation_state["route_geometry"] = None

    return jsonify({
        "message": "Navigation stopped."
    })


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    print("\n" + "=" * 50)
    print("BLIND NAVIGATOR WEB APP")
    print("=" * 50)
    print("Open in browser: http://localhost:5000")
    print("=" * 50 + "\n")

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
