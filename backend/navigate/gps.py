import requests


def get_current_location():

    try:

        response = requests.get(
            "https://ipinfo.io/json",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Location format: "latitude,longitude"
        loc = data["loc"].split(",")

        latitude = float(loc[0])
        longitude = float(loc[1])

        city = data.get(
            "city",
            "Unknown"
        )

        state = data.get(
            "region",
            "Unknown"
        )

        print("\nLOCATION FETCHED")

        print(
            "Latitude:",
            latitude
        )

        print(
            "Longitude:",
            longitude
        )

        print(
            "City:",
            city
        )

        print(
            "State:",
            state
        )

        return latitude, longitude


    except requests.RequestException as error:

        print(
            "Internet or location error:",
            error
        )

        return None, None


    except (
        KeyError,
        ValueError
    ) as error:

        print(
            "Location data error:",
            error
        )

        return None, None