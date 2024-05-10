from pydantic import BaseModel

class Parameters(BaseModel):
    GDP_In_Billion_USD : float
    Per_Capita_in_USD : float
    Percentage_Growth : float

