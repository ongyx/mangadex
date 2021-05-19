# coding: utf8

import datetime


def camel_case(name: str) -> str:
    return "".join(n.capitalize() for n in name.split("_"))


def convert_datetime(fields: dict):
    for key, value in fields.items():
        if "at_since" in key and isinstance(value, datetime.datetime):
            fields[key] = value.isoformat()
