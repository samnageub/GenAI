
from praisonaiagents import Agent, MCP
import gradio as gr

# Define a function to search Airbnb using the MCP server
def search_airbnb(query):
    agent = Agent(
        instructions="""You help book apartments on Airbnb.""",
        llm="gpt-4o-mini",
        tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
    )
    result = agent.start(query)
    return f"## Airbnb Search Result\n\n{result}"

# Create a Gradio interface
demo=gr.Interface(
    fn=search_airbnb,
    inputs=gr.Textbox(placeholder=" want to book my apartment in Paris for 2 nights....."),
    outputs=gr.Markdown(),
    title="Sam Airbnb Booking AI Agent Assistant Using MCP",
    description="This app helps you book apartments on Airbnb. Enter your booking requirements to get started."
)

# Launch the interface
if __name__ == "__main__":
    demo.launch(share=True)
