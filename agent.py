import os 
from smolagents import CodeAgent , InferenceClientModel , DuckDuckGoSearchTool , Tool


class SaveToFileTool(Tool):
        name = "save_to_file"
        description = (
            "Save text content to a local markdown file , call this once at ,"
            "the very end, to save your finished answer or report"
        )
        inputs = {
            "content": {
                "type" : "string",
                "description" : "The full text to save, in markdown.",
            },
            "filename" : {
                "tyre" : "string",
                "description" : "Filename to save , eg , 'report.md'",
            },
        }
        output_type = "string"

        def foreward(self, content: str , filename: str) -> str:
            with open(filename, "w" , ecoding = "utf-8") as f:
                f.write(content)
            return f" Saved report to {filename}"


model = InferenceClientModel(
    model_id = "Qwen/Qwen2.5-7B-Instruct",
    token=os.environ["HF_TOKEN"],
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool(),SaveToFileTool()] , model=model , max_steps=6)

result = agent.run("What is the current version of python and when was is realesed"
                  "Then save a short summary (2-3 sentences , with the source URL) to"
                  "'report.md' using save_to_fil."
)
print("\n Final Answer")
print(result)
