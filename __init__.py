import fileinput
import linecache
import json

def init(dbs):
    global DBs
    DBs = dbs
    global Cache
    Cache = {}
    for db in dbs:
        Cache[db] = {}

def Readline(Database: str, Line: int):
    try:
        Cached = Cache[Database][Line]
        return Cached
    except:
        try:
            Read = json.loads(linecache.getline(Database, Line+1))
            Cache[Database][Line] = Read
            return Read
        except:
            return None

def Write(Database: str, Object):
    try:
        Writefile = open(Database, 'a')
        Writefile.write(json.dumps(Object))
        Writefile.close()
    except:
        pass

def Update(Database: str, Line: int, Object):
    Readfile = open(Database, 'r')
    Writefile = open(Database[0:Database.index('.')]+'.bak', 'w')
    i = -1
    while True:
        i += 1
        Read = Readfile.readline()
        if Read == '':
            break
        if i == Line:
            Writefile.write(json.dumps(Object))
        else:
            Writefile.write(Read)

