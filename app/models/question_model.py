from pydantic import BaseModel

# Requête reçue : l’utilisateur pose une question
class QuestionRequest(BaseModel):
    question: str

# Réponse renvoyée : l’IA répond à la question
class AnswerResponse(BaseModel):
    answer: str
