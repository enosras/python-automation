# import certifi
import requests
import certifi


'''
print("Result:")
print(certifi.where())

'''

#testing for ceonnections to external servers/ resources 
#url = 'https://flask-static-ops.onrender.com/'
#url = 'https://nominatim.openstreetmap.org/search?country=DE&city=Erlangen&postalcode=91052&street=N%C3%BCrnberger+Stra%C3%9Fe+7&format=json&limit=1'
#url = 'https://api.openweathermap.org/data/2.5/weather?q=Nairobi&mode=json&units=imperial&appid=a7b2d28d6dbb12a57ad590e39b6abd58'
#url ='https://nominatim.openstreetmap.org/search?country=USA&city=Kent&postalcode=98032&street=Central+Avenue7&format=json&limit=1'
url = 'https://nominatim.openstreetmap.org/details?osmtype=N&osmid=2567548286&class=place&addressdetails=1&entrances=1&hierarchy=0&group_hierarchy=1&format=json&limit=1'

#url = 'https://www.google.com'
response = requests.get(url)
print(response.status_code)\

r = requests.get(url)

'https://nominatim.openstreetmap.org/details?osmtype=N&osmid=2567548286&class=place&addressdetails=1&entrances=1&hierarchy=0&group_hierarchy=1&format=json&limit=1'
'''
'https://nominatim.openstreetmap.org/search?country=USA&city=Kent&postalcode=98032&street=Central+Avenue7&format=json&limit=1'

'''
