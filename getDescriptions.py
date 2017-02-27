import urllib2
import json

nums = [131, 324, 109, 166, 51, 79, 357, 50, 489, 347, 167, 446, 18, 376, 68, 67, 103, 19, 510, 476, 488, 151, 497, 59]

finalData = ""

for i in nums:

    url = "https://sandbox-healthservice.priaid.ch/issues/" + str(i) + "/info?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5pa2hpbC5hamphcmFwdUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjEwMTMiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTctMDEtMDEiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTQ4ODE2NDIxNCwibmJmIjoxNDg4MTU3MDE0fQ.VU8cM-jQdJSjCqALv6TdnXdthc4CQDoXePCVUDf7sBw&language=en-gb&"

    req = urllib2.Request(url)
    data = urllib2.urlopen(req).read()
    respjson = json.loads(data.decode("utf-8"))

    finalData += "\"" + str(i) + "\":" + json.dumps(respjson) + ","

print(finalData)
