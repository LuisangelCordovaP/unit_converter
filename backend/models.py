from pydantic import BaseModel
from enum import Enum

class CategoryEnum(str, Enum):
    length = 'length'
    weigth = 'weight'
    temperature = 'temperature'

class ConvertionRequest(BaseModel):
    category: CategoryEnum
    from_unit : str
    to_unit : str
    value : float