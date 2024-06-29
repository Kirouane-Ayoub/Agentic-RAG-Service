# Agentic RAG Service 

This project leverages the **[🦙 Llama-Agents 🤖](https://github.com/run-llama/llama-agents)** framework to build a sophisticated **multi-agent** system that integrates a **retrieval-augmented generation (RAG)** approach using the **llama-index query engines** and a **powerful LLM** for enhanced information retrieval and processing.

## Overview
This project sets up an llama-agents framework with the following key components:

- **Two Llama-Index Query Engines**: Utilized as tools for the agent to perform advanced document retrieval and question-answering tasks.
- **Agent Services**: Wrap existing `llama-index agents` to handle specific tasks.
- **Tools Service**: Contains **RAG tools** for processing annual reports and other documents.
- **Agentic Orchestrator**: Manages task distribution and result aggregation.

- **LLM**: `claude-3-opus-20240229` by `Anthropic` for advanced language model capabilities.
- **Embedding Model**: `embed-english-v3.0` by `Cohere` for high-quality text embeddings.
- **Query Engines**: Two `llama-index` query engines used as tools for the agent’s RAG tasks.
## How to Use This

To use this project, follow these steps:

1. **Clone the repository and navigate to the project directory**:
   ```sh
   git clone https://github.com/Kirouane-Ayoub/Agentic-RAG-Service.git
   cd Agentic-RAG-Service
   ```

2. **Install the necessary dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Move your data files (pdf, csv, md, etc.) to the `src/source1` folder for the first query engine and the `src/source2` folder for the second query engine**.

4. **Create a `.env` file with the following content**:
   ```
   ANTHROPIC_API_KEY=........
   CO_API_KEY=..........
   ```
5. **Run the project**:

- If you want to run the local agent service (`LocalLauncher`):

    ```
    python src/local_agent.py
    ```
- If you want to run the server agent service (`ServerLauncher`):

    ```
    python src/server_agent.py
    ```
    The easiest way is to use our client and the control plane URL:
    ```python

    from llama_agents import LlamaAgentsClient, AsyncLlamaAgentsClient

    client = LlamaAgentsClient("<control plane URL>")  # i.e. http://127.0.0.1:8001
    task_id = client.create_task("What is the secret fact?")
    # <Wait a few seconds>
    # returns TaskResult or None if not finished
    result = client.get_task_result(task_id)
    ```
    Rather than using a client or raw `curl` requests, you can also use a built-in CLI tool to monitor and interact with your services.
    ```
    llama-agents monitor --control-plane-url http://127.0.0.1:8000
    ```
