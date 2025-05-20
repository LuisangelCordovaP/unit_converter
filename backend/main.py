from fastapi import FastAPI
from backend.models import ConversionRequest

app = FastAPI()


@app.post('/convert')
def convert(req: ConversionRequest):
    return req