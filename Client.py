import requests, os
from Torrent import Torrent
from tabulate import tabulate


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

table = []
counter = 1
for Torrent in searchResults:
    table.append([str(counter) + ". " + Torrent.getTitle(), Torrent.getSizeInGB()])
    counter+= 1

print(tabulate(table))

os.system()
