import os 
from smolagents import CodeAgent , InferenceClientModel , DuckDuckGoSearchTool 

model = InferenceClientModel(
    model_id = "Qwen/Qwen2.5-7B-Instruct",
    token=os.environ["HF_TOKEN"],
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()] , model=model , max_steps=4)

result = agent.run("What is the current version of python and when was is realesed")
print("\n Final Answer")
print(result)
