import urllib2
import json


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


URL = "https://sandbox-healthservice.priaid.ch/diagnosis?"
gender = "male"
year_of_birth = "1999"
# Need to generate new token every 24 hours. Gonna be a pain.
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5pa2hpbC5hamphcmFwdUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjEwMTMiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTctMDEtMDEiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTQ4ODE2NDIxNCwibmJmIjoxNDg4MTU3MDE0fQ.VU8cM-jQdJSjCqALv6TdnXdthc4CQDoXePCVUDf7sBw"
language = "en-gb"
symptoms = ["13", "9"]

base = UrlBuilder(URL)
base.addParam("symptoms", "[" + ','.join(symptoms) + "]")
base.addParam("gender", gender)
base.addParam("year_of_birth", year_of_birth)
base.addParam("token", token)
base.addParam("language", language)

print(
"AVI I GOT LAZY CHECK OUT THE IDs FOR THE SYMPTOMS HERE: https://sandbox-healthservice.priaid.ch/symptoms?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5pa2hpbC5hamphcmFwdUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjEwMTMiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTctMDEtMDEiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTQ4ODA2MzMzNCwibmJmIjoxNDg4MDU2MTM0fQ.aeDMqPId9_ZpmKLRq7zaukd_CQuQZS6LQzoS_Q5xkj0&language=en-gb")
print("***\n\n")
print("Gender: " + gender.title())
print("Age: " + str(2016 - int(year_of_birth)))
print("Symptom ID(s): " + str(",".join(symptoms)))
print(base.getURL())
req = urllib2.Request(base.getURL())
data = urllib2.urlopen(req).read()
respjson = json.loads(data.decode("utf-8"))
for i in range(0, len(respjson)):
    print("Name of disease: " + str(respjson[i]['Issue']['ProfName']))
    print("Likelihood: " + str(round(int(respjson[i]['Issue']['Accuracy']), 3)) + "%\n")
