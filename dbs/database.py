from dbs.db import DB
import dbs.cfg as cfg


class DataBase(DB):
    """
    Class extended from class DB
    Have methods for working with database using sql-queries
    """
    def create_database(self, db_name):
        """
        Create database
        :param db_name: database name
        :return:
        """
        try:
            if db_name in cfg.DB_NAME_WHITELIST:
                sql = f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8'"
                DB.create_db(self, sql)
                print(f"Database [{db_name}] created successfully!")
            else:
                print("You try to create not permitted database")
        except Exception as err:
            print(f"Error: {err}")

    def drop_database(self, db_name):
        """
        Delete database
        :param db_name: database name
        :return:
        """
        try:
            if db_name in cfg.DB_NAME_WHITELIST:
                sql = f"DROP DATABASE IF EXISTS {db_name}"
                DB.drop_db(self, sql)
                print(f"Database [{db_name}] dropped successfully!")
            else:
                print("You try to delete not permitted database")
        except Exception as err:
            print(f"Error: {err}")

    def show_databases(self):
        """
        Show all databases
        :return:
        """
        try:
            sql = "SHOW DATABASES"
            result = DB.fetch(self, sql)
            if result:
                print("List of databases:")
                for row in result:
                    print(f"[{row[0].decode()}]")
            else:
                print("Not Found")
        except Exception as err:
            print(f"Error: {err}")

    def create_tables(self, db_name, tables):
        """
        Create tables
        :param db_name: database name
        :param tables: list of tables
        :return:
        """
        try:
            if db_name in cfg.DB_NAME_WHITELIST:
                for table_name in tables:
                    table_description = tables[table_name]
                    print(f"Creating table ({table_name})... ", end="")
                    DB.create_tb(self, db_name, table_description)
                    print(f"Table ({table_name}) created successfully!")
            else:
                print("You try to create table(s) in not permitted database")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    pass
