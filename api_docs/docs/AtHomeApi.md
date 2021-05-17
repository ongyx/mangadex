# mangadex_openapi.AtHomeApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_at_home_server_chapter_id**](AtHomeApi.md#get_at_home_server_chapter_id) | **GET** /at-home/server/{chapterId} | Get MangaDex@Home server URL

# **get_at_home_server_chapter_id**
> InlineResponse2003 get_at_home_server_chapter_id(chapter_id, force_port443=force_port443)

Get MangaDex@Home server URL

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AtHomeApi()
chapter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Chapter ID
force_port443 = false # bool | Force selecting from MangaDex@Home servers that use the standard HTTPS port 443.  While the conventional port for HTTPS traffic is 443 and servers are encouraged to use it, it is not a hard requirement as it technically isn't anything special.  However, some misbehaving school/office network will at time block traffic to non-standard ports, and setting this flag to `true` will ensure selection of a server that uses these. (optional) (default to false)

try:
    # Get MangaDex@Home server URL
    api_response = api_instance.get_at_home_server_chapter_id(chapter_id, force_port443=force_port443)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AtHomeApi->get_at_home_server_chapter_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chapter_id** | [**str**](.md)| Chapter ID | 
 **force_port443** | **bool**| Force selecting from MangaDex@Home servers that use the standard HTTPS port 443.  While the conventional port for HTTPS traffic is 443 and servers are encouraged to use it, it is not a hard requirement as it technically isn&#x27;t anything special.  However, some misbehaving school/office network will at time block traffic to non-standard ports, and setting this flag to &#x60;true&#x60; will ensure selection of a server that uses these. | [optional] [default to false]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

