import matplotlib.image as mpimg
# 毕竟graph，可以使用图形工具绘制chatbot graph
# (mac版，win下如果不好用请用AI自行改写)
import matplotlib.pyplot as plt
import toml
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from app.util.lxy_search_util import lxy_main_search

with open('/Users/gmy/Documents/experimentProjects/OpenManus/config/config.toml', 'r') as file:
    data = toml.load(file)

model = ChatOpenAI(
    model=data["llm"]["model"],
    base_url=data["llm"]["base_url"],
    api_key=data["llm"]["api_key"],
)


@tool
def analyze_resume_database_for_recruitment(
        keyword: str = None,
        salarylow: str = None,
        salaryhigh: str = None,
        agelow: str = None,
        agehigh: str = None,
        jobTitle: str = None,
        workyearslow: str = None,
        workyearshigh: str = None,
        city: list = None,
        eduLevel: list = None,
        industry: list = None,
        sex: list = None) -> str:
    """根据用户的招聘需求，分析简历库中满足需求的简历分布状况：本次搜索简历的条件、简历库中满足条件的简历总数、本次搜索到的简历样例。"""
    return lxy_main_search(keyword, salarylow, salaryhigh, agelow, agehigh, jobTitle, workyearslow, workyearshigh, city,
                           eduLevel, industry, sex)


tools = [analyze_resume_database_for_recruitment]

graph = create_react_agent(model, tools=tools)

# try:
#     mermaid_code = graph.get_graph().draw_mermaid_png()
#     with open("graph.png", "wb") as f:
#         f.write(mermaid_code)
#     img = mpimg.imread("graph.png")
#     plt.imshow(img)
#     plt.axis('off')
#     plt.show()
# except Exception as e:
#     print(f"An error occurred: {e}")


def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


file_path = "../doc/招聘JD.txt"
with open(file_path, "r", encoding="utf-8") as file:
    prompt = file.read().strip()

inputs = {"messages": [("user", prompt)]}
print_stream(graph.stream(inputs, stream_mode="values"))
