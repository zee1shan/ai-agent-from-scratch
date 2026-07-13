from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    api_key:str
    model:str

settings=Settings(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL")
)