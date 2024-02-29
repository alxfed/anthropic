# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from anthropic import AI_PROMPT, HUMAN_PROMPT, AnthropicBedrock

# Note: this assumes you have AWS credentials configured.
#
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
client = AnthropicBedrock()

print("------ standard response ------")
completion = client.completions.create(
    model="anthropic.claude-instant-v1",
    prompt=f"{HUMAN_PROMPT} hey!{AI_PROMPT}",
    stop_sequences=[HUMAN_PROMPT],
    max_tokens_to_sample=10,
    temperature=0.5,
    top_k=250,
    top_p=0.5,
)
print(completion.completion)


question = """
Can we change human nature?
"""

print("------ streamed response ------")
stream = client.completions.create(
    model="anthropic.claude-instant-v1",
    prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
    max_tokens_to_sample=10,
    stream=True,
)
for item in stream:
    print(item.completion, end="")
print()