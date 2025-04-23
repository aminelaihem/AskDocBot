from fastapi import APIRouter
from app.models.question_model import QuestionRequest, AnswerResponse
from app.services.question_service import get_answer

router = APIRouter(tags=["AskDocBot"])

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    answer = get_answer(request.question)
    return {"answer": answer}
