class Event(object):
    def __init__(self, ident, name, date, time):
        self.id = ident #This will be useful for events of the same name. Use this to delete or edit events.
        self.name = name
        self.date = date
        self.time = time
        self.desc = "" #Gets assigned later
    
    def setDesc(self, message):
        self.desc = message
    
    def getID(self):
        return self.id

    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time

    def getDesc(self):
        return self.desc