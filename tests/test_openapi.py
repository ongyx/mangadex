# coding: utf8

import mangadex_openapi as mangadex

# monkeypatch client
client = mangadex.ApiClient()


def test_manga():
    manga_api = mangadex.MangaApi(client)

    resp = manga_api.get_manga_random()
    # print(resp)


"""
def test_cover():
    manga_api = mangadex.CoverApi(client)
    manga_api.get_cover(manga="a96676e5-8ae2-425e-b549-7f15dd34a6d8")
"""
