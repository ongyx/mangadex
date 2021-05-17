# coding: utf8
"""Various classes that wrap the generated code in mangadex_openapi."""

from typing import Optional

import mangadex_openapi as mangadex


class APIDelegate:
    def __init__(self, client: mangadex.ApiClient):
        self._client = client
        self._apis = {}

    def __getattr__(self, attr):
        # i.e self.manga will initalize MangaApi and save it in self._apis
        if attr not in self._apis:
            self._apis[attr] = getattr(mangadex, f"{attr.capitalize()}Api")(
                self._client
            )

        return self._apis[attr]


class Client:
    def __init__(self):
        self.client = mangadex.ApiClient()
        self.api = APIDelegate(self.client)

    def login(self, username: str, password: str):
        self.api.auth.post_auth_login(
            mangadex.Login(username=username, password=password)
        )

    def search_manga(self, **criteria):
        return self.api.search.get_search_manga(**criteria)

    def search_chapters(self, **criteria):
        return self.api.search.get_chapter(**criteria)


class Base:
    def __init__(
        self, client: Optional[mangadex.ApiClient] = None, id: Optional[str] = None
    ):
        if client is None:
            client = mangadex.ApiClient()

        self.client = client
        self.id = id
        self.api = getattr(mangadex, f"{self.__class__.__name__}Api")(self.client)


class Chapter(Base):
    def __init__(
        self,
        resp: Optional[mangadex.ChapterResponse] = None,
        saver: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self._pages = None

        if self.id is not None:
            self.resp = self.api.get_chapter_id(self.id)
        else:
            self.resp = resp

        self.saver = saver

    @property
    def pages(self):

        if self._pages is None:
            attrs = self.resp.data.attributes

            base_url = (
                mangadex.AtHomeApi(self.client)
                .get_at_home_server_chapter_id(self.resp.data.id)
                .base_url
            )

            if self.saver:
                mode = "data_saver"
                urls = attrs.data_saver
            else:
                mode = "data"
                urls = attrs.data

            self._pages = ["/".join([base_url, mode, attrs.hash, url]) for url in urls]

        return self._pages
