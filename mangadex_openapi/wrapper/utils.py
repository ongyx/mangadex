# coding: utf8

import datetime
from typing import List

from ..models import Relationship


def camel_case(name: str) -> str:
    return "".join(n.capitalize() for n in name.split("_"))


def convert_datetime(fields: dict):
    for key, value in fields.items():
        if "at_since" in key and isinstance(value, datetime.datetime):
            fields[key] = value.isoformat()


def rselect(type: str, relationships: List[Relationship]) -> List[str]:
    """Select relation ids by type.

    Args:
        type: The type of relation to select.
        relations: A list of Relationship objects, usually available as the .relationships attribute in models.

    Returns:
        The relation ids.
    """

    ids = []

    for relation in relationships:
        if relation.type == type:
            ids.append(relation.id)

    return ids
