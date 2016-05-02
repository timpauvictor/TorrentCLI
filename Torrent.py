import math
class Torrent:
    def __init__(self, params):
        self.title = params["title"]
        self.category = params["category"]
        self.link = params["link"]
        self.pubDate = params["pubDate"]
        self.torrentLink = params["torrentLink"]
        self.size = params["size"]
        self.hash = params["hash"]
        self.seeders = params["seeds"]
        self.leechers = params["leechs"]
    def getTitle(self):
        return self.title
    def getCategory(self):
        return self.category
    def getLink(self):
        return self.link
    def getPubDate(self):
        return self.pubDate
    def getTorrentLink(self):
        return self.torrentLink
    def getSize(self):
        return self.size
    def getSizeInGB(self):
        return str(self.size / math.pow(10,9)) + "GB"
    def getHash(self): 
        return self.hash
    def getSeeders(self):
        return self.seeders
    def getLeechers(self):
        return self.leechers
