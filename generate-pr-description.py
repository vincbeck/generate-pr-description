#!/usr/bin/env python3
import argparse

from generate_pr_description.code_diff_puller import pull_code_diff
from generate_pr_description.description_generator import generate_description

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("url", help="the URL of the PR to generate the description for", type=str)
    args = argParser.parse_args()

    code_diff = pull_code_diff(args.url)
    print(f"Generating description for PR {args.url} ...")
    description = generate_description(code_diff)
    print(description)
