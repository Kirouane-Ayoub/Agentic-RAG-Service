from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)
from models import service_context

docs_1 = SimpleDirectoryReader(input_dir="src/source1").load_data()
docs_2 = SimpleDirectoryReader(input_dir="src/source2").load_data()

# build index
first_index = VectorStoreIndex.from_documents(docs_1, service_context=service_context)
second_index = VectorStoreIndex.from_documents(docs_2, service_context=service_context)


# persist index
# first_index.storage_context.persist(persist_dir="first_index")
# second_index.storage_context.persist(persist_dir="second_index")

first_engine = first_index.as_query_engine(similarity_top_k=3)
second_engine = second_index.as_query_engine(similarity_top_k=3)


# result1 = first_engine.query("hello")
# result2 = second_engine.query("hello")
# print(result1)
# print(result2)
