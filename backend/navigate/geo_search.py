from geopy.geocoders import Nominatim
from geopy.exc import (
    GeocoderTimedOut,
    GeocoderServiceError
)


geolocator = Nominatim(
    user_agent="blind_navigator_app"
)


def search_location(place):

    try:

        location = geolocator.geocode(
            place,
            timeout=10
        )

        if location:

            return {
                "address": location.address,
                "latitude": location.latitude,
                "longitude": location.longitude
            }

        else:

            print("Address not found")

            return None


    except (
        GeocoderTimedOut,
        GeocoderServiceError
    ) as error:

        print(f"Geocoding error: {error}")

        return None