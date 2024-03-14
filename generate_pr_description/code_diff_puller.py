import re

import requests


def pull_code_diff(url: str) -> str:
    if not re.match(r"https://github\.com/.+/(pull|compare)/.+", url, re.IGNORECASE):
        raise ValueError(
            f"The URL specified {url!r} is not valid. The URL must be a Github pull request or a Github compare page.")

    match_pr_page = re.match(r"(https://github\.com/.+/pull/[0-9]+).*", url, re.IGNORECASE)
    match_compare_page = re.match(r"(https://github\.com/.+/compare/[^/]+).*", url, re.IGNORECASE)

    if match_pr_page:
        url = match_pr_page.group(1)
    elif match_compare_page:
        url = match_compare_page.group(1)

    # Append .patch the Github URLs to download the code diff
    request = requests.get(f"{url}.patch")
    return request.content.decode("utf-8")
