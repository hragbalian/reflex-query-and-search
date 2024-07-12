
from llama_index.llms.openai import OpenAI

openai_chat_model = "gpt-3.5-turbo-0125"

llm = OpenAI(model=openai_chat_model, temperature=.5)


