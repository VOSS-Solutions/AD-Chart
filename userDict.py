class userDict:

    def __init__(self, fname, lname, email, title=None, mobile=None, tel=None, skype=None, location=None, manager=None,
                 ip=None, CEO=None, image=''):
        self.parent = None
        self.name = str(fname + " " + lname)
        self.manager = manager
        self.image = "http://directory.visionoss.int/photos/%s.jpg" % self.name.lower().replace(' ','.', 1).replace(' ', '')
        self.bio = str("<br />Title: " + title +
              "<br />Email: " + email + "<br />Mobile: " + mobile + "<br />Telephone: " + tel + "<br />Skype: " +
              skype + "<br />Location: " + location + "<br />IP No.: " + ip)
        if CEO == str(fname + " " + lname):
            self._children = []
        else:
            self.children = []

    def getMan(self):
        return self.manager

    def setParent(self, parentNode):
        self.parent = parentNode

    def addChild(self, childNode):
        try:
            self.children.append(childNode)
        except:
            self._children.append(childNode)

    def getPar(self):
        return self.parent

    def getChilds(self):
        try:
            return self.children
        except:
            return self._children