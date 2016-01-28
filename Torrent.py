class Torrent:
    def __init__(self, params):
        self.title = params["title"]
        self.category = params["category"]
        self.link = params["link"]
        self.pubDate = params["pubDate"]
        self.torrentLink = params["torrentLink"]
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
