from datetime import date

def timediff():
    #Gets difference from date last opened and today
    today = date.today()
    lastSeen = open("lastSeen.txt", "rt")
    lastSeenDate = lastSeen.readline()
    lastSeen.close()
    lastSeen = open("lastSeen.txt", "wt")
    lastSeen.write(today.isoformat())
    dateDiff = today - date.fromisoformat(lastSeenDate)
    lastSeen.close()
    return dateDiff.days
