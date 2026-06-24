import json
from typing import cast

import geocoder
import geopy.geocoders
import phonenumbers
import rich

# from geopy import Point
from geopy.location import Location

# import rich_lib

# from rich_lib import print
# rich = rich_lib.print

# for tich print
rprint = rich.print


# capture region based on manually captured coordinates
def capture_region():
    print("success")
    locater = geopy.geocoders.Nominatim(user_agent="dev")

    lati = 47.61
    longi = -122.33
    # coord_pair = Point(lati, longi)
    region_locater: Location = locater.reverse((lati, longi), timeout=10)  # type: ignore
    # taking the raw data to detect the country
    all_geo_data = region_locater.raw.get("address", {})
    print(all_geo_data)

    # for finding specific item from the dictionary data structure
    specific_geo_locator = region_locater.raw["address"]["city"]
    print(specific_geo_locator)

    # now for the ISO style
    iso_location = all_geo_data.get("country_code", "KE").upper()
    print(iso_location)

    # = region_locater.raw("country_code", "US")
    # return region_locater
    # return all_geo_data
    return iso_location


# for auto region function
def auto_capture_region():
    geo_auto = geocoder.ip("me")
    print(geo_auto)
    # exact = geo_auto[2]
    exact_location = geo_auto.country
    print(exact_location)
    return exact_location


def phone_conv():
    # print("Hi there")

    raw_number = input("Enter phone number : ")
    # number = str(raw_number)
    # print("Hi there")
    region = "US"
    new_number = phonenumbers.parse(raw_number, region)
    print(new_number)
    final_number = phonenumbers.format_number(
        new_number, phonenumbers.PhoneNumberFormat.E164
    )
    rprint(f"[blue] {final_number} [/blue]")


def phone_conv_auto():
    rich.print("[green] Hi there")
    # print("Hi there")
    raw_number = input("Enter phone number : ")
    # number = str(raw_number)
    # print("Hi there")
    region = auto_capture_region()
    new_number = phonenumbers.parse(raw_number, region)
    print(new_number)
    final_number = phonenumbers.format_number(
        new_number, phonenumbers.PhoneNumberFormat.E164
    )
    rich.print("[blue] {final_number}")


# print(final_number)


def json_type():
    raw_data = '{"name": "enos", "age": 21, "status": "multimillionaire", "affluent": true, "contacts": ["eut.gmail.com", 2101230000]}'
    # where we start to test the design
    print(raw_data)
    new_data = json.loads(raw_data)
    choice = input("Enter object you wish to investigate : ")
    print(new_data[choice])


if __name__ == "__main__":
    # phone_conv()
    phone_conv()
    # region_data = capture_region()
    # print(region_data)
    # capture_region()

    # auto = auto_capture_region()
    # print(auto)
