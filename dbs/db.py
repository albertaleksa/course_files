import mysql.connector
from mysql.connector import errorcode

# cur = conn.cursor()  //creates new cursor object for executing SQL statements
# conn.commit()  //Commits the transactions
# conn.rollback()  //Roll back the transactions
# conn.close()  //closes the connection
# conn.callproc(proc,param)  //call stored procedure for execution
# conn.getsource(proc)  //fetches stored procedure code


class DB:
    """
    Class for working with database MySQL
    using module mysql.connector

    """
    def __init__(self, cfg):
        """
        Constructor
        Create connection to DB (when the instance of the class is initialising)
        :param cfg: params for connection (host, user, passwd)
        """
        self._connection = None
        try:
            self._connection = mysql.connector.connect(**cfg)
            print("MySQL Database connection successful")
        except mysql.connector.Error as err:
            print(f"Database connection failed due to {err}")

    def __del__(self):
        """
        Destructor
        Close the connection
        :return:
        """
        if self._connection.is_connected():
            self._connection.close()
            print("MySQL connection is closed")

    @classmethod
    def db_connection(cls, cfg, db_name):
        """
        Create connection to DB with specific database
        :param cfg: params for connection (host, user, passwd)
        :param db_name: database name
        :return: instance of the class by calling Constructor
        """
        my_cfg = cfg.copy()
        my_cfg['database'] = db_name
        return cls(my_cfg)

    def _query(self, sql, args):
        """
        Execute query and return cursor
        :param sql: sql query
        :param args: params for query
        :return: MySQLCursor
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute(sql, args)
            return cursor
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create_db(self, sql, args=None):
        """
        Execute query for creating database.
        Close cursor after execution
        :param sql: sql query
        :return:
        """
        try:
            cursor = self._query(sql, args or ())
        except mysql.connector.Error as err:
            print(f"Database wasn't created successfully: {err}")
        finally:
            cursor.close()

    def create_tb(self, db_name, sql, args=None):
        """
        Execute query for creating table
        Close cursor after execution
        :param db_name:  database name
        :param sql: sql query
        :param args: params for query
        :return:
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute(f"USE {db_name}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print(f"Database [{db_name}] wasn't created")
        try:
            cursor.execute(sql, args or ())
            self._connection.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already exists")
            else:
                print(f"Table wasn't created successfully!: {err}")
        finally:
            cursor.close()

    def drop_db(self, sql):
        """
        Execute query for deleting database.
        Close cursor after execution
        :param sql: sql query
        :return:
        """
        try:
            cursor = self._query(sql, ())
        except mysql.connector.Error as err:
            print(f"Drop database failed due to: {err}")
        finally:
            cursor.close()

    def insert(self, sql, args=None):
        """
        Execute query for insert info into table
        Close cursor after execution
        :param sql: sql query
        :param args: params for query
        :return: id of inserted row
        """
        try:
            cursor = self._query(sql, args or ())
            id = cursor.lastrowid
            self._connection.commit()
            return id
        except mysql.connector.Error as err:
            print(f"Data wasn't inserted successfully: {err}")
        finally:
            cursor.close()

    def insertmany(self, sql, args=None):
        """
        Execute query for insert bulk of info into table
        Close cursor after execution
        :param sql: sql query
        :param args: params for query
        :return: number of inserted rows
        """
        try:
            cursor = self._connection.cursor()
            cursor.executemany(sql, args or ())
            self._connection.commit()
            rowcount = cursor.rowcount
            return rowcount
        except mysql.connector.Error as err:
            print(f"Data wasn't inserted successfully: {err}")
        finally:
            cursor.close()

    def update(self, sql, args=None):
        """
        Execute query for update info into table
        Close cursor after execution
        :param sql: sql query
        :param args: params for query
        :return: number of updated rows
        """
        try:
            cursor = self._query(sql, args or ())
            self._connection.commit()
            rowcount = cursor.rowcount
            return rowcount
        except mysql.connector.Error as err:
            print(f"Data wasn't updated successfully: {err}")
        finally:
            cursor.close()

    def fetch(self, sql, args=None):
        """
        Execute query for retrieve data from table
        Close cursor after execution
        :param sql: sql query
        :param args: params for query
        :return: list of rows
        """
        rows = []
        try:
            cursor = self._query(sql, args or ())
            if cursor.with_rows:
                rows = cursor.fetchall()
            return rows
        except mysql.connector.Error as err:
            print(f"Retrieve data failed due to: {err}")
        finally:
            cursor.close()

    def fetchone(self, sql, args=None):
        """
        Execute query for retrieve one row of data from table
        Close cursor after execution
        :param sql: sql query
        :param args: params for query
        :return: row
        """
        row = None
        try:
            cursor = self._query(sql, args or ())
            if cursor.with_rows:
                row = cursor.fetchone()
            return row
        except mysql.connector.Error as err:
            print(f"Retrieve data failed due to: {err}")
        finally:
            cursor.close()


if __name__ == "__main__":
    pass
