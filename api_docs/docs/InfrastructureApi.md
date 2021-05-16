# mangadex_openapi.InfrastructureApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_get**](InfrastructureApi.md#ping_get) | **GET** /ping | Ping the server

# **ping_get**
> str ping_get()

Ping the server

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.InfrastructureApi()

try:
    # Ping the server
    api_response = api_instance.ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfrastructureApi->ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

