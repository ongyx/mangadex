# coding: utf8
"""ISO 639-1/2 language code dataset mapping.
Dataset sourced from https://github.com/haliaeetus/iso-639.
"""

from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass

from ..utils import snake_case

DATASET_PATH = pathlib.Path(__file__).parent / "dataset.json"
DATASET_KEYS = frozenset(["family", "name", "nativeName", "wikiUrl"])


@dataclass
class Language:
    code1: str
    code2: str
    family: str
    name: str
    native_name: str
    wiki_url: str

    @classmethod
    def _from_dataset(cls, lang: dict) -> Language:
        code1 = lang.pop("639-1")
        code2 = lang.pop("639-2")

        return cls(
            code1=code1, code2=code2, **{snake_case(k): lang[k] for k in DATASET_KEYS}
        )


with DATASET_PATH.open() as f:
    DATASET = {
        code: Language._from_dataset(lang) for code, lang in json.load(f).items()
    }
