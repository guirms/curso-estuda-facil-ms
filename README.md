# Estuda Fácil Microsservciço

![GitHub language count](https://img.shields.io/github/languages/count/guirms/curso-estuda-facil-ms?style=for-the-badge&logo=GitHub&logoColor=%23FFFF)
![GitHub contributors](https://img.shields.io/github/contributors/guirms/curso-estuda-facil-ms?style=for-the-badge&logo=GitHub&logoColor=%23FFFF&color=%23087ABB)
![GitHub forks](https://img.shields.io/github/forks/guirms/curso-estuda-facil-ms?style=for-the-badge&logo=GitHub&logoColor=%23FFFF&color=%23087ABB)

Uma API RESTful utilizada como microsserviço para a [API do Estuda Fácil](https://github.com/guirms/curso-estuda-facil-api) e projetada para criar planos de estudo personalizados para avaliações, utilizando a inteligência artificial da [OpenAI](https://openai.com/index/openai-api/).

# Principais tecnologias utilizadas
<img src="https://github.com/user-attachments/assets/7a7825a8-a399-4bb2-9aff-427a2abbb5e0" alt="drawing" width="50"/>
<img src="https://github.com/user-attachments/assets/7acd468d-1af0-4ff9-bf20-0e813a79d452" alt="drawing" width="50"/>
<img src="https://github.com/user-attachments/assets/7b343d58-0328-4cb6-bbea-c1162c1322cc" alt="drawing" width="50"/>
<img src="https://github.com/user-attachments/assets/a1feeea8-f8e4-4fd0-9cc3-7906b8c9b85a" alt="drawing" width="50"/>

## Pré-requisitos

Para executar o projeto com sucesso, você deve atender os seguintes requisitos:

- [Python](https://www.python.org/downloads/) (A versão utilizada no projeto é 3.11.3)

## Criando instância da API

Para criar uma instância da API localmente, siga o passo a passo:

- Clone o projeto na sua pasta de preferência através do comando `git clone https://github.com/guirms/curso-estuda-facil-ms.git`
- No terminal, dentro da pasta raíz do projeto, execute o comando `pip install -r ./requirements.txt`
- Por fim, crie a instância da API através do comando `fastapi run main.py --port 8000`

## Execute a aplicação através do Docker

Esta API está "dockerizada" e sua imagem está hospedada no [DockerHub](https://hub.docker.com).
Caso você deseje criar um container Docker a partir dessa imagem, siga os seguintes passos:

- Caso ainda não tenha o Docker instalado, siga as instruções para instalá-lo [aqui](https://docs.docker.com/get-started/get-docker/)
- No terminal, execute o seguinte comando `docker run -d -p 8000:8080 guirms/estuda-ai-ms`

## Considerações

Desenvolvi este projeto para o lançamento do meu curso .NET FOCADO NO MERCADO DE TRABALHO. Coloquei em prática diversos conceitos adquiridos durante meus cinco anos de experiência na área e busquei focar em construir uma solução escalável tanto conceitual quanto tecnicamente. Espero que todos os alunos tenham tido uma boa experiência durante o curso assim como eu tive durante o seu planejamento e desenvolvimento. Agradeço a todos os alunos e gostaria de ressaltar que é uma satisfação indescritível poder passar meu conhecimento e experiência adiante e espero que nos vejamos em breve em novos desafios (novidades por aí...😉).
