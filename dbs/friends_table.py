from dbs.db import DB
from dbs.database import DataBase


class FriendsTable(DataBase):
    """
    Class for working with table (friends)
    """
    def add_friend(self, first, last, closeness):
        """
        Add info into table (friends)
        :param first: first name for adding
        :param last: last name for adding
        :param closeness: closeness for adding
        :return:
        """
        try:
            sql = "INSERT INTO friends (first_name, last_name, closeness) VALUES (%s, %s, %s)"
            friend_id = DB.insert(self, sql, (first, last, closeness,))
            print(f"Added friend {friend_id}")
        except Exception as err:
            print(f"Error: {err}")

    def add_friends(self, people):
        """
        Add bulk of info into table (friends)
        :param people: list of people for adding
        :return:
        """
        try:
            sql = "INSERT INTO friends (first_name, last_name, closeness) VALUES (%s, %s, %s)"
            row_count = DB.insertmany(self, sql, people)
            print(f"Added {row_count} row(s)!")
        except Exception as err:
            print(f"Error: {err}")

    def update_friend(self, id, closeness):
        """
        Update info in table (friends)
        :param id: id for searching row for updating
        :param closeness: for updating
        :return:
        """
        try:
            sql = "UPDATE friends SET closeness = %s WHERE id = %s"
            row_count = DB.update(self, sql, (closeness, id,))
            print(f"Updated {row_count} row(s)!")
        except Exception as err:
            print(f"Error: {err}")

    def get_friends(self):
        """
        Get all data from table (friends)
        :return:
        """
        try:
            sql = "SELECT * FROM friends ORDER BY created DESC"
            result = DB.fetch(self, sql)
            if result:
                for row in result:
                    print(row)
            else:
                print("Not Found")
        except Exception as err:
            print(f"Error: {err}")

    def get_friend(self, id):
        """
        Get data for specific id from table (friends)
        :param id: id for searching info
        :return:
        """
        try:
            sql = "SELECT * FROM friends WHERE id = %s"
            row = DB.fetchone(self, sql, (id,))
            if row:
                print(row)
            else:
                print("Not Found")
        except Exception as err:
            print(f"Error: {err}")

    def delete_friend(self, id):
        """
        Delete data with specific id from table (friends)
        :param id: id for searching info
        :return:
        """
        try:
            sql = "DELETE FROM friends WHERE id = %s"
            row_count = DB.update(self, sql, (id,))
            print(f"Deleted {row_count} row(s)!")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    pass
