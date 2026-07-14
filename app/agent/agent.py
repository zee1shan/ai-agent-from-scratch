from app.tools.base_tool import BaseTool
from groq import Groq
import json

class Agent:


    SYSTEM_PROMPT = """
    You are an AI assistant.

    Rules:

    - Always use the calculator tool for mathematical calculations.
    - Always use the weather tool for weather questions.
    - Never answer those yourself.
    - say main nhi bataunga if you dont know the answer
    """

    def __init__(self,tools:list[BaseTool],llm:Groq,model:str):
        self.tools={tool.name:tool for tool in tools}
        self.llm=llm
        self.model=model
    
    def get_definitions(self):
        return  [tool.definition() for tool in self.tools.values()]
    
    def chat(self,question:str):
        tools=self.get_definitions()
        response=self.llm.chat.completions.create(
            messages=[
                {"role":"system","content":str(self.SYSTEM_PROMPT)},
                {"role":"user","content":question}],
            tools=tools,
            model=self.model
        )

        message = response.choices[0].message
        print(message)

        if message.tool_calls:
            tool_call = message.tool_calls[0]

            tool_name = tool_call.function.name
            print("1. Tool selected:", tool_name)

            arguments = tool_call.function.arguments
            j=json.loads(arguments)

            tool = self.tools[tool_name]

            result = tool.run(json=j)
            print("2. Tool result:", result)
            print("3. Calling LLM again...")

            llm_reply=self.llm.chat.completions.create(
                messages=[
                    {"role":"system","content":str(self.SYSTEM_PROMPT)},
                    {"role":"user","content":question},
                    {"role":"assistant","tool_calls":message.tool_calls},
                    {"role":"tool","tool_call_id":tool_call.id,"content":json.dumps(result)}
                ],
                model=self.model

            )
            print("4. Second LLM finished llmreply",llm_reply)
            content=llm_reply.choices[0].message.content or ""
            print(content)
        else:
            print(message.content)
    