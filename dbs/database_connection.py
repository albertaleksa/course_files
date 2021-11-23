from dbs.log_table import LogTable
from dbs.friends_table import FriendsTable
import dbs.cfg as cfg


def t_logs():
    # connect to the specific database cfg.DB_NAME
    logData = LogTable.db_connection(cfg.CONFIG, cfg.DB_NAME)

    # connect to server without specific database
    # database = LogTable(cfg.CONFIG)

    # create database
    logData.create_database(cfg.DB_NAME)
    logData.create_database("python2")
    # show all databases
    logData.show_databases()
    # delete database
    logData.drop_database("python")
    logData.show_databases()
    logData.create_database("python")

    # create tables from cfg.TABLES
    logData.create_tables(cfg.DB_NAME, cfg.TABLES)

    # add data into table Log
    logData.add_log("This is log one", "Brad")

    users = [
        ("This is log two", "Jeff"),
        ("This is log three", "Jane"),
        ("This is log four", "John")
    ]

    logData.add_logs(users)

    # get info from table Log
    logData.get_logs()
    # get data from Log by id
    logData.get_log(2)
    logData.get_log(4)

    # update table log
    logData.update_log(3, 'Updated log')
    logData.get_logs()
    # delete data from log by id
    logData.delete_log(3)
    logData.get_logs()


def t_friends():
    friendsData = FriendsTable.db_connection(cfg.CONFIG, cfg.DB_NAME)

    friendsData.show_databases()

    # friendsData.add_friend("Steve", "Irwin", 9)
    # friendsData.add_friend("Nikki", "Six", 8)
    # friendsData.add_friend("Johnny", "Depp", 10)

    people = [
        ("Joey", "Ramon", 9),
        ("Kurt", "Cobain", 9),
        ("Iggy", "Pop", 8),
        ("Ozzy", "Osbourne", 7),
        ("Jonathan", "Davis", 9)
    ]

    # friendsData.add_friends(people)
    friendsData.get_friends()
    # friendsData.get_friend(5)

    # friendsData.update_friend(6, 7)
    # friendsData.delete_friend(6)
    friendsData.get_friends()

    # friendsData.create_database("python3")
    friendsData.drop_database("python2")


def run():
    t_friends()
    # t_logs()


if __name__ == "__main__":
    run()
