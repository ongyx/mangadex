# coding: utf8

import random

import mangadex_openapi as mangadex
from mangadex_openapi.wrapper.core import Chapter


def test_page_urls():
    api = mangadex.MangaApi()

    chapters = api.get_manga_id_feed("a96676e5-8ae2-425e-b549-7f15dd34a6d8")

    chapter = Chapter(resp=random.choice(chapters.results))
    print(chapter.pages)
