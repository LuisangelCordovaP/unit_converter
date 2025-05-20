from fastapi import FastAPI
from backend.models import ConversionRequest, ConversionResponse
from backend.services.UnitConverter import UnitConverter

app = FastAPI()


@app.post('/convert', response_model=ConversionResponse)
def convert(data: ConversionRequest):
    converter = UnitConverter()
    result = converter.convert(data.category, data.from_unit, data.to_unit, data.value)
    return ConversionResponse(result=result)