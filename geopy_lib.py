import geopy
from geopy.geocoders import Nominatim

#g = geopy
#help(g)

geo = Nominatim(user_agent="geopy_lib.py")

# Geocode an address
address = "101 Ludlow Street, New York City"
location = geo.geocode(address)

if location:
    print(f"Address: {location.address}")
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
else:
    print("Location not found.")
