# mangadex_openapi.AuthorApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_author_id**](AuthorApi.md#delete_author_id) | **DELETE** /author/{id} | Delete Author
[**get_author**](AuthorApi.md#get_author) | **GET** /author | Author list
[**get_author_id**](AuthorApi.md#get_author_id) | **GET** /author/{id} | Get Author
[**post_author**](AuthorApi.md#post_author) | **POST** /author | Create Author
[**put_author_id**](AuthorApi.md#put_author_id) | **PUT** /author/{id} | Update Author

# **delete_author_id**
> Response delete_author_id(id)

Delete Author

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.AuthorApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Author ID

try:
    # Delete Author
    api_response = api_instance.delete_author_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->delete_author_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Author ID | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = mangadex_openapi.AuthorApi()
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
    print("Exception when calling AuthorApi->get_author: %s\n" % e)
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

# **get_author_id**
> AuthorResponse get_author_id(id)

Get Author

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AuthorApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Author ID

try:
    # Get Author
    api_response = api_instance.get_author_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->get_author_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Author ID | 

### Return type

[**AuthorResponse**](AuthorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_author**
> AuthorResponse post_author(body=body)

Create Author

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.AuthorApi(mangadex_openapi.ApiClient(configuration))
body = mangadex_openapi.AuthorCreate() # AuthorCreate | The size of the body is limited to 2KB. (optional)

try:
    # Create Author
    api_response = api_instance.post_author(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->post_author: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorCreate**](AuthorCreate.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**AuthorResponse**](AuthorResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_author_id**
> AuthorResponse put_author_id(id, body=body)

Update Author

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.AuthorApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Author ID
body = mangadex_openapi.AuthorEdit() # AuthorEdit | The size of the body is limited to 2KB. (optional)

try:
    # Update Author
    api_response = api_instance.put_author_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorApi->put_author_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Author ID | 
 **body** | [**AuthorEdit**](AuthorEdit.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**AuthorResponse**](AuthorResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

