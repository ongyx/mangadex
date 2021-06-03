# DEPRECIATED

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

This project is no longer maintained. You should use the [mangadex](https://github.com/EMACC99/mangadex) module instead.

If you do really want to still use this:

1. Increment `API_VERSION` in [build.sh](./build.sh).
2. Build with `./build.sh` (updates the auto-generated API code).
3. Update the wrapper documentation with `./create_docs.sh`.

# mangadex_openapi

Python API to mangadex.org, generated using [swagger-codegen](https://github.com/swagger-api/swagger-codegen).

## Usage

A higher-level API is provided for common tasks (docs [here](API.md)):

```python
import mangadex_openapi as mangadex

client = mangadex.QuickClient()

manga_id = "a96676e5-8ae2-425e-b549-7f15dd34a6d8"

# get the chapters for the manga id...
chapters = client.chapters(manga_id)

# ...and get a list of page urls for the first chapter in the result.
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

-  `curl`
-  `java` (at least Java 8)
-  `black` (installed if you ran `flit install`)

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

### 5.0.20

This is the final version mangadex_openapi will be updated to.

- Another version bump.

### 5.0.17

- Added documentation on how to retrieve manga covers.
- Added a `none` value to the contentRating enum.
- All GET endpoints for UUIDs (i.e get-manga-id, get-chapter-id, get-cover-id, etc.) now return 404 with an ErrorResponse if the UUID was not found.

### 5.0.15

- Version bump, idk why (maybe some low-level API change?)

### 5.0.13

- Changed name of endpoint `/cover/{id}` from `get-cover-id` to `get-cover`.
  Code relying on calls to `CoverApi.get_cover_0` will have to use `CoverApi.get_cover` instead.

### 5.0.12

- Added endpoint `/cover/{id}`.
  Given a cover UUID, it returns the filename of the cover.
- Added endpoint `/cover`.
  This can be used to search for manga covers by manga id.

### 5.0.8

- Removed status code 204 from endpoint `/manga`.
- Added endpoint `/manga/{id}/aggregate`:
  Given a manga UUID, it returns a summary of the volumes in the manga.
  Any chapter without a volume is grouped under the key `N/A`.
- Added status code 204 to endpoints
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

- Added param `order` to endpoint `/author`:
  specifies whether to return results in `asc`ending or `desc`ending order.

- Added endpoint `/manga/read`:
  Given a list of manga UUIDs, it returns an array of chapter UUIDs marked as read (requries login)

- The properties `title`, `altTitles` and `description` in MangaAttributes are now of type LocalizedString
  (localized string mapped to 2-5 letter language code)

- The property `tags` in MangaAttributes now has items of type Tag.

- Added properties `name`, `description` and `group` to TagAttributes.
  The former's two types are LocalizedString, the latter's type is string.

### 5.0.5

First version that the mangadex_openapi module was generated from.

## Todo

-  [x] Create a wrapper around the API to make it easier to use. (Most post/delete calls not done yet)

## License

MIT.
