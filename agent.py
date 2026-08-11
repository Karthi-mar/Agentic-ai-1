import os 
from smolagents import CodeAgent , InferenceClientModel 

model = InferenceClientModel(
    model_id = "Qwen/Qwen2.5-7B-Instruct",
    token=os.environ["HF_TOKEN"],
)

agent = CodeAgent(tools=[] , model=model , max_steps=4)

result = agent.run("What is 17*4+9 ? Show your reasoning.")
print("\n Final Answer")
print(result)
