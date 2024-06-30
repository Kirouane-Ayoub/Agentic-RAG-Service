import os

import settings
from dotenv import load_dotenv
from llama_index.core import ServiceContext, Settings
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.llms.anthropic import Anthropic

load_dotenv()
llm = Anthropic(model=settings.ANTHROPIC_LLM_MODEL)

# with input_typ='search_query'
embed_model = CohereEmbedding(
    model_name=settings.EMBED_MODEL_NAME,
    input_type="search_query",
    api_key=os.environ["CO_API_KEY"],
)
Settings.embed_model = embed_model
Settings.llm = llm

# Create the service context with the cohere model for generation and embedding model
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
