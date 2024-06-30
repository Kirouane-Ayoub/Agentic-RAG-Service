import asyncio

import nest_asyncio
from llama_agents import (
    AgentOrchestrator,
    AgentService,
    ControlPlaneServer,
    LocalLauncher,
    MetaServiceTool,
    SimpleMessageQueue,
    ToolService,
)
from llama_index.core.agent import FunctionCallingAgentWorker
from models import llm
from tools import query_engine_tools

nest_asyncio.apply()


# Function to verify that each tool has a valid name
def validate_tools(tools):
    for tool in tools:
        if not hasattr(tool.metadata, "name") or not tool.metadata.name:
            raise ValueError(f"Tool {tool} does not have a valid name")


validate_tools(query_engine_tools)

# Create our multi-agent framework components
message_queue = SimpleMessageQueue()

control_plane = ControlPlaneServer(
    message_queue=message_queue,
    orchestrator=AgentOrchestrator(llm=llm),
)

# Define Tool Service
tool_service = ToolService(
    message_queue=message_queue,
    tools=query_engine_tools,
    running=True,
    step_interval=0.5,
)


# Asynchronous function to initialize meta-tools
async def init_meta_tools():
    return [
        await MetaServiceTool.from_tool_service(
            t.metadata.name,
            message_queue=message_queue,
            tool_service=tool_service,
        )
        for t in query_engine_tools
    ]


# Main asynchronous function to run everything
async def main():
    try:
        # Initialize meta-tools
        meta_tools = await init_meta_tools()

        # Define Agent and agent service
        worker = FunctionCallingAgentWorker.from_tools(
            meta_tools,
            llm=llm,
        )

        agent = worker.as_agent()
        agent_server = AgentService(
            agent=agent,
            message_queue=message_queue,
            description="Used to answer questions about LLMs and Mixture-of-Agents (MoA) and Rag system.",
            service_name="special_agent",
        )
        # Define Launcher
        local_launcher = LocalLauncher(
            [agent_server, tool_service],
            control_plane,
            message_queue,
        )

        # Define a query string and send a query
        while True:
            query_str = input(">> ")
            result = local_launcher.launch_single(query_str)
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the main function
asyncio.run(main())
