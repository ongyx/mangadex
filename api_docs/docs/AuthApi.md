# mangadex_openapi.AuthApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_check**](AuthApi.md#get_auth_check) | **GET** /auth/check | Check token
[**post_auth_login**](AuthApi.md#post_auth_login) | **POST** /auth/login | Login
[**post_auth_logout**](AuthApi.md#post_auth_logout) | **POST** /auth/logout | Logout
[**post_auth_refresh**](AuthApi.md#post_auth_refresh) | **POST** /auth/refresh | Refresh token

# **get_auth_check**
> CheckResponse get_auth_check()

Check token

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.AuthApi(mangadex_openapi.ApiClient(configuration))

try:
    # Check token
    api_response = api_instance.get_auth_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_login**
> LoginResponse post_auth_login(body=body)

Login

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AuthApi()
body = mangadex_openapi.Login() # Login | The size of the body is limited to 2KB. (optional)

try:
    # Login
    api_response = api_instance.post_auth_login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_logout**
> LogoutResponse post_auth_logout()

Logout

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mangadex_openapi.AuthApi(mangadex_openapi.ApiClient(configuration))

try:
    # Logout
    api_response = api_instance.post_auth_logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogoutResponse**](LogoutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_refresh**
> RefreshResponse post_auth_refresh(body=body)

Refresh token

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AuthApi()
body = mangadex_openapi.RefreshToken() # RefreshToken | The size of the body is limited to 2KB. (optional)

try:
    # Refresh token
    api_response = api_instance.post_auth_refresh(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshToken**](RefreshToken.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**RefreshResponse**](RefreshResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

