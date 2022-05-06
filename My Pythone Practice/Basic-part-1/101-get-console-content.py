
import http.client, requests

# web = http.client.HTTPConnection("https://en.prothomalo.com/")
# web.request("GET", "/")
# data = web.getresponse()
# finalData = data.read()
#
# print(finalData)
# ==============================

data = requests.get("https://en.prothomalo.com/")
print(data)