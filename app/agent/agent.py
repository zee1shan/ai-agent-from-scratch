from app.tools.base_tool import BaseTool
from groq import Groq
import json

class Agent:

    def __init__(self,tools:list[BaseTool],llm:Groq,model:str):
        self.tools={tool.name:tool for tool in tools}
        self.llm=llm
        self.model=model
    
    def get_definitions(self):
        return  [tool.definition() for tool in self.tools.values()]
    
    def chat(self,message:str):
        tools=self.get_definitions()
        response=self.llm.chat.completions.create(
            messages=[{"role":"user","content":message}],
            tools=tools,
            model=self.model
        )

        message = response.choices[0].message

        if message.tool_calls:
            tool_call = message.tool_calls[0]

            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments
            j=json.loads(arguments)
            tool = self.tools[tool_name]

            result = tool.run(json=j)
        print(result)
    