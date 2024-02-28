# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    # api_key="my_api_key",
)


completion = client.completions.create(
    model="claude-instant-1.2",
    max_tokens_to_sample=10,
    prompt=f"\n\nHuman:I am Alex\n\nAssistant:",
    stop_sequences=['\n\nHuman:', '\n\nAssistant:'],
    temperature=0.5,
    top_k=250,
    top_p=0.5,
)
print(completion.completion)