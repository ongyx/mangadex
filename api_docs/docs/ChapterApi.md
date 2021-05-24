# mangadex_openapi.ChapterApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chapter_id_read**](ChapterApi.md#chapter_id_read) | **POST** /chapter/{id}/read | Mark Chapter read
[**chapter_id_unread**](ChapterApi.md#chapter_id_unread) | **DELETE** /chapter/{id}/read | Mark Chapter unread
[**delete_chapter_id**](ChapterApi.md#delete_chapter_id) | **DELETE** /chapter/{id} | Delete Chapter
[**get_chapter**](ChapterApi.md#get_chapter) | **GET** /chapter | Chapter list
[**get_chapter_id**](ChapterApi.md#get_chapter_id) | **GET** /chapter/{id} | Get Chapter
[**put_chapter_id**](ChapterApi.md#put_chapter_id) | **PUT** /chapter/{id} | Update Chapter

# **chapter_id_read**
> InlineResponse2002 chapter_id_read(id)

Mark Chapter read

Mark chapter as read for the current user

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ChapterApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Mark Chapter read
    api_response = api_instance.chapter_id_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapterApi->chapter_id_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chapter_id_unread**
> InlineResponse2002 chapter_id_unread(id)

Mark Chapter unread

Mark chapter as unread for the current user

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ChapterApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Mark Chapter unread
    api_response = api_instance.chapter_id_unread(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapterApi->chapter_id_unread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chapter_id**
> Response delete_chapter_id(id)

Delete Chapter

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ChapterApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Chapter ID

try:
    # Delete Chapter
    api_response = api_instance.delete_chapter_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapterApi->delete_chapter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Chapter ID | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

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
api_instance = mangadex_openapi.ChapterApi()
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
    print("Exception when calling ChapterApi->get_chapter: %s\n" % e)
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

# **get_chapter_id**
> ChapterResponse get_chapter_id(id)

Get Chapter

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.ChapterApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Chapter ID

try:
    # Get Chapter
    api_response = api_instance.get_chapter_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapterApi->get_chapter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Chapter ID | 

### Return type

[**ChapterResponse**](ChapterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_chapter_id**
> ChapterResponse put_chapter_id(id, body=body)

Update Chapter

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ChapterApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Chapter ID
body = mangadex_openapi.ChapterEdit() # ChapterEdit | The size of the body is limited to 32KB. (optional)

try:
    # Update Chapter
    api_response = api_instance.put_chapter_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChapterApi->put_chapter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Chapter ID | 
 **body** | [**ChapterEdit**](ChapterEdit.md)| The size of the body is limited to 32KB. | [optional] 

### Return type

[**ChapterResponse**](ChapterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

