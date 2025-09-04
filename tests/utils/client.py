import httpx
import json
import random
from typing import Any, Optional, Union

from gr4vy import Gr4vy
from gr4vy.httpclient import HttpClient  # Using the synchronous client for this example


class JsonInterceptorClient(HttpClient):
    """
    A custom client that wraps an httpx.Client to intercept and modify
    JSON responses before they are processed by the SDK.

    This class conforms to the `HttpClient` protocol required by the Gr4vy SDK.
    """

    _client: httpx.Client

    def __init__(self, client: httpx.Client):
        """
        Initializes the interceptor with an actual httpx client instance
        that will be used to make the real network requests.
        """
        self._client = client

    def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        """
        This method is called by the SDK to execute an HTTP request.
        This is where we intercept the response.
        """
        # 1. Let the wrapped client handle the actual network request.
        original_response = self._client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

        # 2. Check if the response is JSON. If not, return it unmodified.
        content_type = original_response.headers.get("content-type", "")
        if "application/json" not in content_type:
            return original_response

        try:
            # 3. Read the response content. This consumes the stream, so we
            # must build a new response object later.
            original_response.read()
            data = json.loads(original_response.content)

            # 4. Add a random property to the JSON object.
            random_key = f"unexpected_field_{random.randint(0, 999)}"
            data[random_key] = "this is an injected test value"
            print(f"Intercepted response and added key: {random_key}")

            # 5. Re-encode the modified data to bytes.
            modified_content = json.dumps(data).encode("utf-8")
            
            # 6. Create a new httpx.Response object with the modified content.
            # We pass through the original status code, headers, and request object
            # to ensure the SDK can process it just like a real response.
            # httpx will automatically update Content-Length.
            modified_response = httpx.Response(
                status_code=original_response.status_code,
                headers=original_response.headers,
                content=modified_content,
                request=request,
            )
            return modified_response

        except json.JSONDecodeError:
            # If JSON parsing fails, we must still return a valid response.
            # Since we already consumed the stream with .read(), we reconstruct
            # the original response from its stored content.
            return httpx.Response(
                status_code=original_response.status_code,
                headers=original_response.headers,
                content=original_response.content,
                request=request,
            )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        """
        Delegates request building to the wrapped client. This is required
        to fully satisfy the HttpClient protocol.
        """
        return self._client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

