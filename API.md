# Table of Contents

* [mangadex\_openapi.wrapper.api](#mangadex_openapi.wrapper.api)
  * [Client](#mangadex_openapi.wrapper.api.Client)
    * [ping](#mangadex_openapi.wrapper.api.Client.ping)
  * [AccountMixin](#mangadex_openapi.wrapper.api.AccountMixin)
    * [create\_account](#mangadex_openapi.wrapper.api.AccountMixin.create_account)
    * [activate\_account](#mangadex_openapi.wrapper.api.AccountMixin.activate_account)
    * [actiavte\_resend](#mangadex_openapi.wrapper.api.AccountMixin.actiavte_resend)
    * [recover\_account](#mangadex_openapi.wrapper.api.AccountMixin.recover_account)
    * [recover\_complete](#mangadex_openapi.wrapper.api.AccountMixin.recover_complete)
  * [AuthMixin](#mangadex_openapi.wrapper.api.AuthMixin)
    * [login](#mangadex_openapi.wrapper.api.AuthMixin.login)
    * [logout](#mangadex_openapi.wrapper.api.AuthMixin.logout)
    * [refresh](#mangadex_openapi.wrapper.api.AuthMixin.refresh)
    * [check](#mangadex_openapi.wrapper.api.AuthMixin.check)
  * [AtHomeMixin](#mangadex_openapi.wrapper.api.AtHomeMixin)
    * [server](#mangadex_openapi.wrapper.api.AtHomeMixin.server)
  * [AuthorMixin](#mangadex_openapi.wrapper.api.AuthorMixin)
    * [author](#mangadex_openapi.wrapper.api.AuthorMixin.author)
  * [ChapterMixin](#mangadex_openapi.wrapper.api.ChapterMixin)
    * [chapter](#mangadex_openapi.wrapper.api.ChapterMixin.chapter)
    * [mark\_read](#mangadex_openapi.wrapper.api.ChapterMixin.mark_read)
    * [mark\_unread](#mangadex_openapi.wrapper.api.ChapterMixin.mark_unread)
  * [CoverMixin](#mangadex_openapi.wrapper.api.CoverMixin)
    * [cover](#mangadex_openapi.wrapper.api.CoverMixin.cover)
  * [MangaMixin](#mangadex_openapi.wrapper.api.MangaMixin)
    * [manga\_](#mangadex_openapi.wrapper.api.MangaMixin.manga_)
    * [aggregate](#mangadex_openapi.wrapper.api.MangaMixin.aggregate)
    * [feed\_chapters](#mangadex_openapi.wrapper.api.MangaMixin.feed_chapters)
  * [SearchMixin](#mangadex_openapi.wrapper.api.SearchMixin)
    * [search\_authors](#mangadex_openapi.wrapper.api.SearchMixin.search_authors)
    * [search\_chapters](#mangadex_openapi.wrapper.api.SearchMixin.search_chapters)
    * [search\_covers](#mangadex_openapi.wrapper.api.SearchMixin.search_covers)
    * [search\_groups](#mangadex_openapi.wrapper.api.SearchMixin.search_groups)
    * [search\_manga](#mangadex_openapi.wrapper.api.SearchMixin.search_manga)

<a name="mangadex_openapi.wrapper.api"></a>
# mangadex\_openapi.wrapper.api

Classes here wrap parts of the mangadex API for more version-agonistic code.

Almost every API class from mangadex_openapi has a corrosponding mixin
(i.e MangaApi -> MangaMixin).

This keeps the glue code contained within their own classes.

To use a part of the API, subclass Client/AuthedClient and one or more mixins:

class MyClient(AuthedClient, MangaMixin):
    pass

and then initalise it:

client = MyClient()

Finally, use it.

manga = client.manga_("a96676e5-8ae2-425e-b549-7f15dd34a6d8")

<a name="mangadex_openapi.wrapper.api.Client"></a>
## Client Objects

```python
class Client()
```

Base client that wraps mangadex.ApiClient.

**Attributes**:

- `session_token` _str_ - The token for the current session.
- `persist_token` _str_ - The token for the persistent session (can be reused later on).

<a name="mangadex_openapi.wrapper.api.Client.ping"></a>
#### ping

```python
 | ping() -> bool
```

Ping the Mangadex server to check whether it is online.

<a name="mangadex_openapi.wrapper.api.AccountMixin"></a>
## AccountMixin Objects

```python
class AccountMixin()
```

<a name="mangadex_openapi.wrapper.api.AccountMixin.create_account"></a>
#### create\_account

```python
 | create_account(**kwargs)
```

Create a Mangadex account.

Note that you have to activate the account before you can use it.
Check the email's inbox for an actvation code, and then run client.activate_account("activation code").

**Arguments**:

- `username` _str_ - The new account name.
- `password` _str_ - The new account password.
- `email` _str_ - The email to register the new account to.

<a name="mangadex_openapi.wrapper.api.AccountMixin.activate_account"></a>
#### activate\_account

```python
 | activate_account(code: str)
```

Activate a Mangadex account using a code sent to its email.

**Arguments**:

- `code` - The activation code.

<a name="mangadex_openapi.wrapper.api.AccountMixin.actiavte_resend"></a>
#### actiavte\_resend

```python
 | actiavte_resend(email: str)
```

Resend an activation code to a new Mangadex account.

**Arguments**:

- `email` - The new account's email.

<a name="mangadex_openapi.wrapper.api.AccountMixin.recover_account"></a>
#### recover\_account

```python
 | recover_account(email: str)
```

Recover a Mangadex account
(i.e if you forgot your password).

A recovery code is sent to the email of the account, so call client.recover_complete("code", "new password").

**Arguments**:

- `email` - The account's email.

<a name="mangadex_openapi.wrapper.api.AccountMixin.recover_complete"></a>
#### recover\_complete

```python
 | recover_complete(code: str, password: str)
```

Complete recovery of a Mangadex account.

**Arguments**:

- `code` - The recovery code sent to the account's email.
- `password` - The new password to change the account to.

<a name="mangadex_openapi.wrapper.api.AuthMixin"></a>
## AuthMixin Objects

```python
class AuthMixin()
```

<a name="mangadex_openapi.wrapper.api.AuthMixin.login"></a>
#### login

```python
 | login(username: str, password: str)
```

Authenticate this client by logging in.

**Arguments**:

- `username` - The account name.
- `password` - The account password.

<a name="mangadex_openapi.wrapper.api.AuthMixin.logout"></a>
#### logout

```python
 | logout()
```

Deauthenticate this client by logging out.

<a name="mangadex_openapi.wrapper.api.AuthMixin.refresh"></a>
#### refresh

```python
 | refresh()
```

Refresh this client's session token (expires every 15 minutes).

<a name="mangadex_openapi.wrapper.api.AuthMixin.check"></a>
#### check

```python
 | check() -> mangadex.CheckResponse
```

Get the authentication status of this client.

<a name="mangadex_openapi.wrapper.api.AtHomeMixin"></a>
## AtHomeMixin Objects

```python
class AtHomeMixin()
```

<a name="mangadex_openapi.wrapper.api.AtHomeMixin.server"></a>
#### server

```python
 | server(**kwargs) -> str
```

Get the server url for a chapter id.

**Arguments**:

- `chapter_id` - The UUID of the chapter.
- `force_port443` - Whether or not to only select servers using port 443 (HTTPS).
  Some networks may block connections to other ports (which Mangadex@Home servers may use).
  Defaults to False.

<a name="mangadex_openapi.wrapper.api.AuthorMixin"></a>
## AuthorMixin Objects

```python
class AuthorMixin()
```

<a name="mangadex_openapi.wrapper.api.AuthorMixin.author"></a>
#### author

```python
 | author(id: str) -> mangadex.AuthorResponse
```

Get an author by id.

<a name="mangadex_openapi.wrapper.api.ChapterMixin"></a>
## ChapterMixin Objects

```python
class ChapterMixin(AtHomeMixin)
```

<a name="mangadex_openapi.wrapper.api.ChapterMixin.chapter"></a>
#### chapter

```python
 | chapter(id: str) -> mangadex.ChapterResponse
```

Get a chapter by id.

<a name="mangadex_openapi.wrapper.api.ChapterMixin.mark_read"></a>
#### mark\_read

```python
 | mark_read(id: str)
```

Mark a chapter by id as read for the current user.

<a name="mangadex_openapi.wrapper.api.ChapterMixin.mark_unread"></a>
#### mark\_unread

```python
 | mark_unread(id: str)
```

Mark a chapter by id as unread for the current user.

<a name="mangadex_openapi.wrapper.api.CoverMixin"></a>
## CoverMixin Objects

```python
class CoverMixin()
```

<a name="mangadex_openapi.wrapper.api.CoverMixin.cover"></a>
#### cover

```python
 | cover(id: str) -> mangadex.CoverResponse
```

Get cover by id.

<a name="mangadex_openapi.wrapper.api.MangaMixin"></a>
## MangaMixin Objects

```python
class MangaMixin()
```

<a name="mangadex_openapi.wrapper.api.MangaMixin.manga_"></a>
#### manga\_

```python
 | manga_(id: str) -> mangadex.MangaResponse
```

Get manga by id.

<a name="mangadex_openapi.wrapper.api.MangaMixin.aggregate"></a>
#### aggregate

```python
 | aggregate(id: str) -> mangadex.InlineResponse200
```

Get a summary of volume and chapter info on manga by id.

<a name="mangadex_openapi.wrapper.api.MangaMixin.feed_chapters"></a>
#### feed\_chapters

```python
 | feed_chapters(id: str, **criteria) -> mangadex.ChapterList
```

Get chapters for a manga by id.

<a name="mangadex_openapi.wrapper.api.SearchMixin"></a>
## SearchMixin Objects

```python
class SearchMixin()
```

<a name="mangadex_openapi.wrapper.api.SearchMixin.search_authors"></a>
#### search\_authors

```python
 | search_authors(**criteria) -> mangadex.AuthorList
```

Search authors by criteria.

<a name="mangadex_openapi.wrapper.api.SearchMixin.search_chapters"></a>
#### search\_chapters

```python
 | search_chapters(**criteria) -> mangadex.ChapterList
```

Search chapters by criteria.

<a name="mangadex_openapi.wrapper.api.SearchMixin.search_covers"></a>
#### search\_covers

```python
 | search_covers(**criteria) -> mangadex.CoverList
```

Search covers by criteria.

<a name="mangadex_openapi.wrapper.api.SearchMixin.search_groups"></a>
#### search\_groups

```python
 | search_groups(**criteria) -> mangadex.ScanlationGroupList
```

Search scanlation groups by criteria.

<a name="mangadex_openapi.wrapper.api.SearchMixin.search_manga"></a>
#### search\_manga

```python
 | search_manga(**criteria) -> mangadex.MangaList
```

Search manga by criteria.

