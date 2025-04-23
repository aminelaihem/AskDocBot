import os
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", 
    temperature=0
)


template = PromptTemplate(
    input_variables=["question"],
    template="Explique-moi simplement : {question}"
)

def get_answer(question: str) -> str:
    prompt = template.format(question=question)
    return llm(prompt)
