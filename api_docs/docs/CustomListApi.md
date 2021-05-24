# mangadex_openapi.CustomListApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_list_id**](CustomListApi.md#delete_list_id) | **DELETE** /list/{id} | Delete CustomList
[**delete_manga_id_list_list_id**](CustomListApi.md#delete_manga_id_list_list_id) | **DELETE** /manga/{id}/list/{listId} | Remove Manga in CustomList
[**get_list_id**](CustomListApi.md#get_list_id) | **GET** /list/{id} | Get CustomList
[**get_list_id_feed**](CustomListApi.md#get_list_id_feed) | **GET** /list/{id}/feed | CustomList Manga feed
[**get_user_id_list**](CustomListApi.md#get_user_id_list) | **GET** /user/{id}/list | Get User&#x27;s CustomList list
[**get_user_list**](CustomListApi.md#get_user_list) | **GET** /user/list | Get logged User CustomList list
[**post_list**](CustomListApi.md#post_list) | **POST** /list | Create CustomList
[**post_manga_id_list_list_id**](CustomListApi.md#post_manga_id_list_list_id) | **POST** /manga/{id}/list/{listId} | Add Manga in CustomList
[**put_list_id**](CustomListApi.md#put_list_id) | **PUT** /list/{id} | Update CustomList

# **delete_list_id**
> Response delete_list_id(id)

Delete CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID

try:
    # Delete CustomList
    api_response = api_instance.delete_list_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->delete_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| CustomList ID | 

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
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID
list_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID

try:
    # Remove Manga in CustomList
    api_response = api_instance.delete_manga_id_list_list_id(id, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->delete_manga_id_list_list_id: %s\n" % e)
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

# **get_list_id**
> CustomListResponse get_list_id(id)

Get CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID

try:
    # Get CustomList
    api_response = api_instance.get_list_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->get_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| CustomList ID | 

### Return type

[**CustomListResponse**](CustomListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
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
    print("Exception when calling CustomListApi->get_list_id_feed: %s\n" % e)
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

# **get_user_id_list**
> CustomListList get_user_id_list(id, limit=limit, offset=offset)

Get User's CustomList list

This will list only public CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get User's CustomList list
    api_response = api_instance.get_user_id_list(id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->get_user_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| User ID | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**CustomListList**](CustomListList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_list**
> CustomListList get_user_list(limit=limit, offset=offset)

Get logged User CustomList list

This will list public and private CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get logged User CustomList list
    api_response = api_instance.get_user_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->get_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**CustomListList**](CustomListList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_list**
> CustomListResponse post_list(body=body)

Create CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
body = mangadex_openapi.CustomListCreate() # CustomListCreate | The size of the body is limited to 8KB. (optional)

try:
    # Create CustomList
    api_response = api_instance.post_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->post_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomListCreate**](CustomListCreate.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**CustomListResponse**](CustomListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_list_list_id**
> Response post_manga_id_list_list_id(id, list_id)

Add Manga in CustomList

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Manga ID
list_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID

try:
    # Add Manga in CustomList
    api_response = api_instance.post_manga_id_list_list_id(id, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->post_manga_id_list_list_id: %s\n" % e)
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

# **put_list_id**
> CustomListResponse put_list_id(id, body=body)

Update CustomList

The size of the body is limited to 8KB.

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CustomListApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | CustomList ID
body = mangadex_openapi.CustomListEdit() # CustomListEdit |  (optional)

try:
    # Update CustomList
    api_response = api_instance.put_list_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomListApi->put_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| CustomList ID | 
 **body** | [**CustomListEdit**](CustomListEdit.md)|  | [optional] 

### Return type

[**CustomListResponse**](CustomListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

