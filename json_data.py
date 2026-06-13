import json

import phonenumbers


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
    phone_conv()
