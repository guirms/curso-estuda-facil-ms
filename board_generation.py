from openai import OpenAI
from dotenv import load_dotenv
import json
import os

def handle_board_generation(use_openai: bool, theme: str, days_until_exam: str) -> str:
    if (use_openai):
        return generate_openai_board(theme, days_until_exam)
    else:
        return generate_local_board()

def generate_local_board() -> str:
    return [
        {
            'day': 1,
            'contents': [
                {
                    'name': 'Causas da Primeira Guerra Mundial',
                    'description': 'Exploração das razões que levaram ao conflito',
                    'studyTime': 60
                }
            ]
        },
        {
            'day': 2,
            'contents': [
                {
                    'name': 'Desenvolvimento da Primeira Guerra Mundial',
                    'description': 'Análise dos principais eventos durante o conflito',
                    'studyTime': 150
                }
            ]
        },
        {
            'day': 3,
            'contents': [
                {
                    'name': 'Tratados e Consequências da Primeira Guerra Mundial',
                    'description': 'Estudo dos acordos pós-conflito e impacto global',
                    'studyTime': 180
                }
            ]
        },
        {
            'day': 4,
            'contents': [
                {
                    'name': 'Impacto Social e Econômico da Primeira Guerra Mundial',
                    'description': 'Avaliação dos efeitos no cotidiano e na economia mundial',
                    'studyTime': 90
                }
            ]
        },
        {
            'day': 5,
            'contents': [
                {
                    'name': 'Legado da Primeira Guerra Mundial',
                    'description': 'Reflexão sobre a influência duradoura do conflito',
                    'studyTime': 150
                }
            ]
        }
    ]

def generate_openai_board(theme: str, days_until_exam: str) -> str:
    load_dotenv()

    client = OpenAI(
        api_key = os.getenv('OPENAI_API_KEY')
    )

    example_json = '''{
    'data': [
        {
            'day': Number,
            'contents': [
                {
                    'name': String,
                    'description': String,
                    'studyTime': Number
                }
            ]
        }
    ]
    }'''

    prompt = f'''Provide a valid JSON response.
    Provide a list of the main daily study contents for my exam and the amount of study time I should dedicate to each of these topics.
    The quantity of contents should be sufficient to get ready for the exam.
    Provide a list of objects called with the current day and another list of objects with the contents and their respective descriptions, study times and subtasks.
    The description must be no more than 20 words.
    The Study times should be in minutes.
    Return all names and descriptions in portuguese.
    The theme input will also be in portuguese.
    The main theme of my exam is: {theme}. I want to study it in {days_until_exam} days'''

    chat_completion = client.chat.completions.create(
        model='gpt-3.5-turbo-0125',
        response_format={'type':'json_object'},
        messages=[
            {'role':'system','content':'Provide output in valid JSON. The data schema should follow this schema: '+json.dumps(example_json)},
            {'role':'user','content':prompt}
        ]
    )

    finish_reason = chat_completion.choices[0].finish_reason
    
    while (finish_reason != 'stop'):
        generate_openai_board(theme, days_until_exam)
        
    json_data = chat_completion.choices[0].message.content
    json_data = json.loads(json_data)['data']

    return json_data
