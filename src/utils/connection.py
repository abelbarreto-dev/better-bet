from os import getenv

from pymysql import install_as_MySQLdb

from dotenv import load_dotenv

from peewee import MySQLDatabase

from set_config import get_settings

install_as_MySQLdb()


def get_database_name() -> str:
    database = get_settings()

    if database["database"] in ("production", "staging"):
        return getenv("DATABASE_NAME")

    return "db_test"


def get_mysql_credentials() -> dict:
    load_dotenv()

    return dict(
        host=getenv("DATABASE_HOST"),
        port=int(getenv("DATABASE_PORT")),
        database=get_database_name(),
        user=getenv("DATABASE_USER"),
        password=getenv("DATABASE_PASSWD")
    )


class Database:
    _credentials = get_mysql_credentials()
    _connection = None

    @classmethod
    def connect(cls) -> MySQLDatabase:
        if cls._connection is None:
            cls._connection = MySQLDatabase(**cls._credentials)

        return cls._connection
