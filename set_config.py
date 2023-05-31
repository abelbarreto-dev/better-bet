from pathlib import Path

from json import (
    loads as to_dict,
    dumps as to_json,
)


FILE = {
    "test": "../settings.json",
    "default": "../../../settings.json"
}


def get_settings() -> dict:
    file = ""

    if Path(FILE["test"]).is_file():
        file = FILE["test"]
    elif Path(FILE["default"]).is_file():
        file = FILE["default"]

    with open(file, "r", encoding="utf-8") as new_file:
        data_file = to_dict(new_file.read())

    return data_file


def to_testing() -> None:
    data_file = get_settings()

    data_file["database"] = "testing"

    with open(FILE["test"], "w", encoding="utf-8") as file:
        file.writelines(to_json(data_file, indent=4))


def to_staging() -> None:
    data_file = get_settings()

    data_file["database"] = "staging"

    with open(FILE["default"], "w", encoding="utf-8") as file:
        file.writelines(to_json(data_file, indent=4))


def to_production() -> None:
    data_file = get_settings()

    data_file["database"] = "production"

    with open(FILE["default"], "w", encoding="utf-8") as file:
        file.writelines(to_json(data_file, indent=4))
