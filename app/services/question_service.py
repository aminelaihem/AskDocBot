import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",  
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="mistralai/mistral-7b-instruct" 
)

template = PromptTemplate(
    input_variables=["question"],
    template="Explique-moi simplement : {question}"
)

def get_answer(question: str) -> str:
    prompt = template.format(question=question)
    
    message = HumanMessage(content=prompt)

    response = llm.invoke([message])

    return response.content
