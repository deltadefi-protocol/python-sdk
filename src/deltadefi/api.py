import json

import requests

from deltadefi.error import ClientError, ServerError
from deltadefi.lib.utils import clean_none_value, encoded_string


class API(object):
    def __init__(self, base_url=None, api_key=None, timeout=None, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
            }
        )

    def send_request(self, http_method, url_path, payload=None):
        if payload is None:
            payload = {}
        payload["X-API-KEY"] = self.api_key
        url = self.base_url + url_path
        params = clean_none_value(
            {
                "url": url,
                "params": self._prepare_params(payload),
                "timeout": self.timeout,
            }
        )
        response = self._dispatch_request(http_method)(**params)
        self._handle_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if len(result) != 0:
            result["data"] = data
            return result

        return data

    def _dispatch_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")

    def _prepare_params(self, params):
        return encoded_string(clean_none_value(params))

    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except json.JSONDecodeError:
                raise ClientError(
                    status_code, None, response.text, response.headers, None
                )
            error_data = None
            if "data" in err:
                error_data = err["data"]
            raise ClientError(
                status_code, err["code"], err["msg"], response.headers, error_data
            )
        raise ServerError(status_code, response.text)
