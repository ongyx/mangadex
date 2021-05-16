# mangadex_openapi.LegacyApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_legacy_mapping**](LegacyApi.md#post_legacy_mapping) | **POST** /legacy/mapping | Legacy ID mapping

# **post_legacy_mapping**
> list[MappingIdResponse] post_legacy_mapping(body=body)

Legacy ID mapping

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.LegacyApi()
body = mangadex_openapi.MappingIdBody() # MappingIdBody | The size of the body is limited to 10KB. (optional)

try:
    # Legacy ID mapping
    api_response = api_instance.post_legacy_mapping(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyApi->post_legacy_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MappingIdBody**](MappingIdBody.md)| The size of the body is limited to 10KB. | [optional] 

### Return type

[**list[MappingIdResponse]**](MappingIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

