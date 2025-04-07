import os

import toml
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# 读取 TOML 文件
with open('/Users/gmy/Documents/experimentProjects/OpenManus/config/config.toml', 'r') as file:
    data = toml.load(file)

chatLlm = ChatOpenAI(
    model=data["llm"]["model"],
    base_url=data["llm"]["base_url"],
    api_key=data["llm"]["api_key"]
)


def chat(tag_start, tag_end, chatLLm, chat_history):
    while True:
        user_input = input(f"{tag_start}: ".replace("平台", "用户"))
        if user_input.lower() == "exit":
            print("感谢使用，再见！")
            break
        chat_history.append(HumanMessage(user_input))
        response = chatLLm.invoke(chat_history)
        chat_history.append(response)
        if response.content:
            print(f"{tag_start}: {response.content}\n{tag_end}")
