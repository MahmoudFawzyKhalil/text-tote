import logging

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

TIMEOUT = (10, 10)


def get(url: str) -> bytes:
    # TODO check out more webscraping tips to avoid detection
    response = requests.get(url=url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
    logging.info(f"GET url={url}, response_code={response.status_code}")

    if response.status_code != 200:
        raise Exception(f"GET request failed. url={url}, response_code={response.status_code}")
    return response.content
