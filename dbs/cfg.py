# connection to DB MySQL on AWS
CONFIG = {
    'host': 'aws-db-test.cf86h3oxovif.us-east-2.rds.amazonaws.com',
    'user': 'python_user',
    'passwd': 'pythonAws000'
}

DB_NAME = 'python'

DB_NAME_WHITELIST = frozenset(['python', 'python2'])
TB_NAME_WHITELIST = frozenset(['logs', 'friends'])


TABLES= {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

TABLES['friends'] = (
    "CREATE TABLE `friends` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `first_name` varchar(250) NOT NULL,"
    " `last_name` varchar(250) NOT NULL,"
    " `closeness` int(2) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)


if __name__ == "__main__":
    pass
