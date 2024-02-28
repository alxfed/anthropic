# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import anthropic
from PyPDF2 import PdfReader

reader = PdfReader("/home/alxfed/Downloads/Troelstra_Basic_Proof_Theory.pdf")
number_of_pages = len(reader.pages)
text = ''.join([page.extract_text() for page in reader.pages])
print(text[:2155])

CLIENT = anthropic.Client()


def get_completion(client, prompt, max_tokens=3000, model='claude-2'):
    return client.completions.create(
        prompt=prompt, max_tokens_to_sample=max_tokens, model=model
    ).completion


completion = get_completion(CLIENT,
    f"""\n\nHuman: Here is a book: <book>{text}</book>

Please do the following:
1. Summarize the book;
2. Write a critique of it. (In <critique> tags.)

Assistant:"""
)
print(completion)

# next - https://github.com/anthropics/anthropic-cookbook/blob/main/long_context/mc_qa.ipynb