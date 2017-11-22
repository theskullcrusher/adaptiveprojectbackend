import json
#
for i in range(532):
    if i == 0:
        continue
    file = str(i) + ".json"
    with open(file) as fp:
        data = json.load(fp)
        print data["tags"]

# list = ["a","b","c"]
# with open("tags.txt","w") as fp:
#     for e in list:
#         fp.write(e + "\n")

#
# import requests
#
# with open("tags.txt","a") as fp:
#     for i in range(0,2000):
#         i = i+1
#         print "page", i
#         url = "https://api.stackexchange.com//2.2/tags?page="+str(i)+"&pagesize=100&order=desc&sort=popular&site=stackoverflow&key=uY1y6v5RlMRidvLO1Zi0Ag(("
#         res = requests.get(url)
#         data = json.loads(res.text)
#         print "Quota remaining", data["quota_remaining"]
#         print "has mode", data["has_more"]
#         for doc in data["items"]:
#             val = doc["name"]
#             fp.write(val + "\n")
