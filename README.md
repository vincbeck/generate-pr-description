# generate-pr-description

Generate a PR description for you.

## Requirements

It uses [Amazon Bedrock](https://aws.amazon.com/bedrock/) to generate the description.
You must have an AWS account and have permissions to invoke models in Amazon Bedrock.
This script uses the model `anthropic.claude-v2:1` so you need to have access to this model in your account.

## Getting started
- Download the code: `git clone git@github.com:vincbeck/generate-pr-description.git`
- Create virtual environment: `pyenv virtualenv 3.10 generate-pr-description`
- Install all dependencies: `pip install -r requirements.txt`
- Run the script:
  - Generate a description for an existing PR: `./generate-pr-description.py https://github.com/<respository>/pull/<pr_number>`.
  Example: `./generate-pr-description.py https://github.com/apache/airflow/pull/37915`
  - Generate a description when creating a PR: `./generate-pr-description.py https://github.com/<respository>/compare/main...<branch>`.
  Example: `./generate-pr-description.py https://github.com/apache/airflow/compare/main...aws-mwaa:upstream-to-airflow:vincbeck/test`