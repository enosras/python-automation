import json

import geopy.geocoders
import phonenumbers

# from geopy import Point
from geopy.location import Location


# capture region based on manual cooridnates
def capture_region():
    print("success")
    locater = geopy.geocoders.Nominatim(user_agent="dev")
    lati = 47.61
    longi = -122.33
    # coord_pair = Point(lati, longi)
    region_locater: Location = locater.reverse((lati, longi), timeout=10)  # type: ignore
    # taking the raw data to detect the country
    all_geo_data = region_locater.raw["address"]["country"]
    # return region_locater
    return all_geo_data


def phone_conv():
    print("Hi there")
    raw_number = input("Enter phone number : ")
    # number = str(raw_number)
    # print("Hi there")
    region = "US"
    new_number = phonenumbers.parse(raw_number, region)
    print(new_number)
    final_number = phonenumbers.format_number(
        new_number, phonenumbers.PhoneNumberFormat.E164
    )
    print(final_number)


def json_type():
    raw_data = '{"name": "enos", "age": 21, "status": "multimillionaire", "affluent": true, "contacts": ["eut.gmail.com", 2101230000]}'
    # where we start to test the design
    print(raw_data)
    new_data = json.loads(raw_data)
    choice = input("Enter object you wish to investigate : ")
    print(new_data[choice])


if __name__ == "__main__":
    # phone_conv()
    region_data = capture_region()
    print(region_data)
