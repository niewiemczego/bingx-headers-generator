import time
import uuid
from hashlib import sha256
from typing import Any


class BingXHeadersGenerator:
    _DEFAULT_BEGINNING_VALUE = "95d65c73dc5c4370ae9018fb7f2eab69"
    _DEFAULT_PLATFORM_ID = "30"

    def __init__(self, app_version: str, user_id: str, api_identity: str, default_page_size: str = "10") -> None:
        self.app_version = app_version
        self.user_id = user_id
        self.api_identity = api_identity
        self.default_page_size = default_page_size

    def generate_headers(self, base_url: str) -> dict[str, Any]:
        """
        The `generate_headers` function generates a dictionary of headers for making API requests, including
        app version, app ID, device ID, timestamp, and trace ID.

        :param base_url: The `base_url` parameter is a string that represents the base URL of the API
        endpoint. It is used to determine the specific logic for generating the headers based on the value
        of `base_url`
        :return: a dictionary containing various headers for an API request.
        """
        _timestamp = str(int(time.time() * 1000))
        _trace_id, _device_id = str(uuid.uuid4()), str(uuid.uuid4())

        if self.api_identity != "0" or base_url == "https://bingx.com/api/v3/trader/orders/v3":
            _encryption_content = self._generate_encryption_content(_timestamp, _trace_id, _device_id)
        else:
            _encryption_content = self._generate_encryption_content(_timestamp, _trace_id, _device_id, is_standard=True)

        headers = {
            "app_version": self.app_version,
            "appid": "30004",
            "channel": "official",
            "device_id": _device_id,
            "lang": "en",
            "mainappid": "10009",
            "platformid": self._DEFAULT_PLATFORM_ID,
            "sign": self._generate_sign(_encryption_content),
            "timestamp": _timestamp,
            "timezone": "2",
            "traceid": _trace_id,
        }
        return headers

    def _generate_encryption_content(
        self, timestamp: str, trace_id: str, device_id: str, is_standard: bool = False
    ) -> str:
        """
        The `_generate_encryption_content` function generates an encryption content string using various
        parameters.

        :param timestamp: The timestamp parameter is a string representing the current timestamp. It is used
        to generate a unique value for each encryption content
        :param trace_id: The `trace_id` parameter is a unique identifier that is used to track a specific
        request or transaction. It helps in identifying and tracing the flow of requests across different
        systems or components
        :param device_id: The `device_id` parameter is a string that represents the unique identifier of the
        device being used. It is used in the encryption content generation process
        :param is_standard: The `is_standard` parameter is a boolean flag that indicates whether the
        encryption content should be generated using a standard payload template or a non-standard payload
        template
        :return: the encryption content, which is a string.
        """
        payload_template = (
            '{"pageId":"0","pageSize":"default_page_size","trader":"user_id"}'
            if is_standard
            else '{"apiIdentity":"api_identity","copyTradeLabelType":"1","pageId":"0","pageSize":"default_page_size","uid":"user_id"}'
        )
        payload = (
            payload_template.replace("user_id", self.user_id)
            .replace("default_page_size", self.default_page_size)
            .replace("api_identity", self.api_identity)
        )

        encryption_content = "".join(
            [
                self._DEFAULT_BEGINNING_VALUE,
                timestamp,
                trace_id,
                device_id,
                self._DEFAULT_PLATFORM_ID,
                self.app_version,
                payload,
            ]
        )
        return encryption_content

    def _generate_sign(self, encryption_content: str) -> str:
        """
        The function `_generate_sign` takes a string as input, encodes it using UTF-8, computes the SHA256
        hash, and returns the hexadecimal representation of the hash in uppercase.
        """
        return sha256(encryption_content.encode("utf-8")).hexdigest().upper()
