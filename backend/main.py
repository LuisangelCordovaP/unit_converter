from fastapi import FastAPI
from backend.models import ConvertionRequest

app = FastAPI()


@app.post('/convert')
def convert(req: ConvertionRequest):
    return req