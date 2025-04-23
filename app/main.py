from fastapi import FastAPI
from app.routes.question_route import router
import dotenv

dotenv.load_dotenv()

app = FastAPI(title="AskDocBot - Assistant IA Tech")

app.include_router(router, prefix="/api")
