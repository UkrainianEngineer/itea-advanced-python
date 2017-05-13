class BaseExceptionHandler(Exception):
    """Base class for framework exceptions."""
    pass


class PostgreSQLConnectionRefusedError(BaseExceptionHandler):
    pass


class ConnectionClosedError(BaseExceptionHandler):
    pass


class InvalidCommandError(BaseExceptionHandler):
    pass


class Connection(object):
    """Provides dummy connection."""
    def __init__(self, db_name):
        """
        Args:
            db_name (str): Database name.
        """
        self.db_name = db_name

    def __str__(self):
        return "Connection to {}.".format(self.db_name)


class BaseFramework(object):
    """Base framework provides possibility to connect to database.
    It can be used as a context manager:

        with SQLiteApp(connection=Connection("my_db")) as app:
            app.execute("select")

    Attributes:
        allowed_commands (list): Commands that can be executed.
    """
    allowed_commands = ["SELECT", "INSERT", "UPDATE", "DELETE"]

    def __init__(self, connection, **kwargs):
        """
        Args:
            connection (object): Connection instance.
            **kwargs: Additional parameters that can be set as
            attributes.
        """
        self.connection = connection
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def connect(self):
        return self.connection

    def execute(self, command):
        """
        Args:
            command (str): Database command.
        Returns:
            str: Valid database command.
        """
        if not self.connection:
            raise ConnectionClosedError("Command cannot be executed, "
                                        "the connection is closed.")
        if not command.upper() in self.allowed_commands:
            raise InvalidCommandError("Provide valid command.")
        return command.upper()

    def close(self):
        self.connection = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.close()


class SQLiteApp(BaseFramework):

    def connect(self):
        conn = super(SQLiteApp, self).connect()
        return 'SQLiteApp. {}'.format(conn)

    def execute(self, command):
        command = super(SQLiteApp, self).execute(command)
        return "SQLiteApp. {} command has been executed.".format(command)

    def close(self):
        database_name = self.connection.db_name
        super(SQLiteApp, self).close()
        return "SQLiteApp. Connection to {} closed".format(database_name)


class MySQLApp(BaseFramework):

    def connect(self):
        conn = super(MySQLApp, self).connect()
        return 'MySQLApp. {}'.format(conn)

    def execute(self, command):
        command = super(MySQLApp, self).execute(command)
        return "MySQLApp. {} command has been executed.".format(
            command
        )

    def close(self):
        database_name = self.connection.db_name
        super(MySQLApp, self).close()
        return "MySQLApp. Connection to {} closed.".format(
            database_name
        )


class PostgreSQLApp(BaseFramework):
    def __init__(self, credentials, **kwargs):
        """
        Args:
            credentials (dict): Username and password.
        """
        self.credentials = credentials
        super(PostgreSQLApp, self).__init__(**kwargs)

    def connect(self):
        """ If any of credentials is missing, raise an error."""
        if ("username" not in self.credentials or
                "password" not in self.credentials):
            raise PostgreSQLConnectionRefusedError("Provide username "
                                                   "and password.")
        return super(PostgreSQLApp, self).connect()

    def execute(self, command):
        command = super(PostgreSQLApp, self).execute(command)
        return "PostgresSQLApp. {} command has been executed.".format(command)

    def close(self):
        database_name = self.connection.db_name
        super(PostgreSQLApp, self).close()
        return "PostgreSQLApp. Connection to {} closed.".format(
            database_name)


sql = SQLiteApp(any_attr="some_value", connection=Connection(db_name="My Db"))
print(sql.connect())  # connection to MyDb
print(sql.execute("SELECT"))  # executed
# print(sql.execute("INNER JOIN")) # InvalidCommandError
print(sql.close())
# print(sql.execute("Select")) # ConnectionClosedError
print('*' * 60)
mysql = MySQLApp(connection=Connection(db_name="MySQL Db"))
print(mysql.connect())
print(mysql.execute("UPDATE"))
print(mysql.close())
print("*" * 60)
postgres = PostgreSQLApp(connection=Connection(db_name="My Db"),
                         credentials={"username": '', "password": ''})
# postgres = PostgreSQLApp(connection=Connection(db_name="My Db"),
# credentials={"username": ''}) #error
# print(postgres.connect()) #PostgreSQLConnectionRefusedError
# print(mysql.execute("Inner join")) #ConnectionClosedError
print(postgres.connect())
print(postgres.execute("SELECT"))
print(postgres.close())
