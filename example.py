from langchain.cache import SQLiteCache
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain.globals import set_llm_cache
from langchain_openai import OpenAI
import os
import time
import tekmetric_api_spec

# Project: "TekmetricAPI"
# APIKey: "SandboxKey"
#os.environ["OPENAI_API_KEY"] = "sk-proj-..."

# Tekmetric sandbox api key for testing
os.environ["TEKMETRIC_SANDBOX_BEARER_TOKEN"] = "dd824dda-c02c-478a-aa84-cd9fdb217c15"
headers = {"Authorization": f"Bearer {os.environ['TEKMETRIC_SANDBOX_BEARER_TOKEN']}"}

# Set LLM memory cache as SQLite database rather than memory
set_llm_cache(SQLiteCache(database_path=".langchain.db"))

llm = OpenAI(temperature=0)
chain = APIChain.from_llm_and_api_docs(
    llm,
    tekmetric_api_spec.API_SPEC_YAML,
    headers=headers,
    verbose=True,
    limit_to_domains=["https://sandbox.tekmetric.com/api/v1"],
)

t0 = time.time()
chain.invoke("List all the customers from shop 1 that are a business")
t1 = time.time()
print(t1-t0)

t0 = time.time()
chain.invoke("List all the customers from shop 1 that are a business")
t1 = time.time()
print(t1-t0)
