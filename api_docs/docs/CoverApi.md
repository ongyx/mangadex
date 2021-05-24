# mangadex_openapi.CoverApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cover**](CoverApi.md#delete_cover) | **DELETE** /cover/{coverId} | Delete Cover
[**edit_cover**](CoverApi.md#edit_cover) | **PUT** /cover/{coverId} | Edit Cover
[**get_cover**](CoverApi.md#get_cover) | **GET** /cover | CoverArt list
[**get_cover_0**](CoverApi.md#get_cover_0) | **GET** /cover/{coverId} | Get Cover
[**upload_cover**](CoverApi.md#upload_cover) | **POST** /cover/{mangaId} | Upload Cover

# **delete_cover**
> Response delete_cover(cover_id)

Delete Cover

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.CoverApi()
cover_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete Cover
    api_response = api_instance.delete_cover(cover_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverApi->delete_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cover_id** | [**str**](.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cover**
> CoverResponse edit_cover(cover_id, body=body)

Edit Cover

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.CoverApi()
cover_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = mangadex_openapi.CoverEdit() # CoverEdit | The size of the body is limited to 2KB. (optional)

try:
    # Edit Cover
    api_response = api_instance.edit_cover(cover_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverApi->edit_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cover_id** | [**str**](.md)|  | 
 **body** | [**CoverEdit**](CoverEdit.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**CoverResponse**](CoverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = mangadex_openapi.CoverApi()
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
    print("Exception when calling CoverApi->get_cover: %s\n" % e)
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

# **get_cover_0**
> CoverResponse get_cover_0(cover_id)

Get Cover

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CoverApi(mangadex_openapi.ApiClient(configuration))
cover_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Cover
    api_response = api_instance.get_cover_0(cover_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverApi->get_cover_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cover_id** | [**str**](.md)|  | 

### Return type

[**CoverResponse**](CoverResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_cover**
> CoverResponse upload_cover(manga_id, file=file)

Upload Cover

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.CoverApi(mangadex_openapi.ApiClient(configuration))
manga_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
file = 'file_example' # str |  (optional)

try:
    # Upload Cover
    api_response = api_instance.upload_cover(manga_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverApi->upload_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_id** | [**str**](.md)|  | 
 **file** | **str**|  | [optional] 

### Return type

[**CoverResponse**](CoverResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

