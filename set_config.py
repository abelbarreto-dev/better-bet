from json import loads as to_dict, dumps as to_json


FILE = "settings.json"


def get_settings() -> dict:
    with open(FILE, "r", encoding="utf-8") as file:
        data_file = to_dict(file.read())

    return data_file


def to_testing() -> None:
    data_file = get_settings()

    data_file["database"] = "testing"

    with open(FILE, "w", encoding="utf-8") as file:
        file.writelines(to_json(data_file, indent=4))


def to_staging() -> None:
    data_file = get_settings()

    data_file["database"] = "staging"

    with open(FILE, "w", encoding="utf-8") as file:
        file.writelines(to_json(data_file, indent=4))


def to_production() -> None:
    data_file = get_settings()

    data_file["database"] = "production"

    with open(FILE, "w", encoding="utf-8") as file:
        file.writelines(to_json(data_file, indent=4))
