import requests
import json
from sys import argv 

script,companyUrl, apiKey = argv

url = "https://{0}/api/v1/groups".format(companyUrl)

headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS {0}".format(apiKey),
    'Host': "{0}".format(companyUrl),
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "JSESSIONID=025B5AB7A5309F7AB29D5BC80F7E7FDB",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

for i in range(1, 600):
    response = requests.request("GET", url, headers=headers)
    count = response.headers.get("X-Rate-Limit-Remaining")
    print(count)
    if int(count) > 600:
        print(count)


    response_json = json.loads(response.text)
    for group in response_json:
        url2 = "https://jay.okta.com/api/v1/groups/{0}/users".format(group.get('id'))
        response = requests.request("GET", url, headers=headers)
        response2 = requests.request("GET", url2, headers=headers)
        count2 = response.headers.get("X-Rate-Limit-Remaining")
        if int(count2) > 600:
            print(count)
