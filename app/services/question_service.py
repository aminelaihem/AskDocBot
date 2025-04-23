import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate(
    input_variables=["question"],
    template="Explique-moi simplement : {question}"
)

def get_answer(question: str) -> str:
    prompt = template.format(question=question)
    return llm(prompt)
