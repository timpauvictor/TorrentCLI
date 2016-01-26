import requests, sys

rootURL = "https://kickass.to/json.php"
strSearchString = ""

for i in range(1, len(sys.argv)):
    strSearchString += sys.argv[i] + "%20"

print "Search String: " + strSearchString

