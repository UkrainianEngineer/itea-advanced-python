class SQLiteConnectionRefusedError(Exception):
    def __init__(self, message):
        self.message = message


class PostgreSQLConnectionRefusedError(Exception):
    def __init__(self, message):
        self.message = message


class MySQLConnectionRefusedError(Exception):
    def __init__(self, message):
        self.message = message


class Connection:
    def __init__(self, db_name):
        self.open = False
        self.closed = False
        self.db_name = db_name

    def __str__(self):
        return "Connection to {} is open:{} close:{}".format(self.db_name, self.open, self.closed)


class BaseFramework:
    allowed_keys = ["key1", "key2", "key3", "key4", "key5", "key6"]
    allowed_commands = ["CREATE", "INSERT", "DELETE", "SELECT"]

    def __init__(self, **kwargs):
        if kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def connect(self, db_name=None, key=None):
        if db_name is not None:
            conn = Connection(db_name)
            conn.open = True
            return conn

    def execute(self, command):
        if command in self.allowed_commands:
            return command
        else:
            raise TypeError("Provide valid command")

    def close(self):
        raise NotImplementedError


class SQLiteApp(BaseFramework):
    conn = None

    def connect(self, db_name=None, key=None):
        if hasattr(self, "db_name") and key in self.allowed_keys:
            self.conn = super(SQLiteApp, self).connect(self.db_name)
            return self.conn
        raise SQLiteConnectionRefusedError(
                    "Please provide valid key or database name to have access")

    def execute(self, command):
        valid_command = super(SQLiteApp, self).execute(command)
        return "SQLiteApp. {} command has been executed".format(valid_command)

    def close(self):
        conn = self.conn
        conn.open = False
        conn.closed = True
        return conn


class MySQLApp(BaseFramework):

    def __init__(self, db, **kwargs):
        self.db = db
        super(MySQLApp, self).__init__(**kwargs)

    #completely overrides base method
    def connect(self, db_name=None, key=None):
        if not self.db.get("data"):
            raise MySQLConnectionRefusedError("The database is empty")
        return "Connected to database {}".format(self.db.get("db_name", "Provide name of the database"))

    def execute(self, command):
        valid_command = super(MySQLApp, self).execute(command)
        return "MySQLApp. {} command has been executed".format(valid_command)

    def close(self):
        return "MySQLApp. Connection to {} closed".format(self.db)


class PostgreSQLApp(BaseFramework):
    # override base allowed keys
    allowed_keys = ["key6", "key7", "key8", "key9", "key10", "key11"]

    def connect(self, db_name=None, key=None):
        if key in self.allowed_keys:
            return super(PostgreSQLApp, self).connect(db_name, key)
        raise PostgreSQLConnectionRefusedError

    def execute(self, command):
        command = super(PostgreSQLApp, self).execute(command)
        return "PostgresSQLApp. {} command has been executed".format(command)

    def close(self):
        return "PostgreSQLApp. Connection closed"


sql = SQLiteApp(db_name="MyDb")
print(sql.connect(key="key1")) # connection to MyDb
# print(sql.connect()) # error, key must be provided
print(sql.execute("SELECT")) # executed
# print(sql.execute("INNER JOIN")) #error, invalid command
print(sql.conn) #True
print(sql.close())#False
print(sql.conn) #False
print(sql.connect(key="key2"))#True
print(sql.conn) #True
print(sql.close())#False
print(sql.conn) #False
print('*' * 60)
db={"db_name":"My Db", "data":["some data"]}
mysql = MySQLApp(db=db, any_attr="any_value")
print(mysql.any_attr)
print(mysql.connect())
db={"data":[]}
print("*" * 60)
# mysql = MySQLApp(db=db) # databse is empty error
print(mysql.connect())
# print(mysql.execute("Inner join"))
print(mysql.execute("SELECT"))
print(mysql.close())
print("*" * 60)
postgres = PostgreSQLApp()
print(postgres.connect(key="key6"))
# print(mysql.execute("Inner join"))
print(postgres.execute("SELECT"))
print(postgres.close())


