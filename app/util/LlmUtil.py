import os

import toml
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

# 读取 TOML 文件
with open('/Users/gmy/Documents/experimentProjects/OpenManus/config/config.toml', 'r') as file:
    data = toml.load(file)

os.environ["AZURE_OPENAI_API_KEY"] = data["llm"]["api_key"]

llm = AzureChatOpenAI(
    azure_endpoint=data["llm"]["endpoint"],
    azure_deployment=data["llm"]["deployment"],
    openai_api_version=data["llm"]["api_version"],
)

def chat(tag_start,tag_end,chatLLm, chat_history):
    while True:
        user_input = input(f"{tag_start}: ".replace("平台","用户"))
        if user_input.lower() == "exit":
            print("感谢使用，再见！")
            break
        chat_history.append(HumanMessage(user_input))
        response = chatLLm.invoke(chat_history)
        chat_history.append(response)
        if response.content:
            print(f"{tag_start}: {response.content}\n{tag_end}")