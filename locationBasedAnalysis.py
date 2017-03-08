from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from firebase import firebase

def getLocations(disease, number):

    #Initialize Nominatim
    geolocator = Nominatim()

    # Initialize Firebase Application and get user data
    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    data = fb.get('/Diseases', None)
    current_user = fb.get('/Users', None)[number]

    total = 0

    for i in data:
        if i == disease:

            #Get the details of user's current location
            curLoc = geolocator.geocode(current_user["location"])
            curLatLong = (curLoc.latitude, curLoc.longitude)
            for location in data[i]:

                #Get the details of each location in firebase of disease provided
                loc = geolocator.geocode(location)
                locLatLong = (loc.latitude, loc.longitude)

                #If distance between both points is less than 10 miles, increment total
                if vincenty(curLatLong, locLatLong).miles <= 10:
                    total += 1

    data[disease][current_user["location"]] = number
    result = fb.put("", "/Diseases", data)

    return total
