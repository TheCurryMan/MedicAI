import urllib2
import json
from firebase import firebase
from locationBasedAnalysis import getLocations

"""
Calls HealthService API to find the disease analysis based on symptom ids passed in
Also gets the mapped disease description from the API data
"""


class UrlBuilder:
    def __init__(self, base):
        if base[-1] != '?':
            raise ValueError("Base must end with question mark.")
        if "http://" not in base and "https://" not in base:
            raise ValueError("http:// not in base")
        self.base = base
        self.params = []
        self.paramstr = ""

    def addParam(self, opt, val):
        self.params.append([opt, val])

    def getURL(self):
        self.paramstr = ""
        for paramset in self.params:
            self.paramstr += str("=".join([str(p) for p in paramset]))
            self.paramstr += "&"
        return self.base + self.paramstr

    def getBaseURL(self):
        return self.base

    def setParam(self, opt, newVal):
        self.params[self.params.index(opt)][1] = newVal

    def getParams(self):
        return self.params


def getPotentialDiseasesFromIds(ids, number):
    print(ids)

    # Initialize firebase and get User data
    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    data = fb.get("/Users", None)

    # Set up URL for API calling
    URL = "https://sandbox-healthservice.priaid.ch/diagnosis?"
    gender = data[number]["gender"]
    year_of_birth = str(2017 - int(data[number]["age"]))
    # Need to generate new token every 24 hours. Gonna be a pain.
    token = data["token"]
    language = "en-gb"
    symptoms = ids

    base = UrlBuilder(URL)
    base.addParam("symptoms", "[" + ','.join(symptoms) + "]")
    base.addParam("gender", gender)
    base.addParam("year_of_birth", year_of_birth)
    base.addParam("token", token)
    base.addParam("language", language)

    # Get data from URL
    req = urllib2.Request(base.getURL())
    data = urllib2.urlopen(req).read()
    respjson = json.loads(data.decode("utf-8"))

    finalData = ""
    counter = 0

    # Parse through JSON and get Disease Data + Description
    for i in range(0, len(respjson)):
        if counter == 1:
            break
        finalData += "Name of disease: " + str(respjson[i]['Issue']['ProfName']) + "\n\n"
        finalData += "Likelihood: " + str(round(int(respjson[i]['Issue']['Accuracy']), 3)) + "%\n\n"
        if getLocations(str(respjson[i]['Issue']['ProfName']), number) > 4:
            finalData += "Warning! We've detected a high number of " + str(respjson[i]['Issue']['ProfName'])
            " cases in your locality (" + str(getLocations(str(respjson[i]['Issue']['ProfName']),
                                                           number)) + ") making the likelihood of this disease much higher." + "\n\n"
        with open('details.json') as data_file:
            data = json.load(data_file)
            finalData += data[str(respjson[i]["Issue"]["ID"])]["TreatmentDescription"] + "\n"
        counter += 1

    return finalData