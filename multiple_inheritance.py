# multiple inheritance is inheriting from different class. 
class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print('Log message from '+ self.title)
class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print ('Connecting to the database on '+ self.server)

def framework(item):
    # performing the connectipn
    if isinstance(item, Connection):
        item.connect()
    #Log the operation
    if isinstance(item, Loggable):
        item.log()

#Use the framework
#Inherit from connection and Loggable
class SqlDatabase(Connection, Loggable):
    def __init__(self):
        self.title = 'sql connection demo'
        self.server = 'some_server' 
    
#creating the instance of our class
# sql_connection = SqlDatabase()

class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just logging the records'
just_log = JustLog()
#Use our framework
framework(just_log)