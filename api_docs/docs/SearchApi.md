# mangadex_openapi.SearchApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_author**](SearchApi.md#get_author) | **GET** /author | Author list
[**get_chapter**](SearchApi.md#get_chapter) | **GET** /chapter | Chapter list
[**get_cover**](SearchApi.md#get_cover) | **GET** /cover | CoverArt list
[**get_search_group**](SearchApi.md#get_search_group) | **GET** /group | Scanlation Group list
[**get_search_manga**](SearchApi.md#get_search_manga) | **GET** /manga | Manga list

# **get_author**
> AuthorList get_author(limit=limit, offset=offset, ids=ids, name=name, order=order)

Author list

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.SearchApi()
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)
ids = ['ids_example'] # list[str] | Author ids (limited to 100 per request) (optional)
name = 'name_example' # str |  (optional)
order = mangadex_openapi.Order5() # Order5 |  (optional)

try:
    # Author list
    api_response = api_instance.get_author(limit=limit, offset=offset, ids=ids, name=name, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_author: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**list[str]**](str.md)| Author ids (limited to 100 per request) | [optional] 
 **name** | **str**|  | [optional] 
 **order** | [**Order5**](.md)|  | [optional] 

### Return type

[**AuthorList**](AuthorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chapter**
> ChapterList get_chapter(limit=limit, offset=offset, ids=ids, title=title, groups=groups, uploader=uploader, manga=manga, volume=volume, chapter=chapter, translated_language=translated_language, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)

Chapter list

Chapter list. If you want the Chapters of a given Manga, please check the feed endpoints.

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.SearchApi()
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)
ids = ['ids_example'] # list[str] | Chapter ids (limited to 100 per request) (optional)
title = 'title_example' # str |  (optional)
groups = ['groups_example'] # list[str] |  (optional)
uploader = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
manga = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
volume = 'volume_example' # str |  (optional)
chapter = 'chapter_example' # str |  (optional)
translated_language = ['translated_language_example'] # list[str] |  (optional)
created_at_since = 'created_at_since_example' # str |  (optional)
updated_at_since = 'updated_at_since_example' # str |  (optional)
publish_at_since = 'publish_at_since_example' # str |  (optional)
order = mangadex_openapi.Order1() # Order1 |  (optional)

try:
    # Chapter list
    api_response = api_instance.get_chapter(limit=limit, offset=offset, ids=ids, title=title, groups=groups, uploader=uploader, manga=manga, volume=volume, chapter=chapter, translated_language=translated_language, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_chapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**list[str]**](str.md)| Chapter ids (limited to 100 per request) | [optional] 
 **title** | **str**|  | [optional] 
 **groups** | [**list[str]**](str.md)|  | [optional] 
 **uploader** | [**str**](.md)|  | [optional] 
 **manga** | [**str**](.md)|  | [optional] 
 **volume** | **str**|  | [optional] 
 **chapter** | **str**|  | [optional] 
 **translated_language** | [**list[str]**](str.md)|  | [optional] 
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**Order1**](.md)|  | [optional] 

### Return type

[**ChapterList**](ChapterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cover**
> CoverList get_cover(limit=limit, offset=offset, manga=manga, ids=ids, uploaders=uploaders, order=order)

CoverArt list

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.SearchApi()
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)
manga = ['manga_example'] # list[str] | Manga ids (limited to 100 per request) (optional)
ids = ['ids_example'] # list[str] | Covers ids (limited to 100 per request) (optional)
uploaders = ['uploaders_example'] # list[str] | User ids (limited to 100 per request) (optional)
order = mangadex_openapi.Order4() # Order4 |  (optional)

try:
    # CoverArt list
    api_response = api_instance.get_cover(limit=limit, offset=offset, manga=manga, ids=ids, uploaders=uploaders, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **manga** | [**list[str]**](str.md)| Manga ids (limited to 100 per request) | [optional] 
 **ids** | [**list[str]**](str.md)| Covers ids (limited to 100 per request) | [optional] 
 **uploaders** | [**list[str]**](str.md)| User ids (limited to 100 per request) | [optional] 
 **order** | [**Order4**](.md)|  | [optional] 

### Return type

[**CoverList**](CoverList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_group**
> ScanlationGroupList get_search_group(limit=limit, offset=offset, ids=ids, name=name)

Scanlation Group list

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.SearchApi()
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)
ids = ['ids_example'] # list[str] | ScanlationGroup ids (limited to 100 per request) (optional)
name = 'name_example' # str |  (optional)

try:
    # Scanlation Group list
    api_response = api_instance.get_search_group(limit=limit, offset=offset, ids=ids, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**list[str]**](str.md)| ScanlationGroup ids (limited to 100 per request) | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**ScanlationGroupList**](ScanlationGroupList.md)

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
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.SearchApi()
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
order = mangadex_openapi.Order() # Order |  (optional)

try:
    # Manga list
    api_response = api_instance.get_search_manga(limit=limit, offset=offset, title=title, authors=authors, artists=artists, year=year, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode, status=status, original_language=original_language, publication_demographic=publication_demographic, ids=ids, content_rating=content_rating, created_at_since=created_at_since, updated_at_since=updated_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_manga: %s\n" % e)
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

