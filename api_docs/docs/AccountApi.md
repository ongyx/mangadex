# mangadex_openapi.AccountApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_activate_code**](AccountApi.md#get_account_activate_code) | **GET** /account/activate/{code} | Activate account
[**post_account_activate_resend**](AccountApi.md#post_account_activate_resend) | **POST** /account/activate/resend | Resend Activation code
[**post_account_create**](AccountApi.md#post_account_create) | **POST** /account/create | Create Account
[**post_account_recover**](AccountApi.md#post_account_recover) | **POST** /account/recover | Recover given Account
[**post_account_recover_code**](AccountApi.md#post_account_recover_code) | **POST** /account/recover/{code} | Complete Account recover

# **get_account_activate_code**
> AccountActivateResponse get_account_activate_code(code)

Activate account

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi()
code = 'code_example' # str | 

try:
    # Activate account
    api_response = api_instance.get_account_activate_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_activate_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**AccountActivateResponse**](AccountActivateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_activate_resend**
> AccountActivateResponse post_account_activate_resend(body=body)

Resend Activation code

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi()
body = mangadex_openapi.SendAccountActivationCode() # SendAccountActivationCode | The size of the body is limited to 1KB. (optional)

try:
    # Resend Activation code
    api_response = api_instance.post_account_activate_resend(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_activate_resend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendAccountActivationCode**](SendAccountActivationCode.md)| The size of the body is limited to 1KB. | [optional] 

### Return type

[**AccountActivateResponse**](AccountActivateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_create**
> UserResponse post_account_create(body=body)

Create Account

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi()
body = mangadex_openapi.CreateAccount() # CreateAccount | The size of the body is limited to 4KB. (optional)

try:
    # Create Account
    api_response = api_instance.post_account_create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAccount**](CreateAccount.md)| The size of the body is limited to 4KB. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_recover**
> AccountActivateResponse post_account_recover(body=body)

Recover given Account

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi()
body = mangadex_openapi.SendAccountActivationCode() # SendAccountActivationCode | The size of the body is limited to 1KB. (optional)

try:
    # Recover given Account
    api_response = api_instance.post_account_recover(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_recover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendAccountActivationCode**](SendAccountActivationCode.md)| The size of the body is limited to 1KB. | [optional] 

### Return type

[**AccountActivateResponse**](AccountActivateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_recover_code**
> AccountActivateResponse post_account_recover_code(code, body=body)

Complete Account recover

### Example
```python
from __future__ import print_function
import time
import mangadex_openapi
from mangadex_openapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mangadex_openapi.AccountApi()
code = 'code_example' # str | 
body = mangadex_openapi.RecoverCompleteBody() # RecoverCompleteBody | The size of the body is limited to 2KB. (optional)

try:
    # Complete Account recover
    api_response = api_instance.post_account_recover_code(code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->post_account_recover_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **body** | [**RecoverCompleteBody**](RecoverCompleteBody.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**AccountActivateResponse**](AccountActivateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

