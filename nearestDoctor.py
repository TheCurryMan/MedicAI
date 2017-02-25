from bs4 import BeautifulSoup
import requests
import urllib2

place = self.request.get("place")
        url = "https://www.ahd.com/states/hospital_CA.html"
        req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'})
        con = urllib2.urlopen( req )

        counter=0
        alldata = []
        soup = BeautifulSoup(con.read(), "html.parser")
        for obj in soup.find_all("tr"):
            beds = 0
            hospName = ""
            for item in obj.find_all("td"):
                counter += 1
                if counter % 6 == 2:
                    if place != item.value:
                        counter += 4
                        break
                if counter % 6 == 1:
                    hospName = item.value
                if counter % 6 == 3:
                    beds = int(item.value)
                    alldata.append({hospName:beds})

        self.response.write(json.dumps({place:alldata}))
