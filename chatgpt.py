import pickle

import openai

# 设置 OpenAI API 的密钥
openai.api_key = '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'


def loadHistoryMessage(name):
    try:
        with open(r'database\%s' % (name), 'rb') as f:
            messages = pickle.load(f)

    except:
        messages = []
    return messages


def updateHistoryMessage(name, messages):
    with open(r'database\%s' % (name), 'wb') as f:
        pickle.dump(messages, f)


def ChatGPT(content, flag=1, name=None):
    MAXMESSAGE = 5  # 设置chatgpt记录的最大聊天消息数量为 5
    if flag:
        messages = loadHistoryMessage(name)  # 加载历史聊天记录

        # 将用户发送的消息加入到 messages 中
        messages.append({'role': 'user', 'content': content})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages[-MAXMESSAGE * 2 + 1:]
        )
        # 获取 AI 回复的内容
        ai_response = completion.choices[0].message['content']
        # 将 AI 回复的消息加入到 messages 中
        messages.append({'role': 'assistant', 'content': ai_response})
        # 更新历史聊天记录
        updateHistoryMessage(name, messages[-MAXMESSAGE * 2:])
    else:
        messages = []
        messages.append({'role': 'user', 'content': content})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ai_response = completion.choices[0].message['content']
        messages.append({'role': 'assistant', 'content': ai_response})
        updateHistoryMessage(name, messages)
    return ai_response  # 返回 AI 的回复
