import requests, sys
from Torrent import Torrent


rootURL = "https://kickass.to/json.php"
strSearchString = ""

for i in range(1, len(sys.argv)):
    strSearchString += sys.argv[i] + " "

print("Search String: " + strSearchString)

params = dict(
            q = strSearchString,
            field = "seeder",
            sorter = "desc",
            page = "1"
        )

jsonReply = requests.get(url = rootURL, params=params).json()

searchResults = []
for searchResult in jsonReply["list"]:
    searchResults.append(Torrent(searchResult))

for Torrent in searchResults:
    print(Torrent.getTitle() + " " + str(Torrent.getSizeInGB()))
