import urllib2
import json
from firebase import firebase

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

    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    data = fb.get('/Users/' + number, None)

    URL = "https://sandbox-healthservice.priaid.ch/diagnosis?"
    gender = data["gender"]
    year_of_birth = str(2017 - int(data["age"]))
    # Need to generate new token every 24 hours. Gonna be a pain.
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5pa2hpbC5hamphcmFwdUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjEwMTMiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTctMDEtMDEiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTQ4ODg3MDc3MiwibmJmIjoxNDg4ODYzNTcyfQ.-XaMj1c1nb-jU0v6qrwmRiLS9mPTiloIW5exFj9MTio"
    language = "en-gb"
    symptoms = ids

    base = UrlBuilder(URL)
    base.addParam("symptoms", "[" + ','.join(symptoms) + "]")
    base.addParam("gender", gender)
    base.addParam("year_of_birth", year_of_birth)
    base.addParam("token", token)
    base.addParam("language", language)

    #print("Gender: " + gender.title())
    #print("Age: " + str(2016 - int(year_of_birth)))
    #print("Symptom ID(s): " + str(",".join(symptoms)))
    print(base.getURL())


    req = urllib2.Request(base.getURL())
    data = urllib2.urlopen(req).read()
    respjson = json.loads(data.decode("utf-8"))
    print(respjson)
    finalData = ""
    counter = 0

    for i in range(0, len(respjson)):
        if counter == 2:
            break
        finalData += "Name of disease: " + str(respjson[i]['Issue']['ProfName']) + "\n"
        finalData += "Likelihood: " + str(round(int(respjson[i]['Issue']['Accuracy']), 3)) + "%\n"
        with open('details.json') as data_file:
            data = json.load(data_file)
            finalData += data[str(respjson[i]["Issue"]["ID"])]["TreatmentDescription"] + "\n"
        counter += 1

    return finalData

