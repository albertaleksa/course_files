from dbs.db import DB
from dbs.database import DataBase


class LogTable(DataBase):
    """
    Class for working with table (log)
    """
    def add_log(self, text, user):
        """
        Add info into table (log)
        :param text: text for adding
        :param user: user for adding
        :return:
        """
        try:
            sql = "INSERT INTO logs (text, user) VALUES (%s, %s)"
            log_id = DB.insert(self, sql, (text, user,))
            print(f"Added log {log_id}")
        except Exception as err:
            print(f"Error: {err}")

    def add_logs(self, log):
        """
        Add bulk of info into table (log)
        :param log: list of users for adding
        :return:
        """
        try:
            sql = "INSERT INTO logs (text, user) VALUES (%s, %s)"
            row_count = DB.insertmany(self, sql, log)
            print(f"Added {row_count} row(s)!")
        except Exception as err:
            print(f"Error: {err}")

    def update_log(self, id, text):
        """
        Update info in table (log)
        :param id: id for searching row for updating
        :param text: text for updating
        :return:
        """
        try:
            sql = "UPDATE logs SET text = %s WHERE id = %s"
            row_count = DB.update(self, sql, (text, id,))
            print(f"Updated {row_count} row(s)!")
        except Exception as err:
            print(f"Error: {err}")

    def get_logs(self):
        """
        Get all data from table (log)
        :return:
        """
        try:
            sql = "SELECT * FROM logs ORDER BY created DESC"
            result = DB.fetch(self, sql)
            if result:
                for row in result:
                    print(row)
            else:
                print("Not Found")
        except Exception as err:
            print(f"Error: {err}")

    def get_log(self, id):
        """
        Get data for specific id from table (log)
        :param id: id for searching info
        :return:
        """
        try:
            sql = "SELECT * FROM logs WHERE id = %s"
            row = DB.fetchone(self, sql, (id,))
            if row:
                print(row)
            else:
                print("Not Found")
        except Exception as err:
            print(f"Error: {err}")

    def delete_log(self, id):
        """
        Delete data with specific id from table (log)
        :param id: id for searching info
        :return:
        """
        try:
            sql = "DELETE FROM logs WHERE id = %s"
            row_count = DB.update(self, sql, (id,))
            print(f"Deleted {row_count} row(s)!")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    pass
