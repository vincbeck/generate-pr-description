import json

import boto3

BEDROCK_MODEL_ID = "anthropic.claude-v2:1"


def generate_description(code_diff: str):
    client = boto3.client('bedrock-runtime')
    body = {
        "prompt": f"Human: Can you summarize the code diff below:{code_diff}\nAssistant:",
        "max_tokens_to_sample": 300,
    }
    response = client.invoke_model(
        body=str.encode(json.dumps(body)),
        modelId=BEDROCK_MODEL_ID
    )
    return response['body'].read().decode('utf-8')
