from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

TArguments = TypeVar("TArguments", bound=BaseModel)


class BaseTool(Generic[TArguments], ABC):

    name: str
    description: str
    argument_model: type[TArguments]

    def run(self, json: dict[str, Any]) -> Any:
        arguments = self.argument_model.model_validate(json)
        return self.execute(arguments)

    @abstractmethod
    def execute(self, arguments: TArguments) -> Any:
        pass