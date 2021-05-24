# mangadex_openapi.FeedApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_id_feed**](FeedApi.md#get_list_id_feed) | **GET** /list/{id}/feed | CustomList Manga feed
[**get_user_follows_manga_feed**](FeedApi.md#get_user_follows_manga_feed) | **GET** /user/follows/manga/feed | Get logged User followed Manga feed

# **get_list_id_feed**
> ChapterList get_list_id_feed(id, limit=limit, offset=offset, translated_language=translated_language, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)

CustomList Manga feed

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.FeedApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
limit = 100 # int |  (optional) (default to 100)
offset = 56 # int |  (optional)
translated_language = ['translated_language_example'] # list[str] |  (optional)
created_at_since = 'created_at_since_example' # str |  (optional)
updated_at_since = 'updated_at_since_example' # str |  (optional)
publish_at_since = 'publish_at_since_example' # str |  (optional)
order = mangadex_openapi.Order3() # Order3 |  (optional)

try:
    # CustomList Manga feed
    api_response = api_instance.get_list_id_feed(id, limit=limit, offset=offset, translated_language=translated_language, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedApi->get_list_id_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **translated_language** | [**list[str]**](str.md)|  | [optional] 
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**Order3**](.md)|  | [optional] 

### Return type

[**ChapterList**](ChapterList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_manga_feed**
> ChapterList get_user_follows_manga_feed(limit=limit, offset=offset, translated_language=translated_language, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)

Get logged User followed Manga feed

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.FeedApi(mangadex_openapi.ApiClient(configuration))
limit = 100 # int |  (optional) (default to 100)
offset = 56 # int |  (optional)
translated_language = ['translated_language_example'] # list[str] |  (optional)
created_at_since = 'created_at_since_example' # str |  (optional)
updated_at_since = 'updated_at_since_example' # str |  (optional)
publish_at_since = 'publish_at_since_example' # str |  (optional)
order = mangadex_openapi.Order2() # Order2 |  (optional)

try:
    # Get logged User followed Manga feed
    api_response = api_instance.get_user_follows_manga_feed(limit=limit, offset=offset, translated_language=translated_language, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedApi->get_user_follows_manga_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **translated_language** | [**list[str]**](str.md)|  | [optional] 
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

