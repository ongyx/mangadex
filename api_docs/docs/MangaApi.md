# mangadex.MangaApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_manga_id**](MangaApi.md#delete_manga_id) | **DELETE** /manga/{id} | Delete Manga
[**delete_manga_id_follow**](MangaApi.md#delete_manga_id_follow) | **DELETE** /manga/{id}/follow | Unfollow Manga
[**delete_manga_id_list_list_id**](MangaApi.md#delete_manga_id_list_list_id) | **DELETE** /manga/{id}/list/{listId} | Remove Manga in CustomList
[**get_manga_chapter_readmarkers**](MangaApi.md#get_manga_chapter_readmarkers) | **GET** /manga/{id}/read | Manga read markers
[**get_manga_chapter_readmarkers_0**](MangaApi.md#get_manga_chapter_readmarkers_0) | **GET** /manga/read | Manga read markers
[**get_manga_id**](MangaApi.md#get_manga_id) | **GET** /manga/{id} | View Manga
[**get_manga_id_feed**](MangaApi.md#get_manga_id_feed) | **GET** /manga/{id}/feed | Manga feed
[**get_manga_id_status**](MangaApi.md#get_manga_id_status) | **GET** /manga/{id}/status | Get a Manga reading status
[**get_manga_random**](MangaApi.md#get_manga_random) | **GET** /manga/random | Get a random Manga
[**get_manga_status**](MangaApi.md#get_manga_status) | **GET** /manga/status | Get all Manga reading status for logged User
[**get_manga_tag**](MangaApi.md#get_manga_tag) | **GET** /manga/tag | Tag list
[**get_search_manga**](MangaApi.md#get_search_manga) | **GET** /manga | Manga list
[**get_user_follows_manga**](MangaApi.md#get_user_follows_manga) | **GET** /user/follows/manga | Get logged User followed Manga list
[**get_user_follows_manga_feed**](MangaApi.md#get_user_follows_manga_feed) | **GET** /user/follows/manga/feed | Get logged User followed Manga feed
[**post_manga**](MangaApi.md#post_manga) | **POST** /manga | Create Manga
[**post_manga_id_follow**](MangaApi.md#post_manga_id_follow) | **POST** /manga/{id}/follow | Follow Manga
[**post_manga_id_list_list_id**](MangaApi.md#post_manga_id_list_list_id) | **POST** /manga/{id}/list/{listId} | Add Manga in CustomList
[**post_manga_id_status**](MangaApi.md#post_manga_id_status) | **POST** /manga/{id}/status | Update Manga reading status
[**put_manga_id**](MangaApi.md#put_manga_id) | **PUT** /manga/{id} | Update Manga

# **delete_manga_id**
> Response delete_manga_id(id)

Delete Manga

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID

try:
    # Delete Manga
    api_response = api_instance.delete_manga_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->delete_manga_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Manga ID | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manga_id_follow**
> Response delete_manga_id_follow(id)

Unfollow Manga

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Unfollow Manga
    api_response = api_instance.delete_manga_id_follow(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->delete_manga_id_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manga_id_list_list_id**
> Response delete_manga_id_list_list_id(id, list_id)

Remove Manga in CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID
list_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID

try:
    # Remove Manga in CustomList
    api_response = api_instance.delete_manga_id_list_list_id(id, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->delete_manga_id_list_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Manga ID | 
 **list_id** | [**str**](.md)| CustomList ID | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_chapter_readmarkers**
> InlineResponse200 get_manga_chapter_readmarkers(id)

Manga read markers

A list of chapter ids that are marked as read for the specified manga

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Manga read markers
    api_response = api_instance.get_manga_chapter_readmarkers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_chapter_readmarkers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_chapter_readmarkers_0**
> InlineResponse200 get_manga_chapter_readmarkers_0(ids)

Manga read markers

A list of chapter ids that are marked as read for the given manga ids

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
ids = ['ids_example'] # list[str] | Manga ids

try:
    # Manga read markers
    api_response = api_instance.get_manga_chapter_readmarkers_0(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_chapter_readmarkers_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| Manga ids | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id**
> MangaResponse get_manga_id(id)

View Manga

View Manga.

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex.MangaApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID

try:
    # View Manga
    api_response = api_instance.get_manga_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Manga ID | 

### Return type

[**MangaResponse**](MangaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id_feed**
> ChapterList get_manga_id_feed(id, limit=limit, offset=offset, locales=locales, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)

Manga feed

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex.MangaApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID
limit = 100 # int |  (optional) (default to 100)
offset = 56 # int |  (optional)
locales = ['locales_example'] # list[str] |  (optional)
created_at_since = 'created_at_since_example' # str |  (optional)
updated_at_since = 'updated_at_since_example' # str |  (optional)
publish_at_since = 'publish_at_since_example' # str |  (optional)
order = mangadex.Order5() # Order5 |  (optional)

try:
    # Manga feed
    api_response = api_instance.get_manga_id_feed(id, limit=limit, offset=offset, locales=locales, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_id_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Manga ID | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **locales** | [**list[str]**](str.md)|  | [optional] 
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**Order5**](.md)|  | [optional] 

### Return type

[**ChapterList**](ChapterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id_status**
> InlineResponse2004 get_manga_id_status(id)

Get a Manga reading status

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get a Manga reading status
    api_response = api_instance.get_manga_id_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_id_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_random**
> MangaResponse get_manga_random()

Get a random Manga

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex.MangaApi()

try:
    # Get a random Manga
    api_response = api_instance.get_manga_random()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_random: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MangaResponse**](MangaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_status**
> InlineResponse2003 get_manga_status(status=status)

Get all Manga reading status for logged User

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
status = 'status_example' # str | Used to filter the list by given status (optional)

try:
    # Get all Manga reading status for logged User
    api_response = api_instance.get_manga_status(status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Used to filter the list by given status | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_tag**
> list[TagResponse] get_manga_tag()

Tag list

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex.MangaApi()

try:
    # Tag list
    api_response = api_instance.get_manga_tag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_manga_tag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_manga**
> MangaList get_search_manga(limit=limit, offset=offset, title=title, authors=authors, artists=artists, year=year, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode, status=status, original_language=original_language, publication_demographic=publication_demographic, ids=ids, content_rating=content_rating, created_at_since=created_at_since, updated_at_since=updated_at_since, order=order)

Manga list

Search a list of Manga.

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex.MangaApi()
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)
title = 'title_example' # str |  (optional)
authors = ['authors_example'] # list[str] |  (optional)
artists = ['artists_example'] # list[str] |  (optional)
year = 56 # int |  (optional)
included_tags = ['included_tags_example'] # list[str] |  (optional)
included_tags_mode = 'AND' # str |  (optional) (default to AND)
excluded_tags = ['excluded_tags_example'] # list[str] |  (optional)
excluded_tags_mode = 'OR' # str |  (optional) (default to OR)
status = ['status_example'] # list[str] |  (optional)
original_language = ['original_language_example'] # list[str] |  (optional)
publication_demographic = ['publication_demographic_example'] # list[str] |  (optional)
ids = ['ids_example'] # list[str] | Manga ids (limited to 100 per request) (optional)
content_rating = ['content_rating_example'] # list[str] |  (optional)
created_at_since = 'created_at_since_example' # str |  (optional)
updated_at_since = 'updated_at_since_example' # str |  (optional)
order = mangadex.Order() # Order |  (optional)

try:
    # Manga list
    api_response = api_instance.get_search_manga(limit=limit, offset=offset, title=title, authors=authors, artists=artists, year=year, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode, status=status, original_language=original_language, publication_demographic=publication_demographic, ids=ids, content_rating=content_rating, created_at_since=created_at_since, updated_at_since=updated_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_search_manga: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **title** | **str**|  | [optional] 
 **authors** | [**list[str]**](str.md)|  | [optional] 
 **artists** | [**list[str]**](str.md)|  | [optional] 
 **year** | **int**|  | [optional] 
 **included_tags** | [**list[str]**](str.md)|  | [optional] 
 **included_tags_mode** | **str**|  | [optional] [default to AND]
 **excluded_tags** | [**list[str]**](str.md)|  | [optional] 
 **excluded_tags_mode** | **str**|  | [optional] [default to OR]
 **status** | [**list[str]**](str.md)|  | [optional] 
 **original_language** | [**list[str]**](str.md)|  | [optional] 
 **publication_demographic** | [**list[str]**](str.md)|  | [optional] 
 **ids** | [**list[str]**](str.md)| Manga ids (limited to 100 per request) | [optional] 
 **content_rating** | [**list[str]**](str.md)|  | [optional] 
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **order** | [**Order**](.md)|  | [optional] 

### Return type

[**MangaList**](MangaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_manga**
> MangaList get_user_follows_manga(limit=limit, offset=offset)

Get logged User followed Manga list

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get logged User followed Manga list
    api_response = api_instance.get_user_follows_manga(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_user_follows_manga: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**MangaList**](MangaList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_manga_feed**
> ChapterList get_user_follows_manga_feed(limit=limit, offset=offset, locales=locales, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)

Get logged User followed Manga feed

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
limit = 100 # int |  (optional) (default to 100)
offset = 56 # int |  (optional)
locales = ['locales_example'] # list[str] |  (optional)
created_at_since = 'created_at_since_example' # str |  (optional)
updated_at_since = 'updated_at_since_example' # str |  (optional)
publish_at_since = 'publish_at_since_example' # str |  (optional)
order = mangadex.Order2() # Order2 |  (optional)

try:
    # Get logged User followed Manga feed
    api_response = api_instance.get_user_follows_manga_feed(limit=limit, offset=offset, locales=locales, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->get_user_follows_manga_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **locales** | [**list[str]**](str.md)|  | [optional] 
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**Order2**](.md)|  | [optional] 

### Return type

[**ChapterList**](ChapterList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga**
> MangaResponse post_manga(body=body)

Create Manga

Create a new Manga.

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
body = mangadex.MangaCreate() # MangaCreate | The size of the body is limited to 16KB. (optional)

try:
    # Create Manga
    api_response = api_instance.post_manga(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->post_manga: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MangaCreate**](MangaCreate.md)| The size of the body is limited to 16KB. | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_follow**
> Response post_manga_id_follow(id)

Follow Manga

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Follow Manga
    api_response = api_instance.post_manga_id_follow(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->post_manga_id_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_list_list_id**
> Response post_manga_id_list_list_id(id, list_id)

Add Manga in CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID
list_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID

try:
    # Add Manga in CustomList
    api_response = api_instance.post_manga_id_list_list_id(id, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->post_manga_id_list_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Manga ID | 
 **list_id** | [**str**](.md)| CustomList ID | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_status**
> Response post_manga_id_status(id, body=body)

Update Manga reading status

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = mangadex.UpdateMangaStatus() # UpdateMangaStatus | Using a `null` value in `status` field will remove the Manga reading status. The size of the body is limited to 2KB. (optional)

try:
    # Update Manga reading status
    api_response = api_instance.post_manga_id_status(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->post_manga_id_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **body** | [**UpdateMangaStatus**](UpdateMangaStatus.md)| Using a &#x60;null&#x60; value in &#x60;status&#x60; field will remove the Manga reading status. The size of the body is limited to 2KB. | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_manga_id**
> MangaResponse put_manga_id(id, body=body)

Update Manga

### Example
```python
from __future__ import print_function
import time
import mangadex
from mangadex.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex.MangaApi(mangadex.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID
body = mangadex.MangaEdit() # MangaEdit | The size of the body is limited to 16KB. (optional)

try:
    # Update Manga
    api_response = api_instance.put_manga_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MangaApi->put_manga_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Manga ID | 
 **body** | [**MangaEdit**](MangaEdit.md)| The size of the body is limited to 16KB. | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

