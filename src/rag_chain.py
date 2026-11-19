from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

PROMPT = ChatPromptTemplate.from_template(
    "Answer the question using only the context below. "
    "If the answer is not in the context, say you don't know.\n\n"
    "Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
)


def _format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_qa_chain(retriever, model_name="phi3"):
    llm = OllamaLLM(model=model_name)

    chain = (
        {"context": retriever | _format_docs, "question": RunnablePassthrough()}
        | PROMPT
        | llm
        | StrOutputParser()
    )
    return chain
