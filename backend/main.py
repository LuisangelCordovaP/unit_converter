from fastapi import FastAPI
from backend.models import ConversionRequest, ConversionResponse
from backend.services.UnitConverter import UnitConverter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:5173'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post('/convert', response_model=ConversionResponse)
def convert(data: ConversionRequest):
    converter = UnitConverter()
    result = converter.convert(data.category, data.from_unit, data.to_unit, data.value)
    return ConversionResponse(result=result)