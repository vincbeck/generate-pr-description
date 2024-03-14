import json
import logging
import os

from generate_pr_description.code_diff_puller import pull_code_diff
from generate_pr_description.description_generator import generate_description

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES: %s', json.dumps(dict(**os.environ)))
    logger.info('## EVENT: %s', json.dumps(event))

    url = None
    if "url" in event:
        # When executing directly the lambda
        url = event["url"]
    if "queryStringParameters" in event and "url" in event["queryStringParameters"]:
        # When executing the lambda through its public URL
        url = event["queryStringParameters"]["url"]

    if not url:
        raise ValueError("'url' is required")

    code_diff = pull_code_diff(url)
    logger.info("Generating description for PR %s ...", url)
    description = generate_description(code_diff)
    logger.info("Description: %s", description)

    return description
