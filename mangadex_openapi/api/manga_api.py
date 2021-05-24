# coding: utf-8

"""
    MangaDex API

    MangaDex is an ad-free manga reader offering high-quality images!  This document details our API as it is right now. It is in no way a promise to never change it, although we will endeavour to publicly notify any major change.  # Authentication  You can login with the `/auth/login` endpoint. On success, it will return a JWT that remains valid for 15 minutes along with a session token that allows refreshing without re-authenticating for 1 month.  # Rate limits  The API enforces rate-limits to protect our servers against malicious and/or mistaken use. The API keeps track of the requests on an IP-by-IP basis. Hence, if you're on a VPN, proxy or a shared network in general, the requests of other users on this network might affect you.  At first, a **global limit of 5 requests per second per IP address** is in effect.  > This limit is enforced across multiple load-balancers, and thus is not an exact value but rather a lower-bound that we guarantee. The exact value will be somewhere in the range `[5, 5*n]` (with `n` being the number of load-balancers currently active). The exact value within this range will depend on the current traffic patterns we are experiencing.  On top of this, **some endpoints are further restricted** as follows:  | Endpoint                           | Requests per time period    | Time period in minutes | |------------------------------------|--------------------------   |------------------------| | `POST   /account/create`           | 1                           | 60                     | | `GET    /account/activate/{code}`  | 30                          | 60                     | | `POST   /account/activate/resend`  | 5                           | 60                     | | `POST   /account/recover`          | 5                           | 60                     | | `POST   /account/recover/{code}`   | 5                           | 60                     | | `POST   /auth/login`               | 30                          | 60                     | | `POST   /auth/refresh`             | 30                          | 60                     | | `POST   /author`                   | 10                          | 60                     | | `PUT    /author`                   | 10                          | 1                      | | `DELETE /author/{id}`              | 10                          | 10                     | | `POST   /captcha/solve`            | 10                          | 10                     | | `POST   /chapter/{id}/read`        | 300                         | 10                     | | `PUT    /chapter/{id}`             | 10                          | 1                      | | `DELETE /chapter/{id}`             | 10                          | 1                      | | `POST   /manga`                    | 10                          | 60                     | | `PUT    /manga/{id}`               | 10                          | 60                     | | `DELETE /manga/{id}`               | 10                          | 10                     | | `POST   /cover`                    | 10                          | 1                      | | `PUT    /cover/{id}`               | 10                          | 1                      | | `DELETE /cover/{id}`               | 10                          | 10                     | | `POST   /group`                    | 10                          | 60                     | | `PUT    /group/{id}`               | 10                          | 1                      | | `DELETE /group/{id}`               | 10                          | 10                     | | `GET    /at-home/server/{id}`      | 60                          | 1                      |  Calling these endpoints will further provide details via the following headers about your remaining quotas:  | Header                    | Description                                                                 | |---------------------------|-----------------------------------------------------------------------------| | `X-RateLimit-Limit`       | Maximal number of requests this endpoint allows per its time period         | | `X-RateLimit-Remaining`   | Remaining number of requests within your quota for the current time period  | | `X-RateLimit-Retry-After` | Timestamp of the end of the current time period, as UNIX timestamp          |  # Captchas  Some endpoints may require captchas to proceed, in order to slow down automated malicious traffic. Legitimate users might also be affected, based on the frequency of write requests or due certain endpoints being particularly sensitive to malicious use, such as user signup.  Once an endpoint decides that a captcha needs to be solved, a 403 Forbidden response will be returned, with the error code `captcha_required_exception`. The sitekey needed for recaptcha to function is provided in both the `X-Captcha-Sitekey` header field, as well as in the error context, specified as `siteKey` parameter.  The captcha result of the client can either be passed into the repeated original request with the `X-Captcha-Result` header or alternatively to the `POST /captcha/solve` endpoint. The time a solved captcha is remembered varies across different endpoints and can also be influenced by individual client behavior.  Authentication is not required for the `POST /captcha/solve` endpoint, captchas are tracked both by client ip and logged in user id. If you are logged in, you want to send the session token along, so you validate the captcha for your client ip and user id at the same time, but it is not required.  # Reading a chapter using the API  ## Retrieving pages from the MangaDex@Home network  A valid [MangaDex@Home network](https://mangadex.network) page URL is in the following format: `{server-specific base url}/{temporary access token}/{quality mode}/{chapter hash}/{filename}`  There are currently 2 quality modes: - `data`: Original upload quality - `data-saver`: Compressed quality  Upon fetching a chapter from the API, you will find 4 fields necessary to compute MangaDex@Home page URLs:  | Field                        | Type     | Description                       | |------------------------------|----------|-----------------------------------| | `.data.id`                   | `string` | API Chapter ID                    | | `.data.attributes.hash`      | `string` | MangaDex@Home Chapter Hash        | | `.data.attributes.data`      | `array`  | data quality mode filenames       | | `.data.attributes.dataSaver` | `array`  | data-saver quality mode filenames |  Example ```json GET /chapter/{id}  {   ...,   \"data\": {     \"id\": \"e46e5118-80ce-4382-a506-f61a24865166\",     ...,     \"attributes\": {       ...,       \"hash\": \"e199c7d73af7a58e8a4d0263f03db660\",       \"data\": [         \"x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png\",         ...       ],       \"dataSaver\": [         \"x1-ab2b7c8f30c843aa3a53c29bc8c0e204fba4ab3e75985d761921eb6a52ff6159.jpg\",         ...       ]     }   } } ```  From this point you miss only the base URL to an assigned MangaDex@Home server for your client and chapter. This is retrieved via a `GET` request to `/at-home/server/{ chapter .data.id }`.  Example: ```json GET /at-home/server/e46e5118-80ce-4382-a506-f61a24865166  {   \"baseUrl\": \"https://abcdefg.hijklmn.mangadex.network:12345/some-token\" } ```  The full URL is the constructed as follows ``` { server .baseUrl }/{ quality mode }/{ chapter .data.attributes.hash }/{ chapter .data.attributes.{ quality mode }.[*] }  Examples  data quality: https://abcdefg.hijklmn.mangadex.network:12345/some-token/data/e199c7d73af7a58e8a4d0263f03db660/x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png        base url: https://abcdefg.hijklmn.mangadex.network:12345/some-token   quality mode: data   chapter hash: e199c7d73af7a58e8a4d0263f03db660       filename: x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png   data-saver quality: https://abcdefg.hijklmn.mangadex.network:12345/some-token/data-saver/e199c7d73af7a58e8a4d0263f03db660/x1-ab2b7c8f30c843aa3a53c29bc8c0e204fba4ab3e75985d761921eb6a52ff6159.jpg        base url: https://abcdefg.hijklmn.mangadex.network:12345/some-token   quality mode: data-saver   chapter hash: e199c7d73af7a58e8a4d0263f03db660       filename: x1-ab2b7c8f30c843aa3a53c29bc8c0e204fba4ab3e75985d761921eb6a52ff6159.jpg ```  If the server you have been assigned fails to serve images, you are allowed to call the `/at-home/server/{ chapter id }` endpoint again to get another server.  Whether successful or not, **please do report the result you encountered as detailed below**. This is so we can pull the faulty server out of the network.  ## Report  In order to keep track of the health of the servers in the network and to improve the quality of service and reliability, we ask that you call the MangaDex@Home report endpoint after each image you retrieve, whether successfully or not.  It is a `POST` request against `https://api.mangadex.network/report` and expects the following payload with our example above:  | Field                       | Type       | Description                                                                         | |-----------------------------|------------|-------------------------------------------------------------------------------------| | `url`                       | `string`   | The full URL of the image                                                           | | `success`                   | `boolean`  | Whether the image was successfully retrieved                                        | | `cached `                   | `boolean`  | `true` iff the server returned an `X-Cache` header with a value starting with `HIT` | | `bytes`                     | `number`   | The size in bytes of the retrieved image                                            | | `duration`                  | `number`   | The time in miliseconds that the complete retrieval (not TTFB) of this image took   |  Examples herafter.  **Success:** ```json POST https://api.mangadex.network/report Content-Type: application/json  {   \"url\": \"https://abcdefg.hijklmn.mangadex.network:12345/some-token/data/e199c7d73af7a58e8a4d0263f03db660/x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png\",   \"success\": true,   \"bytes\": 727040,   \"duration\": 235,   \"cached\": true } ```  **Failure:** ```json POST https://api.mangadex.network/report Content-Type: application/json  {  \"url\": \"https://abcdefg.hijklmn.mangadex.network:12345/some-token/data/e199c7d73af7a58e8a4d0263f03db660/x1-b765e86d5ecbc932cf3f517a8604f6ac6d8a7f379b0277a117dc7c09c53d041e.png\",  \"success\": false,  \"bytes\": 25,  \"duration\": 235,  \"cached\": false } ```  While not strictly necessary, this helps us monitor the network's healthiness, and we appreciate your cooperation towards this goal. If no one reports successes and failures, we have no way to know that a given server is slow/broken, which eventually results in broken image retrieval for everyone.  # Static data  ## Manga publication demographic  | Value            | Description               | |------------------|---------------------------| | shounen          | Manga is a Shounen        | | shoujo           | Manga is a Shoujo         | | josei            | Manga is a Josei          | | seinen           | Manga is a Seinen         |  ## Manga status  | Value            | Description               | |------------------|---------------------------| | ongoing          | Manga is still going on   | | completed        | Manga is completed        | | hiatus           | Manga is paused           | | cancelled        | Manga has been cancelled  |  ## Manga reading status  | Value            | |------------------| | reading          | | on_hold          | | plan\\_to\\_read   | | dropped          | | re\\_reading      | | completed        |  ## Manga content rating  | Value            | Description               | |------------------|---------------------------| | safe             | Safe content              | | suggestive       | Suggestive content        | | erotica          | Erotica content           | | pornographic     | Pornographic content      |  ## CustomList visibility  | Value            | Description               | |------------------|---------------------------| | public           | CustomList is public      | | private          | CustomList is private     |  ## Relationship types  | Value            | Description                    | |------------------|--------------------------------| | manga            | Manga resource                 | | chapter          | Chapter resource               | | cover_art        | A Cover Art for a manga `*`    | | author           | Author resource                | | artist           | Author resource (drawers only) | | scanlation_group | ScanlationGroup resource       | | tag              | Tag resource                   | | user             | User resource                  | | custom_list      | CustomList resource            |  `*` Note, that on manga resources you get only one cover_art resource relation marking the primary cover if there are more than one. By default this will be the latest volume's cover art. If you like to see all the covers for a given manga, use the cover search endpoint for your mangaId and select the one you wish to display.  ## Manga links data  In Manga attributes you have the `links` field that is a JSON object with some strange keys, here is how to decode this object:  | Key   | Related site  | URL                                                                                           | URL details                                                    | |-------|---------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------| | al    | anilist       | https://anilist.co/manga/`{id}`                                                               | Stored as id                                                   | | ap    | animeplanet   | https://www.anime-planet.com/manga/`{slug}`                                                   | Stored as slug                                                 | | bw    | bookwalker.jp | https://bookwalker.jp/`{slug}`                                                                | Stored has \"series/{id}\"                                       | | mu    | mangaupdates  | https://www.mangaupdates.com/series.html?id=`{id}`                                            | Stored has id                                                  | | nu    | novelupdates  | https://www.novelupdates.com/series/`{slug}`                                                  | Stored has slug                                                | | kt    | kitsu.io      | https://kitsu.io/api/edge/manga/`{id}` or https://kitsu.io/api/edge/manga?filter[slug]={slug} | If integer, use id version of the URL, otherwise use slug one  | | amz   | amazon        | N/A                                                                                           | Stored as full URL                                             | | ebj   | ebookjapan    | N/A                                                                                           | Stored as full URL                                             | | mal   | myanimelist   | https://myanimelist.net/manga/{id}                                                            | Store as id                                                    | | raw   | N/A           | N/A                                                                                           | Stored as full URL, untranslated stuff URL (original language) | | engtl | N/A           | N/A                                                                                           | Stored as full URL, official english licenced URL              |  # noqa: E501

    OpenAPI spec version: 5.0.12
    Contact: mangadexstaff@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mangadex_openapi.api_client import ApiClient


class MangaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_manga_id(self, id, **kwargs):  # noqa: E501
        """Delete Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manga_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_manga_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_manga_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_manga_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manga_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_manga_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_manga_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Response",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_manga_id_follow(self, id, **kwargs):  # noqa: E501
        """Unfollow Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manga_id_follow(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_manga_id_follow_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_manga_id_follow_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def delete_manga_id_follow_with_http_info(self, id, **kwargs):  # noqa: E501
        """Unfollow Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manga_id_follow_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_manga_id_follow" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_manga_id_follow`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/follow",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Response",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_manga_id_list_list_id(self, id, list_id, **kwargs):  # noqa: E501
        """Remove Manga in CustomList  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manga_id_list_list_id(id, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param str list_id: CustomList ID (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_manga_id_list_list_id_with_http_info(
                id, list_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_manga_id_list_list_id_with_http_info(
                id, list_id, **kwargs
            )  # noqa: E501
            return data

    def delete_manga_id_list_list_id_with_http_info(
        self, id, list_id, **kwargs
    ):  # noqa: E501
        """Remove Manga in CustomList  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_manga_id_list_list_id_with_http_info(id, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param str list_id: CustomList ID (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "list_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_manga_id_list_list_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_manga_id_list_list_id`"
            )  # noqa: E501
        # verify the required parameter 'list_id' is set
        if "list_id" not in params or params["list_id"] is None:
            raise ValueError(
                "Missing the required parameter `list_id` when calling `delete_manga_id_list_list_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "list_id" in params:
            path_params["listId"] = params["list_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/list/{listId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Response",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_chapter_readmarkers(self, id, **kwargs):  # noqa: E501
        """Manga read markers  # noqa: E501

        A list of chapter ids that are marked as read for the specified manga  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_chapter_readmarkers(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_chapter_readmarkers_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_manga_chapter_readmarkers_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def get_manga_chapter_readmarkers_with_http_info(self, id, **kwargs):  # noqa: E501
        """Manga read markers  # noqa: E501

        A list of chapter ids that are marked as read for the specified manga  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_chapter_readmarkers_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_chapter_readmarkers" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_manga_chapter_readmarkers`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/read",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2001",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_chapter_readmarkers2(self, ids, **kwargs):  # noqa: E501
        """Manga read markers  # noqa: E501

        A list of chapter ids that are marked as read for the given manga ids  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_chapter_readmarkers2(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: Manga ids (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_chapter_readmarkers2_with_http_info(
                ids, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_manga_chapter_readmarkers2_with_http_info(
                ids, **kwargs
            )  # noqa: E501
            return data

    def get_manga_chapter_readmarkers2_with_http_info(
        self, ids, **kwargs
    ):  # noqa: E501
        """Manga read markers  # noqa: E501

        A list of chapter ids that are marked as read for the given manga ids  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_chapter_readmarkers2_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: Manga ids (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["ids"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_chapter_readmarkers2" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'ids' is set
        if "ids" not in params or params["ids"] is None:
            raise ValueError(
                "Missing the required parameter `ids` when calling `get_manga_chapter_readmarkers2`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "ids" in params:
            query_params.append(("ids", params["ids"]))  # noqa: E501
            collection_formats["ids"] = "multi"  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/read",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2001",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_id(self, id, **kwargs):  # noqa: E501
        """View Manga  # noqa: E501

        View Manga.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_manga_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_manga_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """View Manga  # noqa: E501

        View Manga.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_manga_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MangaResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_id_feed(self, id, **kwargs):  # noqa: E501
        """Manga feed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_id_feed(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param int limit:
        :param int offset:
        :param list[str] translated_language:
        :param str created_at_since:
        :param str updated_at_since:
        :param str publish_at_since:
        :param Order6 order:
        :return: ChapterList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_id_feed_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_manga_id_feed_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_manga_id_feed_with_http_info(self, id, **kwargs):  # noqa: E501
        """Manga feed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_id_feed_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param int limit:
        :param int offset:
        :param list[str] translated_language:
        :param str created_at_since:
        :param str updated_at_since:
        :param str publish_at_since:
        :param Order6 order:
        :return: ChapterList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "id",
            "limit",
            "offset",
            "translated_language",
            "created_at_since",
            "updated_at_since",
            "publish_at_since",
            "order",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_id_feed" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_manga_id_feed`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501
        if "translated_language" in params:
            query_params.append(
                ("translatedLanguage", params["translated_language"])
            )  # noqa: E501
            collection_formats["translatedLanguage"] = "multi"  # noqa: E501
        if "created_at_since" in params:
            query_params.append(
                ("createdAtSince", params["created_at_since"])
            )  # noqa: E501
        if "updated_at_since" in params:
            query_params.append(
                ("updatedAtSince", params["updated_at_since"])
            )  # noqa: E501
        if "publish_at_since" in params:
            query_params.append(
                ("publishAtSince", params["publish_at_since"])
            )  # noqa: E501
        if "order" in params:
            query_params.append(("order", params["order"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/feed",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ChapterList",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_id_status(self, id, **kwargs):  # noqa: E501
        """Get a Manga reading status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_id_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_id_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_manga_id_status_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_manga_id_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a Manga reading status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_id_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_id_status" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_manga_id_status`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/status",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2005",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_random(self, **kwargs):  # noqa: E501
        """Get a random Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_random(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_random_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_manga_random_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_manga_random_with_http_info(self, **kwargs):  # noqa: E501
        """Get a random Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_random_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_random" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/manga/random",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MangaResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_status(self, **kwargs):  # noqa: E501
        """Get all Manga reading status for logged User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: Used to filter the list by given status
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_manga_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_manga_status_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Manga reading status for logged User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: Used to filter the list by given status
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["status"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_status" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "status" in params:
            query_params.append(("status", params["status"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/status",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2004",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_manga_tag(self, **kwargs):  # noqa: E501
        """Tag list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_tag(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TagResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_manga_tag_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_manga_tag_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_manga_tag_with_http_info(self, **kwargs):  # noqa: E501
        """Tag list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manga_tag_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TagResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manga_tag" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/manga/tag",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[TagResponse]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_search_manga(self, **kwargs):  # noqa: E501
        """Manga list  # noqa: E501

        Search a list of Manga.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_manga(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :param str title:
        :param list[str] authors:
        :param list[str] artists:
        :param int year:
        :param list[str] included_tags:
        :param str included_tags_mode:
        :param list[str] excluded_tags:
        :param str excluded_tags_mode:
        :param list[str] status:
        :param list[str] original_language:
        :param list[str] publication_demographic:
        :param list[str] ids: Manga ids (limited to 100 per request)
        :param list[str] content_rating:
        :param str created_at_since:
        :param str updated_at_since:
        :param Order order:
        :return: MangaList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_search_manga_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_search_manga_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_search_manga_with_http_info(self, **kwargs):  # noqa: E501
        """Manga list  # noqa: E501

        Search a list of Manga.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_manga_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :param str title:
        :param list[str] authors:
        :param list[str] artists:
        :param int year:
        :param list[str] included_tags:
        :param str included_tags_mode:
        :param list[str] excluded_tags:
        :param str excluded_tags_mode:
        :param list[str] status:
        :param list[str] original_language:
        :param list[str] publication_demographic:
        :param list[str] ids: Manga ids (limited to 100 per request)
        :param list[str] content_rating:
        :param str created_at_since:
        :param str updated_at_since:
        :param Order order:
        :return: MangaList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "limit",
            "offset",
            "title",
            "authors",
            "artists",
            "year",
            "included_tags",
            "included_tags_mode",
            "excluded_tags",
            "excluded_tags_mode",
            "status",
            "original_language",
            "publication_demographic",
            "ids",
            "content_rating",
            "created_at_since",
            "updated_at_since",
            "order",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_manga" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501
        if "title" in params:
            query_params.append(("title", params["title"]))  # noqa: E501
        if "authors" in params:
            query_params.append(("authors", params["authors"]))  # noqa: E501
            collection_formats["authors"] = "multi"  # noqa: E501
        if "artists" in params:
            query_params.append(("artists", params["artists"]))  # noqa: E501
            collection_formats["artists"] = "multi"  # noqa: E501
        if "year" in params:
            query_params.append(("year", params["year"]))  # noqa: E501
        if "included_tags" in params:
            query_params.append(("includedTags", params["included_tags"]))  # noqa: E501
            collection_formats["includedTags"] = "multi"  # noqa: E501
        if "included_tags_mode" in params:
            query_params.append(
                ("includedTagsMode", params["included_tags_mode"])
            )  # noqa: E501
        if "excluded_tags" in params:
            query_params.append(("excludedTags", params["excluded_tags"]))  # noqa: E501
            collection_formats["excludedTags"] = "multi"  # noqa: E501
        if "excluded_tags_mode" in params:
            query_params.append(
                ("excludedTagsMode", params["excluded_tags_mode"])
            )  # noqa: E501
        if "status" in params:
            query_params.append(("status", params["status"]))  # noqa: E501
            collection_formats["status"] = "multi"  # noqa: E501
        if "original_language" in params:
            query_params.append(
                ("originalLanguage", params["original_language"])
            )  # noqa: E501
            collection_formats["originalLanguage"] = "multi"  # noqa: E501
        if "publication_demographic" in params:
            query_params.append(
                ("publicationDemographic", params["publication_demographic"])
            )  # noqa: E501
            collection_formats["publicationDemographic"] = "multi"  # noqa: E501
        if "ids" in params:
            query_params.append(("ids", params["ids"]))  # noqa: E501
            collection_formats["ids"] = "multi"  # noqa: E501
        if "content_rating" in params:
            query_params.append(
                ("contentRating", params["content_rating"])
            )  # noqa: E501
            collection_formats["contentRating"] = "multi"  # noqa: E501
        if "created_at_since" in params:
            query_params.append(
                ("createdAtSince", params["created_at_since"])
            )  # noqa: E501
        if "updated_at_since" in params:
            query_params.append(
                ("updatedAtSince", params["updated_at_since"])
            )  # noqa: E501
        if "order" in params:
            query_params.append(("order", params["order"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/manga",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MangaList",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_user_follows_manga(self, **kwargs):  # noqa: E501
        """Get logged User followed Manga list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_follows_manga(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :return: MangaList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_user_follows_manga_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_follows_manga_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_follows_manga_with_http_info(self, **kwargs):  # noqa: E501
        """Get logged User followed Manga list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_follows_manga_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :return: MangaList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["limit", "offset"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_follows_manga" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/user/follows/manga",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MangaList",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_user_follows_manga_feed(self, **kwargs):  # noqa: E501
        """Get logged User followed Manga feed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_follows_manga_feed(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :param list[str] translated_language:
        :param str created_at_since:
        :param str updated_at_since:
        :param str publish_at_since:
        :param Order2 order:
        :return: ChapterList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_user_follows_manga_feed_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_user_follows_manga_feed_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def get_user_follows_manga_feed_with_http_info(self, **kwargs):  # noqa: E501
        """Get logged User followed Manga feed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_follows_manga_feed_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :param list[str] translated_language:
        :param str created_at_since:
        :param str updated_at_since:
        :param str publish_at_since:
        :param Order2 order:
        :return: ChapterList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "limit",
            "offset",
            "translated_language",
            "created_at_since",
            "updated_at_since",
            "publish_at_since",
            "order",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_follows_manga_feed" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501
        if "translated_language" in params:
            query_params.append(
                ("translatedLanguage", params["translated_language"])
            )  # noqa: E501
            collection_formats["translatedLanguage"] = "multi"  # noqa: E501
        if "created_at_since" in params:
            query_params.append(
                ("createdAtSince", params["created_at_since"])
            )  # noqa: E501
        if "updated_at_since" in params:
            query_params.append(
                ("updatedAtSince", params["updated_at_since"])
            )  # noqa: E501
        if "publish_at_since" in params:
            query_params.append(
                ("publishAtSince", params["publish_at_since"])
            )  # noqa: E501
        if "order" in params:
            query_params.append(("order", params["order"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/user/follows/manga/feed",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ChapterList",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def manga_id_aggregate_get(self, id, **kwargs):  # noqa: E501
        """Get Manga volumes & chapters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.manga_id_aggregate_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param list[str] translated_language:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.manga_id_aggregate_get_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.manga_id_aggregate_get_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def manga_id_aggregate_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Manga volumes & chapters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.manga_id_aggregate_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param list[str] translated_language:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "translated_language"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method manga_id_aggregate_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `manga_id_aggregate_get`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []
        if "translated_language" in params:
            query_params.append(
                ("translatedLanguage", params["translated_language"])
            )  # noqa: E501
            collection_formats["translatedLanguage"] = "multi"  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/aggregate",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse200",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_manga(self, **kwargs):  # noqa: E501
        """Create Manga  # noqa: E501

        Create a new Manga.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MangaCreate body: The size of the body is limited to 16KB.
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_manga_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_manga_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_manga_with_http_info(self, **kwargs):  # noqa: E501
        """Create Manga  # noqa: E501

        Create a new Manga.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MangaCreate body: The size of the body is limited to 16KB.
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_manga" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MangaResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_manga_id_follow(self, id, **kwargs):  # noqa: E501
        """Follow Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_id_follow(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_manga_id_follow_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_manga_id_follow_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def post_manga_id_follow_with_http_info(self, id, **kwargs):  # noqa: E501
        """Follow Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_id_follow_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_manga_id_follow" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `post_manga_id_follow`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/follow",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Response",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_manga_id_list_list_id(self, id, list_id, **kwargs):  # noqa: E501
        """Add Manga in CustomList  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_id_list_list_id(id, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param str list_id: CustomList ID (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_manga_id_list_list_id_with_http_info(
                id, list_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.post_manga_id_list_list_id_with_http_info(
                id, list_id, **kwargs
            )  # noqa: E501
            return data

    def post_manga_id_list_list_id_with_http_info(
        self, id, list_id, **kwargs
    ):  # noqa: E501
        """Add Manga in CustomList  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_id_list_list_id_with_http_info(id, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param str list_id: CustomList ID (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "list_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_manga_id_list_list_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `post_manga_id_list_list_id`"
            )  # noqa: E501
        # verify the required parameter 'list_id' is set
        if "list_id" not in params or params["list_id"] is None:
            raise ValueError(
                "Missing the required parameter `list_id` when calling `post_manga_id_list_list_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501
        if "list_id" in params:
            path_params["listId"] = params["list_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/list/{listId}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Response",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_manga_id_status(self, id, **kwargs):  # noqa: E501
        """Update Manga reading status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_id_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param UpdateMangaStatus body: Using a `null` value in `status` field will remove the Manga reading status. The size of the body is limited to 2KB.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_manga_id_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_manga_id_status_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def post_manga_id_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Manga reading status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_manga_id_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param UpdateMangaStatus body: Using a `null` value in `status` field will remove the Manga reading status. The size of the body is limited to 2KB.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_manga_id_status" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `post_manga_id_status`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}/status",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Response",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_manga_id(self, id, **kwargs):  # noqa: E501
        """Update Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_manga_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param MangaEdit body: The size of the body is limited to 16KB.
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_manga_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_manga_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def put_manga_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Manga  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_manga_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Manga ID (required)
        :param MangaEdit body: The size of the body is limited to 16KB.
        :return: MangaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_manga_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `put_manga_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["Bearer"]  # noqa: E501

        return self.api_client.call_api(
            "/manga/{id}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MangaResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
