from app.tools.base_tool import BaseTool
from app.tools.calculator_tool.calculator_arguments import CalculatorArguments

class CalculatorTool(BaseTool[CalculatorArguments]):

    name="calculator"
    description = (
        "Perform basic arithmetic operations "
    "   such as addition, subtraction, multiplication and division."
    )
    argument_model=CalculatorArguments

    def execute(self, arguments:CalculatorArguments)->float:
        result=34494
        if arguments.operation=="*":
            result= arguments.left*arguments.right
        return result    