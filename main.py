from fastapi import FastAPI, Request
from .service.model import Service
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/create_service/")
async def createService():
    return FileResponse("ServiceCreate.html")


@app.get("services/")
async def services(request: Request):
    return templates.TemplateResponse('ServiceList.html')
    