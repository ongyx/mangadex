# mangadex_openapi

Python API to mangadex.org, generated using [swagger-codegen](https://github.com/swagger-api/swagger-codegen).

## Usage

A higher-level API is provided for common tasks (docs [here](API.md)):

```python
from mangadex_openapi.wrapper import api

class MangaClient(api.Client, api.MangaMixin, api.ChapterMixin):
    pass

client = MangaClient()

chapters = client.feed_chapters("a96676e5-8ae2-425e-b549-7f15dd34a6d8")
pages = client.pages(chapters.results[0])
```

You can also directly use the API like this (docs [here](api_docs/README.md)):

```python
import mangadex_openapi as mangadex

client = mangadex.ApiClient()

manga_api = mangadex.MangaApi(client)

random_manga = manga_api.get_manga_random()
```

The version of this API will remain at 0.y.z until the Mangadex API itself is out of beta (and considered stable).

## Building

Make sure you have installed the following:

- `curl`
- `java` (at least Java 8)
- `black` (installed if you ran `flit install`)

The build script will tell you if you haven't installed these yet.

Then, run the build script in a Bash shell:

```bash
$ ./build.sh
```

This will download the codegen.jar artifact if it does not exist, update the spec if there are any changes, and (re)generate the API code.

If you only want to update the spec (inspect differences) without regenerating:

```bash
$ ./build.sh nogen
```

## Spec Changes

This section attempts to document changes in the spec from version to version.

Legend:

- ⭕: bugfix, probably won't break existing code
- ❗: minor change, may break existing code
- 💥: major change, will break existing code

### 5.0.12 (Latest)

- ❗ Added endpoint `/cover/{id}`.
     Given a cover UUID, it returns the filename of the cover.
- ❗ Added endpoint `/cover`.
     This can be used to search for manga covers by manga id.

### 5.0.8

- ❗ Removed status code 204 from endpoint `/manga`.
- ❗ Added endpoint `/manga/{id}/aggregate`:
     Given a manga UUID, it returns a summary of the volumes in the manga.
     Any chapter without a volume is grouped under the key `N/A`.
- ❗ Added status code 204 to endpoints
     `/group`,
     `/chapter`,
     `/user/follows/manga/feed`,
     `/list/{id}/feed`,
     `/author`,
     `/manga/{id}/feed`,
     `/user/follows/group`,
     `/user/follows/user` and
     `/user/follows/manga`.

### 5.0.7

- ❗ Added param `order` to endpoint `/author`:
     specifies whether to return results in `asc`ending or `desc`ending order.

- ❗ Added endpoint `/manga/read`:
     Given a list of manga UUIDs, it returns an array of chapter UUIDs marked as read (requries login)

- 💥 The properties `title`, `altTitles` and `description` in MangaAttributes are now of type LocalizedString
     (localized string mapped to 2-5 letter language code)

- 💥 The property `tags` in MangaAttributes now has items of type Tag.

- ❗ Added properties `name`, `description` and `group` to TagAttributes.
     The former's two types are LocalizedString, the latter's type is string.

### 5.0.5

First version that the mangadex_openapi module was generated from.

## Todo

- [ ] Create a wrapper around the API to make it easier to use.

## License

MIT.
