#Rodar o site: python -m uvicorn main:app --reload
# Fastapi
# pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
#Para salvar o CSS em pastas Separadas
from fastapi.staticfiles import StaticFiles

#Rodar o servidor: 
app = FastAPI(title = "Gestão")

#Configurar o diretorio do html
templates = Jinja2Templates(directory = "templates")

#Mapeia a pasta static para servir arquivos (css , img , js)
app.mount("/static" , StaticFiles(directory = "static") , name = "static")

# Abrir/Retornar HTML:
# Rota - endpoint
# Metodo HTTP - GET, POST, PUT , DELETE
# GET = Pegar/listar/Exibir
# POST = Criar/adicionar
# PUT = Atualizar
# DELETE = Deletar
@app.get("/")
def pagina_principal(request: Request):
    return templates.TemplateResponse(
        request, 
        "pagina_principal.html",
        {"request": request}
    )
@app.get("/alunos")
def listar_alunos(request: Request):
    alunos = [
        {"nome":"Messi", "nota": 9},
        {"nome": "olise" , "nota": 11},
        {"nome": "wily willy" , "nota": 2},
    ]
    return templates.TemplateResponse(
        request,
        "alunos.html",
        {"request": request , "alunos" : alunos}



    )