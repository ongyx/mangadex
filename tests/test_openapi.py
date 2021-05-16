# coding: utf8

import mangadex_openapi as mangadex

# monkeypatch client
client = mangadex.ApiClient()


def test_manga():
    manga_api = mangadex.MangaApi(client)

    resp = manga_api.get_manga_random()
    # print(resp)
