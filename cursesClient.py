import requests, os, sys, curses
from Torrent import Torrent
from tabulate import tabulate


stdscr = curses.initscr()

rootURL = "https://kat.cr/json.php"
strSearchString = ""

for i in range(1, len(sys.argv)):
    strSearchString += sys.argv[i] + " "

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
    table.append([str(counter) + ". " + Torrent.getTitle(), Torrent.getSeeders(), Torrent.getSizeInGB()])
    counter+= 1

table = tabulate(table)


def main(stdscr):
    stdscr.addstr(0, 0, "Search String: " + strSearchString)
    stdscr.addstr(1, 0, table)
    stdscr.refresh()
    gotCh = stdscr.getch()
    stdscr.addstr(28, 0, str(gotCh.encode('utf_8')))
    if (gotCh == ord('n')):
    	stdscr.addstr(29, 0, "Next!".encode('utf_8'))
    stdscr.getch()

curses.wrapper(main)
