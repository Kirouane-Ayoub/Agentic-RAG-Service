from llama_index.core.tools import QueryEngineTool, ToolMetadata
from engines import first_engine, second_engine

query_engine_tools = [
    QueryEngineTool(
        query_engine=first_engine,
        metadata=ToolMetadata(
            name="moa_tool",
            description=(
                "Provides information about LLMs and Mixture-of-Agents (MoA)"
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=second_engine,
        metadata=ToolMetadata(
            name="self_rag_tool",
            description=(
                "Provides information about Retrieval-Augmented Generation (RAG) and Self-RAG"
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
]
