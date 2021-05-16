# mangadex_openapi

Python API to mangadex.org, generated using [swagger-codegen](https://github.com/swagger-api/swagger-codegen).

## Usage

You can directly use the API like this:

```
import mangadex_openapi as mangadex

client = mangadex.ApiClient()

manga_api = mangadex.MangaApi(client)

random_manga = manga_api.get_manga_random()
```

For more info on using the API, read the auto-generated docs [here](api_docs/README.md).

The version of this API will remain at 0.y.z until the Mangadex API itself is out of beta (and considered stable).

## Building

Make sure you have installed the following:

- `curl`
- `java` (at least Java 8)

The build script will tell you if you haven't installed these yet.

Then, run the build script in a Bash shell:

```bash
$ ./build.sh
```

This will download the codegen.jar artifact if it does not exist, update the spec if there are any changes, and (re)generate the API code.

## Todo

- [ ] Create a wrapper around the API to make it easier to use.

## License

MIT.
