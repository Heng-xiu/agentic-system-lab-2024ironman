from fastapi import APIRouter
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from app.core.config import settings

router = APIRouter()

model = ChatOpenAI(api_key=settings.OPENAI_API_KEY['key'])
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
custom_chain = prompt | model

add_routes(
    router,
    custom_chain,
    path="/joke",
    # playground_type="default",
)