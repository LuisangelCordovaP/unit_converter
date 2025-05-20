from pydantic import BaseModel
from enum import Enum

class CategoryEnum(str, Enum):
    length = 'length'
    weigth = 'weight'
    temperature = 'temperature'

class ConversionRequest(BaseModel):
    category: CategoryEnum
    from_unit : str
    to_unit : str
    value : float

class ConversionResponse(BaseModel):
    result : float