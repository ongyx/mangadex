# coding: utf8
"""Various classes that wrap the generated code in mangadex_openapi."""

from typing import List

import mangadex_openapi as mangadex


class APIDelegate:
    def __init__(self, client: mangadex.ApiClient):
        self._client = client
        self._apis = {}

    def __getattr__(self, attr):
        # i.e accessing self.manga will initalize MangaApi and save it in self._apis
        if attr not in self._apis:
            self._apis[attr] = getattr(mangadex, f"{attr.capitalize()}Api")(
                self._client
            )

        return self._apis[attr]


class Client:
    def __init__(self):
        self.client = mangadex.ApiClient()
        self.api = APIDelegate(self.client)
        self.auth = None

    def create_account(self, username: str, password: str, email: str):
        """Create a Mangadex account.

        Note that you have to activate the account before you can use it.
        Check the email's inbox for an actvation code, and then run client.activate_account("<activation code>").
        """

        self.api.account.post_account_create(
            mangadex.CreateAccount(username=username, password=password, email=email)
        )

    def login(self, username: str, password: str):
        """Authenticate this client by logging in.

        Args:
            username: The account name.
            password: The account password.
        """

        self.auth = self.api.auth.post_auth_login(
            mangadex.Login(username=username, password=password)
        )
        self.client.default_headers[
            "Authorization"
        ] = f"Bearer {self.auth.token.session}"

    def logout(self):
        """Deauthenticate this client by logging out."""
        self.api.auth.post_auth_logout()

    def pages(
        self, chapter: mangadex.ChapterResponse, saver: bool = False
    ) -> List[str]:
        attrs = chapter.data.attributes

        base_url = self.api.athome.get_at_home_server_chapter_id(
            chapter.data.id
        ).base_url

        if saver:
            mode = "data_saver"
            urls = attrs.data_saver
        else:
            mode = "data"
            urls = attrs.data

        return ["/".join([base_url, mode, attrs.hash, url]) for url in urls]

    def search_manga(self, **criteria):
        return self.api.search.get_search_manga(**criteria)

    def search_chapters(self, **criteria):
        return self.api.search.get_chapter(**criteria)
