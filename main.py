from fastapi import FastAPI
from board_generation import handle_board_generation

app = FastAPI()

@app.get('/generateBoard/{use_openai}/{theme}/{days_until_exam}')
async def root(use_openai: bool, theme: str, days_until_exam: str):
    return handle_board_generation(use_openai, theme, days_until_exam)
