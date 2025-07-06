"""Minimal HTTP client used for interacting with GitHub without external deps."""

from urllib import request, parse
import json


class Response:
    def __init__(self, status_code: int, data: bytes, headers: dict):
        self.status_code = status_code
        self._data = data
        self.headers = headers

    def json(self):
        return json.loads(self._data.decode())

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise RuntimeError(f"HTTP status {self.status_code}")


def _make_request(method: str, url: str, *, headers: dict | None = None, params: dict | None = None, json_body: dict | None = None):
    if params:
        url += "?" + parse.urlencode(params)
    data = None
    if json_body is not None:
        data = json.dumps(json_body).encode()
        if headers is None:
            headers = {}
        headers.setdefault("Content-Type", "application/json")

    req = request.Request(url, data=data, headers=headers or {}, method=method)
    with request.urlopen(req) as resp:
        return Response(resp.status, resp.read(), dict(resp.headers))


def get(url: str, headers: dict | None = None, params: dict | None = None):
    return _make_request("GET", url, headers=headers, params=params)


def post(url: str, json: dict | None = None, headers: dict | None = None):
    return _make_request("POST", url, headers=headers, json_body=json)


def patch(url: str, json: dict | None = None, headers: dict | None = None):
    return _make_request("PATCH", url, headers=headers, json_body=json)
