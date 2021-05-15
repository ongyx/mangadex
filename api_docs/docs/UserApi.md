# mangadex_openapi.UserApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_follows_group**](UserApi.md#get_user_follows_group) | **GET** /user/follows/group | Get logged User followed Groups
[**get_user_follows_manga**](UserApi.md#get_user_follows_manga) | **GET** /user/follows/manga | Get logged User followed Manga list
[**get_user_follows_user**](UserApi.md#get_user_follows_user) | **GET** /user/follows/user | Get logged User followed User list
[**get_user_id**](UserApi.md#get_user_id) | **GET** /user/{id} | Get User
[**get_user_me**](UserApi.md#get_user_me) | **GET** /user/me | Logged User details

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
api_instance = mangadex_openapi.UserApi(mangadex_openapi.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get logged User followed Groups
    api_response = api_instance.get_user_follows_group(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_follows_group: %s\n" % e)
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

# **get_user_follows_manga**
> MangaList get_user_follows_manga(limit=limit, offset=offset)

Get logged User followed Manga list

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.UserApi(mangadex_openapi.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get logged User followed Manga list
    api_response = api_instance.get_user_follows_manga(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_follows_manga: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**MangaList**](MangaList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_user**
> UserList get_user_follows_user(limit=limit, offset=offset)

Get logged User followed User list

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.UserApi(mangadex_openapi.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
offset = 56 # int |  (optional)

try:
    # Get logged User followed User list
    api_response = api_instance.get_user_follows_user(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_follows_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**UserList**](UserList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_id**
> UserResponse get_user_id(id)

Get User

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.UserApi(mangadex_openapi.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | User ID

try:
    # Get User
    api_response = api_instance.get_user_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| User ID | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_me**
> UserResponse get_user_me()

Logged User details

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.UserApi(mangadex_openapi.ApiClient(configuration))

try:
    # Logged User details
    api_response = api_instance.get_user_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

