# mangadex

Python API to mangadex.org, generated using [swagger-codegen](https://github.com/swagger-api/swagger-codegen).

## Usage

You can directly use the API like this:

```
import mangadex

client = mangadex.ApiClient()

manga_api = mangadex.MangaApi(client)

random_manga = manga_api.get_manga_random()
```

For more info on using the API, read the auto-generated docs [here](api_docs/README.md).

The generated code *may* change at any time because of changes to the underlying OpenAPI document.
Hence, the version of this API will remain at 0.y.z until the Mangadex API itself is out of beta (and considered stable).

## Building

Make sure you have installed the following:

- `curl`
- `java` (at least Java 8)

The build script will tell you if you haven't installed these yet.



## Todo

- [ ] Create a wrapper around the API to make it easier to use.

## License

MIT.
