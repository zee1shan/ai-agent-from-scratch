from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

TArguments = TypeVar("TArguments", bound=BaseModel)


class BaseTool(Generic[TArguments], ABC):

    name: str
    description: str
    argument_model: type[TArguments]

    def definition(self)->dict:
        return {
            "type":"function",
            "function":{
                "name":self.name,
                "description":self.description,
                "parameters":self.argument_model.model_json_schema()
            }
        }

    def run(self, json: TArguments) -> Any:
        arguments = self.argument_model.model_validate(json)
        return self.execute(arguments)

    @abstractmethod
    def execute(self, arguments: TArguments) -> Any:
        pass