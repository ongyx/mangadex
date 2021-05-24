# coding: utf8

from mangadex_openapi.wrapper import QuickClient

client = QuickClient()

mid = "a96676e5-8ae2-425e-b549-7f15dd34a6d8"


def test_page_urls():

    chapters = client.feed_chapters(mid)
    pages = client.pages(chapters.results[0])
    # print(pages)


def test_cover():

    covers = client.search_covers(manga=[mid])
