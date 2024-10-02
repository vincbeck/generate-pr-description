import json

import boto3

BEDROCK_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"


def generate_description(code_diff: str) -> str:
    """
    Generate a description for a given code diff.

    :param code_diff: the code diff
    """
    client = boto3.client('bedrock-runtime')
    body = {
        "messages": [{
            "role": "user",
            "content": [{
                "type": "text",
                "text": f"Can you summarize the code diff below:\n\n{code_diff}"
            }]
        }],
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2000,
    }

    response = client.invoke_model(
        body=str.encode(json.dumps(body)),
        modelId=BEDROCK_MODEL_ID
    )

    body_json = json.loads(response['body'].read().decode('utf-8'))
    return body_json["content"][0]["text"]
