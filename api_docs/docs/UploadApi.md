# mangadex_openapi.UploadApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_cover**](UploadApi.md#upload_cover) | **POST** /cover/{mangaId} | Upload Cover

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
api_instance = mangadex_openapi.UploadApi(mangadex_openapi.ApiClient(configuration))
manga_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
file = 'file_example' # str |  (optional)

try:
    # Upload Cover
    api_response = api_instance.upload_cover(manga_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->upload_cover: %s\n" % e)
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

