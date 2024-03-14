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
    logger.info('## CONTEXT: %s', json.dumps(context))

    if "url" not in event:
        return {"statusCode": 400, "body": "url is required"}

    code_diff = pull_code_diff(event["url"])
    logger.info("Generating description for PR %s ...", event["url"])
    description = generate_description(code_diff)
    logger.info("Description: %s", description)

    return {"statusCode": 200, "body": "description"}
