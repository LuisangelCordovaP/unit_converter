from pydantic import BaseModel

class ConvertionRequest(BaseModel):
    category: str
    from_unit : str
    to_unit : str
    value : float