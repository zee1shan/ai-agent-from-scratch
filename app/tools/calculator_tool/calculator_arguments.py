from pydantic import BaseModel
from typing import Literal

CalculatorOperation=Literal[
    "+",
    "-",
    "*",
    "/"
]

class CalculatorArguments(BaseModel):
    left:float
    right:float
    operation:CalculatorOperation

