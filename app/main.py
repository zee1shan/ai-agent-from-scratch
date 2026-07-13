from app.tools.calculator_tool.calculator_tool import CalculatorTool
from app.agent.agent import Agent
from app.config.config import settings
from groq import Groq
def main():
    print("main laoder")
    tool = CalculatorTool()
    llm=Groq(api_key=settings.api_key)
    model=settings.model


    result = tool.run(json={
    "left": 12,
    "right": 20,
    "operation": "+"
    })

    print(result)
    agent=Agent(tools=[tool],llm=llm,model=model)
    print("agent response -----")
    agent.chat("what is 3 plus 6")


if __name__ == '__main__':
    main()