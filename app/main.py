from app.tools.calculator_tool.calculator_tool import CalculatorTool
from app.tools.weather_tool.weather_tool import Weathertool
from app.agent.agent import Agent
from app.config.config import settings
from groq import Groq
def main():
    print("main laoder")
    tools = [CalculatorTool(),Weathertool()]
    llm=Groq(api_key=settings.api_key)
    model=settings.model
    agent=Agent(tools=tools,llm=llm,model=model)
    while(True):
        text=input()
        if text=='exit':
            break
        agent.chat(question=text)


if __name__ == '__main__':
    main()