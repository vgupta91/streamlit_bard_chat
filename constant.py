import re

remove_lines = ["I'm a language model and don't have the capacity to help with that.",
                "I'm unable to help",
                "As a language model, I'm not able to assist you with that.",
                "I'm just a language model, so I can't help you with that.",
                # "Response Error: ",
                "I can't assist you with that, as I'm only a language model and don't have the capacity to understand "
                "and respond.",
                "I'm not programmed to assist with that.",
                "I'm a text-based AI",
                "I'm not able to help with that, as I'm only a language model.",
                "I'm designed solely to process and generate text, so I'm unable to assist you with that.",
                "I can't summarize the website in 5 lines because it does not exist.",
                "I cannot summarize the website",
                'I cannot access the website you mentioned. It says "ERR_CONNECTION_TIMED_OUT".',
                "I don't have enough information to do that.",
                "I am still working to learn more languages",
                "I am an LLM trained to respond in a subset of languages at this time, so I can't assist you with that",
                "I'm still learning languages, so at the moment I can't help you with this request",
                "I do not have enough information about that person to help with your request.",
                "I don't have any information"
                ]

replace_words = [r'Sure. ', r'Sure, ', r'Sure. In 2 lines, ', r'In two lines, ', r'In 2 lines, ',
                 r'I hope this summary is helpful!']


def clear_summarized_text(text1):
    text1 = re.sub('Sure.*?\n', '', text1)
    text1 = re.sub('here.*?\n', '', text1)
    text1 = re.sub('Here.*?\n', '', text1)
    text1 = re.sub('I hope this.*?questions.', '', text1)
    for word in replace_words:
        if re.search(word, text1) is not None:
            text1 = text1.replace(re.search(word, text1).group(), '')

    for line in remove_lines:
        if line in text1:
            text1 = ''
    return text1
