import requests, sys

rootURL = "https://kickass.to/json.php"
strSearchString = ""

for i in range(1, len(sys.argv)):
    strSearchString += sys.argv[i] + " "

print "Search String: " + strSearchString

params = dict(
            q = strSearchString,
            field = "seeder",
            sorter = "desc",
            page = "1"
        )

jsonReply = requests.get(url = rootURL, params=params)
jsonReply = jsonReply.json()

print jsonReply
