from langchain_openai import ChatOpenAI 
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def get_answer(question: str) -> str:

    llm = ChatOpenAI(
        temperature=0.7,  
        model_name="gpt-3.5-turbo"  
    )

    prompt = PromptTemplate(
        input_variables=["question"],
        template="Réponds clairement à cette question : {question}"
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run({"question": question})
    return response
