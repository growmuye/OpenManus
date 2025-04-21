# Create server parameters for stdio connection
import toml
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

with open('/Users/gmy/Documents/experimentProjects/OpenManus/config/config.toml', 'r') as file:
    data = toml.load(file)

model = ChatOpenAI(
    model=data["llm"]["model"],
    base_url=data["llm"]["base_url"],
    api_key=data["llm"]["api_key"],
    temperature=data["llm"]["temperature"],
    top_p=data["llm"]["top_p"],
)


server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["/Users/gmy/Documents/experimentProjects/OpenManus/langchain_mcp_server.py"],
)


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
            print(agent_response)

# 调用异步函数
import asyncio
asyncio.run(main())