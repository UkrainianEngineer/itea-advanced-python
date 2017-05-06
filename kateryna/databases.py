class PostgreSQLConnectionRefusedError(Exception):
    def __init__(self, message):
        self.message = message


class Connection(object):
    def __init__(self, db_name):
        self.closed = False
        self.db_name = db_name

    def __str__(self):
        return "Connection to {}".format(self.db_name)


class BaseFramework(object):
    allowed_commands = ["SELECT", "INSERT", "UPDATE", "DELETE"]

    def __init__(self, connection, **kwargs):
        self.connection = connection
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def connect(self):
        self.connection.closed = False
        return self.connection

    def execute(self, command):
        if not command.upper() in self.allowed_commands:
            raise Exception("Provide valid command")
        return command.upper()

    def close(self):
        raise NotImplementedError


class SQLiteApp(BaseFramework):

    def connect(self):
        conn = super(SQLiteApp, self).connect()
        return 'SQLiteApp. {}'.format(conn)

    def execute(self, command):
        command = super(SQLiteApp, self).execute(command)
        return "SQLiteApp. {} command has been executed".format(command)

    def close(self):
        self.connection.closed = True
        return "{} closed".format(self.connection)


class MySQLApp(BaseFramework):

    def connect(self):
        conn = super(MySQLApp, self).connect()
        return 'SQLiteApp. {}'.format(conn)

    def execute(self, command):
        command = super(MySQLApp, self).execute(command)
        return "MySQLApp. {} command has been executed".format(command)

    def close(self):
        self.connection.closed = True
        return "MySQLApp. {} closed".format(self.connection)


class PostgreSQLApp(BaseFramework):
    """"""
    def __init__(self, credentials, **kwargs):
        """
        :param credentials: username and password
        :type credentials: dict
        """
        self.credentials = credentials
        super(PostgreSQLApp, self).__init__(**kwargs)

    def connect(self):
        """ if any of credentials is missing, raise an error"""
        if "username" not in self.credentials or "password" not in self.credentials:
            raise PostgreSQLConnectionRefusedError("Provide username and passoword")
        return super(PostgreSQLApp, self).connect()

    def execute(self, command):
        command = super(PostgreSQLApp, self).execute(command)
        return "PostgresSQLApp. {} command has been executed".format(command)

    def close(self):
        return "PostgreSQLApp. Connection closed"


sql = SQLiteApp(any_attr="some_value", connection=Connection(db_name="My Db"))
print(sql.connect()) # connection to MyDb
print(sql.execute("SELECT")) # executed
# print(sql.execute("INNER JOIN")) #error, invalid command
print(sql.connection.closed) #False
print(sql.close())
print(sql.connection.closed) #True
print(sql.connect())
print(sql.connection.closed) #False
print(sql.close())
print(sql.connection.closed) #True
print('*' * 60)
mysql = MySQLApp(connection=Connection(db_name="MySQL Db"))
print(mysql.connect())
print(mysql.execute("UPDATE"))
print(mysql.close())
print("*" * 60)
postgres = PostgreSQLApp(connection=Connection(db_name="My Db"), credentials={"username": '', "password": ''})
# postgres = PostgreSQLApp(connection=Connection(db_name="My Db"), credentials={"username": ''}) #error
print(postgres.connect())
# # print(mysql.execute("Inner join"))
print(postgres.execute("SELECT"))
print(postgres.close())

