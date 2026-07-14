from pydantic import BaseModel

class WeatherArguments(BaseModel):
    city:str

