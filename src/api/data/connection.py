from os import environ

from peewee import MySQLDatabase

from set_config import get_settings


def get_database_name() -> str:
    database = get_settings()

    if database["database"] in ("production", "staging"):
        return environ.get("DATABASE_NAME")

    return "db_test"


def get_mysql_credentials() -> dict:
    return dict(
        host=environ.get("DATABASE_HOST"),
        port=environ.get("DATABASE_PORT"),
        name=get_database_name(),
        username=environ.get("DATABASE_USER"),
        passwd=environ.get("DATABASE_PASSWD")
    )


class Database:
    credentials = get_mysql_credentials()
    connect = MySQLDatabase(
        **credentials
    )
