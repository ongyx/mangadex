# mangadex-openapi
MangaDex is an ad-free manga reader offering high-quality images!  This document details our API as it is right now. It is in no way a promise to never change it, although we will endeavour to publicly notify any major change.  # Authentication  You can login with the `/auth/login` endpoint. On success, it will return a JWT that remains valid for 15 minutes along with a session token that allows refreshing without re-authenticating for 1 month.  # Rate limits  The API enforces rate-limits to protect our servers against malicious and/or mistaken use. The API keeps track of the requests on an IP-by-IP basis. Hence, if you're on a VPN, proxy or a shared network in general, the requests of other users on this network might affect you.  At first, a **global limit of 5 requests per second per IP address** is in effect.  > This limit is enforced across multiple load-balancers, and thus is not an exact value but rather a lower-bound that we guarantee. The exact value will be somewhere in the range `[5, 5*n]` (with `n` being the number of load-balancers currently active). The exact value within this range will depend on the current traffic patterns we are experiencing.  On top of this, **some endpoints are further restricted** as follows:  | Endpoint                           | Requests per time period    | Time period in minutes | |------------------------------------|--------------------------   |------------------------| | `POST   /account/create`           | 1                           | 60                     | | `GET    /account/activate/{code}`  | 30                          | 60                     | | `POST   /account/activate/resend`  | 5                           | 60                     | | `POST   /account/recover`          | 5                           | 60                     | | `POST   /account/recover/{code}`   | 5                           | 60                     | | `POST   /auth/login`               | 30                          | 60                     | | `POST   /auth/refresh`             | 30                          | 60                     | | `POST   /author`                   | 10                          | 60                     | | `PUT    /author`                   | 10                          | 1                      | | `DELETE /author/{id}`              | 10                          | 10                     | | `POST   /captcha/solve`            | 10                          | 10                     | | `POST   /chapter/{id}/read`        | 300                         | 10                     | | `PUT    /chapter/{id}`             | 10                          | 1                      | | `DELETE /chapter/{id}`             | 10                          | 1                      | | `POST   /manga`                    | 10                          | 60                     | | `PUT    /manga/{id}`               | 10                          | 60                     | | `DELETE /manga/{id}`               | 10                          | 10                     | | `POST   /cover`                    | 10                          | 1                      | | `PUT    /cover/{id}`               | 10                          | 1                      | | `DELETE /cover/{id}`               | 10                          | 10                     | | `POST   /group`                    | 10                          | 60                     | | `PUT    /group/{id}`               | 10                          | 1                      | | `DELETE /group/{id}`               | 10                          | 10                     | | `GET    /at-home/server/{id}`      | 60                          | 1                      |  Calling these endpoints will further provide details via the following headers about your remaining quotas:  | Header                    | Description                                                                 | |---------------------------|-----------------------------------------------------------------------------| | `X-RateLimit-Limit`       | Maximal number of requests this endpoint allows per its time period         | | `X-RateLimit-Remaining`   | Remaining number of requests within your quota for the current time period  | | `X-RateLimit-Retry-After` | Timestamp of the end of the current time period, as UNIX timestamp          |  # Captchas  Some endpoints may require captchas to proceed, in order to slow down automated malicious traffic. Legitimate users might also be affected, based on the frequency of write requests or due certain endpoints being particularly sensitive to malicious use, such as user signup.  Once an endpoint decides that a captcha needs to be solved, a 403 Forbidden response will be returned, with the error code `captcha_required_exception`. The sitekey needed for recaptcha to function is provided in both the `X-Captcha-Sitekey` header field, as well as in the error context, specified as `siteKey` parameter.  The captcha result of the client can either be passed into the repeated original request with the `X-Captcha-Result` header or alternatively to the `POST /captcha/solve` endpoint. The time a solved captcha is remembered varies across different endpoints and can also be influenced by individual client behavior.  Authentication is not required for the `POST /captcha/solve` endpoint, captchas are tracked both by client ip and logged in user id. If you are logged in, you want to send the session token along, so you validate the captcha for your client ip and user id at the same time, but it is not required.  # Reading a chapter using the API  ## Retrieving pages from the MangaDex@Home network  A valid [MangaDex@Home network](https://mangadex.network) page URL is in the following format: `{server-specific base url}/{temporary access token}/{quality mode}/{chapter hash}/{filename}`  There are currently 2 quality modes: - `data`: Original upload quality - `data-saver`: Compressed quality  Upon fetching a chapter from the API, you will find 4 fields necessary to compute MangaDex@Home page URLs:  | Field                        | Type     | Description                       | |------------------------------|----------|-----------------------------------| | `.data.id`                   | `string` | API Chapter ID                    | | `.data.attributes.hash`      | `string` | MangaDex@Home Chapter Hash        | | `.data.attributes.data`      | `array`  | data quality mode filenames       | | `.data.attributes.dataSaver` | `array`  | data-saver quality mode filenames |  Example ```json GET /chapter/{id}  {   ...,   \"data\": {     \"id\": \"e46e5118-80ce-4382-a506-f61a24865166\",     ...,     \"attributes\": {       ...,       \"hash\": \"e199c7d73af7a58e8a4d0263f03db660\",       \"data\": [         \"x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png\",         ...       ],       \"dataSaver\": [         \"x1-ab2b7c8f30c843aa3a53c29bc8c0e204fba4ab3e75985d761921eb6a52ff6159.jpg\",         ...       ]     }   } } ```  From this point you miss only the base URL to an assigned MangaDex@Home server for your client and chapter. This is retrieved via a `GET` request to `/at-home/server/{ chapter .data.id }`.  Example: ```json GET /at-home/server/e46e5118-80ce-4382-a506-f61a24865166  {   \"baseUrl\": \"https://abcdefg.hijklmn.mangadex.network:12345/some-token\" } ```  The full URL is the constructed as follows ``` { server .baseUrl }/{ quality mode }/{ chapter .data.attributes.hash }/{ chapter .data.attributes.{ quality mode }.[*] }  Examples  data quality: https://abcdefg.hijklmn.mangadex.network:12345/some-token/data/e199c7d73af7a58e8a4d0263f03db660/x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png        base url: https://abcdefg.hijklmn.mangadex.network:12345/some-token   quality mode: data   chapter hash: e199c7d73af7a58e8a4d0263f03db660       filename: x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png   data-saver quality: https://abcdefg.hijklmn.mangadex.network:12345/some-token/data-saver/e199c7d73af7a58e8a4d0263f03db660/x1-ab2b7c8f30c843aa3a53c29bc8c0e204fba4ab3e75985d761921eb6a52ff6159.jpg        base url: https://abcdefg.hijklmn.mangadex.network:12345/some-token   quality mode: data-saver   chapter hash: e199c7d73af7a58e8a4d0263f03db660       filename: x1-ab2b7c8f30c843aa3a53c29bc8c0e204fba4ab3e75985d761921eb6a52ff6159.jpg ```  If the server you have been assigned fails to serve images, you are allowed to call the `/at-home/server/{ chapter id }` endpoint again to get another server.  Whether successful or not, **please do report the result you encountered as detailed below**. This is so we can pull the faulty server out of the network.  ## Report  In order to keep track of the health of the servers in the network and to improve the quality of service and reliability, we ask that you call the MangaDex@Home report endpoint after each image you retrieve, whether successfully or not.  It is a `POST` request against `https://api.mangadex.network/report` and expects the following payload with our example above:  | Field                       | Type       | Description                                                                         | |-----------------------------|------------|-------------------------------------------------------------------------------------| | `url`                       | `string`   | The full URL of the image                                                           | | `success`                   | `boolean`  | Whether the image was successfully retrieved                                        | | `cached `                   | `boolean`  | `true` iff the server returned an `X-Cache` header with a value starting with `HIT` | | `bytes`                     | `number`   | The size in bytes of the retrieved image                                            | | `duration`                  | `number`   | The time in miliseconds that the complete retrieval (not TTFB) of this image took   |  Examples herafter.  **Success:** ```json POST https://api.mangadex.network/report Content-Type: application/json  {   \"url\": \"https://abcdefg.hijklmn.mangadex.network:12345/some-token/data/e199c7d73af7a58e8a4d0263f03db660/x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png\",   \"success\": true,   \"bytes\": 727040,   \"duration\": 235,   \"cached\": true } ```  **Failure:** ```json POST https://api.mangadex.network/report Content-Type: application/json  {  \"url\": \"https://abcdefg.hijklmn.mangadex.network:12345/some-token/data/e199c7d73af7a58e8a4d0263f03db660/x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png\",  \"success\": false,  \"bytes\": 25,  \"duration\": 235,  \"cached\": false } ```  While not strictly necessary, this helps us monitor the network's healthiness, and we appreciate your cooperation towards this goal. If no one reports successes and failures, we have no way to know that a given server is slow/broken, which eventually results in broken image retrieval for everyone.  # Static data  ## Manga publication demographic  | Value            | Description               | |------------------|---------------------------| | shounen          | Manga is a Shounen        | | shoujo           | Manga is a Shoujo         | | josei            | Manga is a Josei          | | seinen           | Manga is a Seinen         |  ## Manga status  | Value            | Description               | |------------------|---------------------------| | ongoing          | Manga is still going on   | | completed        | Manga is completed        | | hiatus           | Manga is paused           | | cancelled        | Manga has been cancelled  |  ## Manga reading status  | Value            | |------------------| | reading          | | on_hold          | | plan\\_to\\_read   | | dropped          | | re\\_reading      | | completed        |  ## Manga content rating  | Value            | Description               | |------------------|---------------------------| | safe             | Safe content              | | suggestive       | Suggestive content        | | erotica          | Erotica content           | | pornographic     | Pornographic content      |  ## CustomList visibility  | Value            | Description               | |------------------|---------------------------| | public           | CustomList is public      | | private          | CustomList is private     |  ## Relationship types  | Value            | Description                    | |------------------|--------------------------------| | manga            | Manga resource                 | | chapter          | Chapter resource               | | cover_art        | A Cover Art for a manga `*`    | | author           | Author resource                | | artist           | Author resource (drawers only) | | scanlation_group | ScanlationGroup resource       | | tag              | Tag resource                   | | user             | User resource                  | | custom_list      | CustomList resource            |  `*` Note, that on manga resources you get only one cover_art resource relation marking the primary cover if there are more than one. By default this will be the latest volume's cover art. If you like to see all the covers for a given manga, use the cover search endpoint for your mangaId and select the one you wish to display.  ## Manga links data  In Manga attributes you have the `links` field that is a JSON object with some strange keys, here is how to decode this object:  | Key   | Related site  | URL                                                                                           | URL details                                                    | |-------|---------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------| | al    | anilist       | https://anilist.co/manga/`{id}`                                                               | Stored as id                                                   | | ap    | animeplanet   | https://www.anime-planet.com/manga/`{slug}`                                                   | Stored as slug                                                 | | bw    | bookwalker.jp | https://bookwalker.jp/`{slug}`                                                                | Stored has \"series/{id}\"                                       | | mu    | mangaupdates  | https://www.mangaupdates.com/series.html?id=`{id}`                                            | Stored has id                                                  | | nu    | novelupdates  | https://www.novelupdates.com/series/`{slug}`                                                  | Stored has slug                                                | | kt    | kitsu.io      | https://kitsu.io/api/edge/manga/`{id}` or https://kitsu.io/api/edge/manga?filter[slug]={slug} | If integer, use id version of the URL, otherwise use slug one  | | amz   | amazon        | N/A                                                                                           | Stored as full URL                                             | | ebj   | ebookjapan    | N/A                                                                                           | Stored as full URL                                             | | mal   | myanimelist   | https://myanimelist.net/manga/{id}                                                            | Store as id                                                    | | raw   | N/A           | N/A                                                                                           | Stored as full URL, untranslated stuff URL (original language) | | engtl | N/A           | N/A                                                                                           | Stored as full URL, official english licenced URL              |

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 5.0.12
- Package version: 0.2.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import mangadex_openapi 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mangadex_openapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi(mangadex_openapi.ApiClient(configuration))
code = 'code_example' # str | 

try:
    # Activate account
    api_response = api_instance.get_account_activate_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_activate_code: %s\n" % e)

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi(mangadex_openapi.ApiClient(configuration))
body = mangadex_openapi.SendAccountActivationCode() # SendAccountActivationCode | The size of the body is limited to 1KB. (optional)

try:
    # Resend Activation code
    api_response = api_instance.post_account_activate_resend(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_activate_resend: %s\n" % e)

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi(mangadex_openapi.ApiClient(configuration))
body = mangadex_openapi.CreateAccount() # CreateAccount | The size of the body is limited to 4KB. (optional)

try:
    # Create Account
    api_response = api_instance.post_account_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_create: %s\n" % e)

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi(mangadex_openapi.ApiClient(configuration))
body = mangadex_openapi.SendAccountActivationCode() # SendAccountActivationCode | The size of the body is limited to 1KB. (optional)

try:
    # Recover given Account
    api_response = api_instance.post_account_recover(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_recover: %s\n" % e)

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi(mangadex_openapi.ApiClient(configuration))
code = 'code_example' # str | 
body = mangadex_openapi.RecoverCompleteBody() # RecoverCompleteBody | The size of the body is limited to 2KB. (optional)

try:
    # Complete Account recover
    api_response = api_instance.post_account_recover_code(code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_recover_code: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.mangadex.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**get_account_activate_code**](docs/AccountApi.md#get_account_activate_code) | **GET** /account/activate/{code} | Activate account
*AccountApi* | [**post_account_activate_resend**](docs/AccountApi.md#post_account_activate_resend) | **POST** /account/activate/resend | Resend Activation code
*AccountApi* | [**post_account_create**](docs/AccountApi.md#post_account_create) | **POST** /account/create | Create Account
*AccountApi* | [**post_account_recover**](docs/AccountApi.md#post_account_recover) | **POST** /account/recover | Recover given Account
*AccountApi* | [**post_account_recover_code**](docs/AccountApi.md#post_account_recover_code) | **POST** /account/recover/{code} | Complete Account recover
*AtHomeApi* | [**get_at_home_server_chapter_id**](docs/AtHomeApi.md#get_at_home_server_chapter_id) | **GET** /at-home/server/{chapterId} | Get MangaDex@Home server URL
*AuthApi* | [**get_auth_check**](docs/AuthApi.md#get_auth_check) | **GET** /auth/check | Check token
*AuthApi* | [**post_auth_login**](docs/AuthApi.md#post_auth_login) | **POST** /auth/login | Login
*AuthApi* | [**post_auth_logout**](docs/AuthApi.md#post_auth_logout) | **POST** /auth/logout | Logout
*AuthApi* | [**post_auth_refresh**](docs/AuthApi.md#post_auth_refresh) | **POST** /auth/refresh | Refresh token
*AuthorApi* | [**delete_author_id**](docs/AuthorApi.md#delete_author_id) | **DELETE** /author/{id} | Delete Author
*AuthorApi* | [**get_author**](docs/AuthorApi.md#get_author) | **GET** /author | Author list
*AuthorApi* | [**get_author_id**](docs/AuthorApi.md#get_author_id) | **GET** /author/{id} | Get Author
*AuthorApi* | [**post_author**](docs/AuthorApi.md#post_author) | **POST** /author | Create Author
*AuthorApi* | [**put_author_id**](docs/AuthorApi.md#put_author_id) | **PUT** /author/{id} | Update Author
*CaptchaApi* | [**post_captcha_solve**](docs/CaptchaApi.md#post_captcha_solve) | **POST** /captcha/solve | Solve Captcha
*ChapterApi* | [**chapter_id_read**](docs/ChapterApi.md#chapter_id_read) | **POST** /chapter/{id}/read | Mark Chapter read
*ChapterApi* | [**chapter_id_unread**](docs/ChapterApi.md#chapter_id_unread) | **DELETE** /chapter/{id}/read | Mark Chapter unread
*ChapterApi* | [**delete_chapter_id**](docs/ChapterApi.md#delete_chapter_id) | **DELETE** /chapter/{id} | Delete Chapter
*ChapterApi* | [**get_chapter**](docs/ChapterApi.md#get_chapter) | **GET** /chapter | Chapter list
*ChapterApi* | [**get_chapter_id**](docs/ChapterApi.md#get_chapter_id) | **GET** /chapter/{id} | Get Chapter
*ChapterApi* | [**put_chapter_id**](docs/ChapterApi.md#put_chapter_id) | **PUT** /chapter/{id} | Update Chapter
*CoverApi* | [**delete_cover**](docs/CoverApi.md#delete_cover) | **DELETE** /cover/{coverId} | Delete Cover
*CoverApi* | [**edit_cover**](docs/CoverApi.md#edit_cover) | **PUT** /cover/{coverId} | Edit Cover
*CoverApi* | [**get_cover**](docs/CoverApi.md#get_cover) | **GET** /cover | CoverArt list
*CoverApi* | [**get_cover_0**](docs/CoverApi.md#get_cover_0) | **GET** /cover/{coverId} | Get Cover
*CoverApi* | [**upload_cover**](docs/CoverApi.md#upload_cover) | **POST** /cover/{mangaId} | Upload Cover
*CustomListApi* | [**delete_list_id**](docs/CustomListApi.md#delete_list_id) | **DELETE** /list/{id} | Delete CustomList
*CustomListApi* | [**delete_manga_id_list_list_id**](docs/CustomListApi.md#delete_manga_id_list_list_id) | **DELETE** /manga/{id}/list/{listId} | Remove Manga in CustomList
*CustomListApi* | [**get_list_id**](docs/CustomListApi.md#get_list_id) | **GET** /list/{id} | Get CustomList
*CustomListApi* | [**get_list_id_feed**](docs/CustomListApi.md#get_list_id_feed) | **GET** /list/{id}/feed | CustomList Manga feed
*CustomListApi* | [**get_user_id_list**](docs/CustomListApi.md#get_user_id_list) | **GET** /user/{id}/list | Get User&#x27;s CustomList list
*CustomListApi* | [**get_user_list**](docs/CustomListApi.md#get_user_list) | **GET** /user/list | Get logged User CustomList list
*CustomListApi* | [**post_list**](docs/CustomListApi.md#post_list) | **POST** /list | Create CustomList
*CustomListApi* | [**post_manga_id_list_list_id**](docs/CustomListApi.md#post_manga_id_list_list_id) | **POST** /manga/{id}/list/{listId} | Add Manga in CustomList
*CustomListApi* | [**put_list_id**](docs/CustomListApi.md#put_list_id) | **PUT** /list/{id} | Update CustomList
*FeedApi* | [**get_list_id_feed**](docs/FeedApi.md#get_list_id_feed) | **GET** /list/{id}/feed | CustomList Manga feed
*FeedApi* | [**get_user_follows_manga_feed**](docs/FeedApi.md#get_user_follows_manga_feed) | **GET** /user/follows/manga/feed | Get logged User followed Manga feed
*InfrastructureApi* | [**ping_get**](docs/InfrastructureApi.md#ping_get) | **GET** /ping | Ping the server
*LegacyApi* | [**post_legacy_mapping**](docs/LegacyApi.md#post_legacy_mapping) | **POST** /legacy/mapping | Legacy ID mapping
*MangaApi* | [**delete_manga_id**](docs/MangaApi.md#delete_manga_id) | **DELETE** /manga/{id} | Delete Manga
*MangaApi* | [**delete_manga_id_follow**](docs/MangaApi.md#delete_manga_id_follow) | **DELETE** /manga/{id}/follow | Unfollow Manga
*MangaApi* | [**delete_manga_id_list_list_id**](docs/MangaApi.md#delete_manga_id_list_list_id) | **DELETE** /manga/{id}/list/{listId} | Remove Manga in CustomList
*MangaApi* | [**get_manga_chapter_readmarkers**](docs/MangaApi.md#get_manga_chapter_readmarkers) | **GET** /manga/{id}/read | Manga read markers
*MangaApi* | [**get_manga_chapter_readmarkers2**](docs/MangaApi.md#get_manga_chapter_readmarkers2) | **GET** /manga/read | Manga read markers
*MangaApi* | [**get_manga_id**](docs/MangaApi.md#get_manga_id) | **GET** /manga/{id} | View Manga
*MangaApi* | [**get_manga_id_feed**](docs/MangaApi.md#get_manga_id_feed) | **GET** /manga/{id}/feed | Manga feed
*MangaApi* | [**get_manga_id_status**](docs/MangaApi.md#get_manga_id_status) | **GET** /manga/{id}/status | Get a Manga reading status
*MangaApi* | [**get_manga_random**](docs/MangaApi.md#get_manga_random) | **GET** /manga/random | Get a random Manga
*MangaApi* | [**get_manga_status**](docs/MangaApi.md#get_manga_status) | **GET** /manga/status | Get all Manga reading status for logged User
*MangaApi* | [**get_manga_tag**](docs/MangaApi.md#get_manga_tag) | **GET** /manga/tag | Tag list
*MangaApi* | [**get_search_manga**](docs/MangaApi.md#get_search_manga) | **GET** /manga | Manga list
*MangaApi* | [**get_user_follows_manga**](docs/MangaApi.md#get_user_follows_manga) | **GET** /user/follows/manga | Get logged User followed Manga list
*MangaApi* | [**get_user_follows_manga_feed**](docs/MangaApi.md#get_user_follows_manga_feed) | **GET** /user/follows/manga/feed | Get logged User followed Manga feed
*MangaApi* | [**manga_id_aggregate_get**](docs/MangaApi.md#manga_id_aggregate_get) | **GET** /manga/{id}/aggregate | Get Manga volumes &amp; chapters
*MangaApi* | [**post_manga**](docs/MangaApi.md#post_manga) | **POST** /manga | Create Manga
*MangaApi* | [**post_manga_id_follow**](docs/MangaApi.md#post_manga_id_follow) | **POST** /manga/{id}/follow | Follow Manga
*MangaApi* | [**post_manga_id_list_list_id**](docs/MangaApi.md#post_manga_id_list_list_id) | **POST** /manga/{id}/list/{listId} | Add Manga in CustomList
*MangaApi* | [**post_manga_id_status**](docs/MangaApi.md#post_manga_id_status) | **POST** /manga/{id}/status | Update Manga reading status
*MangaApi* | [**put_manga_id**](docs/MangaApi.md#put_manga_id) | **PUT** /manga/{id} | Update Manga
*ScanlationGroupApi* | [**delete_group_id**](docs/ScanlationGroupApi.md#delete_group_id) | **DELETE** /group/{id} | Delete Scanlation Group
*ScanlationGroupApi* | [**delete_group_id_follow**](docs/ScanlationGroupApi.md#delete_group_id_follow) | **DELETE** /group/{id}/follow | Unfollow Scanlation Group
*ScanlationGroupApi* | [**get_group_id**](docs/ScanlationGroupApi.md#get_group_id) | **GET** /group/{id} | View Scanlation Group
*ScanlationGroupApi* | [**get_search_group**](docs/ScanlationGroupApi.md#get_search_group) | **GET** /group | Scanlation Group list
*ScanlationGroupApi* | [**get_user_follows_group**](docs/ScanlationGroupApi.md#get_user_follows_group) | **GET** /user/follows/group | Get logged User followed Groups
*ScanlationGroupApi* | [**post_group**](docs/ScanlationGroupApi.md#post_group) | **POST** /group | Create Scanlation Group
*ScanlationGroupApi* | [**post_group_id_follow**](docs/ScanlationGroupApi.md#post_group_id_follow) | **POST** /group/{id}/follow | Follow Scanlation Group
*ScanlationGroupApi* | [**put_group_id**](docs/ScanlationGroupApi.md#put_group_id) | **PUT** /group/{id} | Update Scanlation Group
*SearchApi* | [**get_author**](docs/SearchApi.md#get_author) | **GET** /author | Author list
*SearchApi* | [**get_chapter**](docs/SearchApi.md#get_chapter) | **GET** /chapter | Chapter list
*SearchApi* | [**get_cover**](docs/SearchApi.md#get_cover) | **GET** /cover | CoverArt list
*SearchApi* | [**get_search_group**](docs/SearchApi.md#get_search_group) | **GET** /group | Scanlation Group list
*SearchApi* | [**get_search_manga**](docs/SearchApi.md#get_search_manga) | **GET** /manga | Manga list
*UploadApi* | [**upload_cover**](docs/UploadApi.md#upload_cover) | **POST** /cover/{mangaId} | Upload Cover
*UserApi* | [**get_user_follows_group**](docs/UserApi.md#get_user_follows_group) | **GET** /user/follows/group | Get logged User followed Groups
*UserApi* | [**get_user_follows_manga**](docs/UserApi.md#get_user_follows_manga) | **GET** /user/follows/manga | Get logged User followed Manga list
*UserApi* | [**get_user_follows_user**](docs/UserApi.md#get_user_follows_user) | **GET** /user/follows/user | Get logged User followed User list
*UserApi* | [**get_user_id**](docs/UserApi.md#get_user_id) | **GET** /user/{id} | Get User
*UserApi* | [**get_user_me**](docs/UserApi.md#get_user_me) | **GET** /user/me | Logged User details

## Documentation For Models

 - [AccountActivateResponse](docs/AccountActivateResponse.md)
 - [Author](docs/Author.md)
 - [AuthorAttributes](docs/AuthorAttributes.md)
 - [AuthorCreate](docs/AuthorCreate.md)
 - [AuthorEdit](docs/AuthorEdit.md)
 - [AuthorList](docs/AuthorList.md)
 - [AuthorResponse](docs/AuthorResponse.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Chapter](docs/Chapter.md)
 - [ChapterAttributes](docs/ChapterAttributes.md)
 - [ChapterEdit](docs/ChapterEdit.md)
 - [ChapterList](docs/ChapterList.md)
 - [ChapterRequest](docs/ChapterRequest.md)
 - [ChapterResponse](docs/ChapterResponse.md)
 - [CheckResponse](docs/CheckResponse.md)
 - [Cover](docs/Cover.md)
 - [CoverAttributes](docs/CoverAttributes.md)
 - [CoverEdit](docs/CoverEdit.md)
 - [CoverList](docs/CoverList.md)
 - [CoverResponse](docs/CoverResponse.md)
 - [CreateAccount](docs/CreateAccount.md)
 - [CreateScanlationGroup](docs/CreateScanlationGroup.md)
 - [CustomList](docs/CustomList.md)
 - [CustomListAttributes](docs/CustomListAttributes.md)
 - [CustomListCreate](docs/CustomListCreate.md)
 - [CustomListEdit](docs/CustomListEdit.md)
 - [CustomListList](docs/CustomListList.md)
 - [CustomListResponse](docs/CustomListResponse.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse200Chapters](docs/InlineResponse200Chapters.md)
 - [InlineResponse200Volumes](docs/InlineResponse200Volumes.md)
 - [LocalizedString](docs/LocalizedString.md)
 - [Login](docs/Login.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [LoginResponseToken](docs/LoginResponseToken.md)
 - [LogoutResponse](docs/LogoutResponse.md)
 - [Manga](docs/Manga.md)
 - [MangaAttributes](docs/MangaAttributes.md)
 - [MangaCreate](docs/MangaCreate.md)
 - [MangaEdit](docs/MangaEdit.md)
 - [MangaList](docs/MangaList.md)
 - [MangaRequest](docs/MangaRequest.md)
 - [MangaResponse](docs/MangaResponse.md)
 - [MappingId](docs/MappingId.md)
 - [MappingIdAttributes](docs/MappingIdAttributes.md)
 - [MappingIdBody](docs/MappingIdBody.md)
 - [MappingIdResponse](docs/MappingIdResponse.md)
 - [Order](docs/Order.md)
 - [Order1](docs/Order1.md)
 - [Order2](docs/Order2.md)
 - [Order3](docs/Order3.md)
 - [Order4](docs/Order4.md)
 - [Order5](docs/Order5.md)
 - [Order6](docs/Order6.md)
 - [RecoverCompleteBody](docs/RecoverCompleteBody.md)
 - [RefreshResponse](docs/RefreshResponse.md)
 - [RefreshToken](docs/RefreshToken.md)
 - [Relationship](docs/Relationship.md)
 - [Response](docs/Response.md)
 - [ScanlationGroup](docs/ScanlationGroup.md)
 - [ScanlationGroupAttributes](docs/ScanlationGroupAttributes.md)
 - [ScanlationGroupEdit](docs/ScanlationGroupEdit.md)
 - [ScanlationGroupList](docs/ScanlationGroupList.md)
 - [ScanlationGroupResponse](docs/ScanlationGroupResponse.md)
 - [ScanlationGroupResponseRelationships](docs/ScanlationGroupResponseRelationships.md)
 - [SendAccountActivationCode](docs/SendAccountActivationCode.md)
 - [Tag](docs/Tag.md)
 - [TagAttributes](docs/TagAttributes.md)
 - [TagResponse](docs/TagResponse.md)
 - [UpdateMangaStatus](docs/UpdateMangaStatus.md)
 - [User](docs/User.md)
 - [UserAttributes](docs/UserAttributes.md)
 - [UserList](docs/UserList.md)
 - [UserResponse](docs/UserResponse.md)

## Documentation For Authorization


## Bearer



## Author

mangadexstaff@gmail.com
