import urllib.request
import json
import time

url = 'https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

id_list=[]
#sleep for 30 seconds
while True:
    f=open("ballhistory.txt","a")
    g=open("lightninghistory.txt","a")
    time.sleep(30)
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    json_data = json.loads(response.read())

    # if the id doesnt exist
    if json_data['id'] not in id_list:
        id_list.append(json_data['id'])
        f.write(str(json_data["data"]["result"]["outcome"]["number"]))
        g.write(str([json_data['data']['startedAt'],json_data['data']['result']['luckyNumbersList']]))
        f.write("\n"),g.write("\n")
        print("more data collected",json_data['id'])
        print(len(id_list),"data points")
    f.close()
    g.close()
