# mangadex_openapi.ScanlationGroupApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_group_id**](ScanlationGroupApi.md#delete_group_id) | **DELETE** /group/{id} | Delete Scanlation Group
[**delete_group_id_follow**](ScanlationGroupApi.md#delete_group_id_follow) | **DELETE** /group/{id}/follow | Unfollow Scanlation Group
[**get_group_id**](ScanlationGroupApi.md#get_group_id) | **GET** /group/{id} | View Scanlation Group
[**get_search_group**](ScanlationGroupApi.md#get_search_group) | **GET** /group | Scanlation Group list
[**get_user_follows_group**](ScanlationGroupApi.md#get_user_follows_group) | **GET** /user/follows/group | Get logged User followed Groups
[**post_group**](ScanlationGroupApi.md#post_group) | **POST** /group | Create Scanlation Group
[**post_group_id_follow**](ScanlationGroupApi.md#post_group_id_follow) | **POST** /group/{id}/follow | Follow Scanlation Group
[**put_group_id**](ScanlationGroupApi.md#put_group_id) | **PUT** /group/{id} | Update Scanlation Group

# **delete_group_id**
> Response delete_group_id(id)

Delete Scanlation Group

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Scanlation Group ID

try:
    # Delete Scanlation Group
    api_response = api_instance.delete_group_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->delete_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Scanlation Group ID | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_id_follow**
> Response delete_group_id_follow(id)

Unfollow Scanlation Group

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Unfollow Scanlation Group
    api_response = api_instance.delete_group_id_follow(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->delete_group_id_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_id**
> ScanlationGroupResponse get_group_id(id)

View Scanlation Group

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Scanlation Group ID

try:
    # View Scanlation Group
    api_response = api_instance.get_group_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->get_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Scanlation Group ID | 

### Return type

[**ScanlationGroupResponse**](ScanlationGroupResponse.md)

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
api_instance = mangadex_openapi.ScanlationGroupApi()
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)
ids = ['ids_example'] # list[str] | ScanlationGroup ids (limited to 100 per request) (optional)
name = 'name_example' # str |  (optional)

try:
    # Scanlation Group list
    api_response = api_instance.get_search_group(limit=limit, offset=offset, ids=ids, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->get_search_group: %s\n" % e)
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

# **get_user_follows_group**
> ScanlationGroupList get_user_follows_group(limit=limit, offset=offset)

Get logged User followed Groups

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi(mangadex_openapi.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get logged User followed Groups
    api_response = api_instance.get_user_follows_group(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->get_user_follows_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**ScanlationGroupList**](ScanlationGroupList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group**
> ScanlationGroupResponse post_group(body=body)

Create Scanlation Group

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi(mangadex_openapi.ApiClient(configuration))
body = mangadex_openapi.CreateScanlationGroup() # CreateScanlationGroup | The size of the body is limited to 8KB. (optional)

try:
    # Create Scanlation Group
    api_response = api_instance.post_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->post_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateScanlationGroup**](CreateScanlationGroup.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**ScanlationGroupResponse**](ScanlationGroupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group_id_follow**
> Response post_group_id_follow(id)

Follow Scanlation Group

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Follow Scanlation Group
    api_response = api_instance.post_group_id_follow(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->post_group_id_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_group_id**
> ScanlationGroupResponse put_group_id(id, body=body)

Update Scanlation Group

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.ScanlationGroupApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Scanlation Group ID
body = mangadex_openapi.ScanlationGroupEdit() # ScanlationGroupEdit | The size of the body is limited to 8KB. (optional)

try:
    # Update Scanlation Group
    api_response = api_instance.put_group_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanlationGroupApi->put_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Scanlation Group ID | 
 **body** | [**ScanlationGroupEdit**](ScanlationGroupEdit.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**ScanlationGroupResponse**](ScanlationGroupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

