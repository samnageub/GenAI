from praisonaiagents import Agent, MCP
import gradio as gr
import requests
import json 

# Define a function to analyze traffic and adjust signal lights
def analyze_traffic_MCP(query):
    # Connect to a hypothetical MCP server for live traffic data
    agent = Agent(
        instructions="""You are an AI traffic management assistant. Analyze live traffic data and provide 
        recommendations for adjusting signal lights dynamically to optimize traffic flow.""",
        llm="gpt-4o-mini",
        tools=MCP("npx -y @opentraffic/mcp-server-traffic --live-data")
    )
    
    # Process the query through the agent
    result = agent.start(query)
    
    # Return the result as a Markdown response
    return f"## Traffic Signal Adjustment Recommendations\n\n{result}" if result else "No recommendations available."

def analyze_traffic_api_agent(location):
    api_key = "AIzaSyB05CAgY-S2AqTlmNWJOQ66rEbY5iWJd9A"
    url = f"https://maps.googleapis.com/maps/api/traffic/json?location={location}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        traffic_data = response.json()
        # Process the traffic data into a readable format
        if "error" in traffic_data:
            return f"Error: {traffic_data['error']['message']}"
        else:
            # Format the traffic data into Markdown
            formatted_data = "### Traffic Data\n\n"
            for key, value in traffic_data.items():
                formatted_data += f"- **{key}**: {value}\n"
            return formatted_data
    else:
        return f"Error: Unable to fetch traffic data (HTTP {response.status_code})"

def analyze_traffic_json(query):
    # Load mock traffic data
    mock_data_file = "mock_traffic_data.json"
    try:
        with open(mock_data_file, "r") as file:
            mock_data = json.load(file)
    except FileNotFoundError:
        return "Error: Mock traffic data file not found."
    except json.JSONDecodeError:
        return "Error: Failed to parse mock traffic data."

    # Check if the query location exists in the mock data
    if query in mock_data:
        traffic_info = mock_data[query]
        streets = traffic_info.get("streets", [])
        
        # Format the response
        formatted_response = f"### Traffic Data for {query}\n\n"
        for street in streets:
            name = street.get("name", "Unknown Street")
            vehicle_count = street.get("vehicle_count", "N/A")
            average_speed = street.get("average_speed", "N/A")
            incidents = ", ".join(street.get("incidents", [])) or "None"
            pedestrian_activity = street.get("pedestrian_activity", "N/A")
            cyclist_activity = street.get("cyclist_activity", "N/A")
            time_of_day = street.get("time_of_day", "N/A")
            
            formatted_response += f"- **Street**: {name}\n"
            formatted_response += f"  - Vehicle Count: {vehicle_count}\n"
            formatted_response += f"  - Average Speed: {average_speed} mph\n"
            formatted_response += f"  - Incidents: {incidents}\n"
            formatted_response += f"  - Pedestrian Activity: {pedestrian_activity}\n"
            formatted_response += f"  - Cyclist Activity: {cyclist_activity}\n"
            formatted_response += f"  - Time of Day: {time_of_day}\n\n"
        
        # Add recommendations based on traffic data
        formatted_response += "### Recommendations\n\n"
        for street in streets:
            if street["vehicle_count"] > 100:
                formatted_response += f"- Increase green light duration on {street['name']}.\n"
            if street["average_speed"] < 20:
                formatted_response += f"- Investigate congestion on {street['name']}.\n"
            if street["pedestrian_activity"] == "High":
                formatted_response += f"- Prioritize pedestrian crossings on {street['name']}.\n"
            if street["cyclist_activity"] == "High":
                formatted_response += f"- Ensure safe crossings for cyclists on {street['name']}.\n"
            if street["incidents"]:
                formatted_response += f"- Address incidents on {street['name']} ({', '.join(street['incidents'])}).\n"
        return formatted_response
    else:
        return f"No traffic data available for {query}."
# Create a Gradio interface
demo_mcp = gr.Interface(
    fn=analyze_traffic_MCP,
    inputs=gr.Textbox(placeholder="Describe the traffic situation or ask for signal adjustments..."),
    outputs=gr.Markdown(),
    title="AI Traffic Management Assistant",
    description="This app analyzes live traffic data and provides recommendations for adjusting signal lights dynamically."
)

demo_api = gr.Interface(
    fn=analyze_traffic_api_agent,
    inputs=gr.Textbox(placeholder="Describe the traffic situation or ask for signal adjustments..."),
    outputs=gr.Markdown(),
    title="AI Traffic Management Assistant",
    description="This app analyzes live traffic data and provides recommendations for adjusting signal lights dynamically."
)

demo_json = gr.Interface(
    fn=analyze_traffic_json,
    inputs=gr.Textbox(placeholder="Enter a location (e.g., Seattle, WA)..."),
    outputs=gr.Markdown(),
    title="AI Traffic Management Assistant (Mock Data)",
    description="This app uses mock traffic data to provide recommendations for optimizing traffic lights dynamically."
)
# Launch the interface
if __name__ == "__main__":
    demo_mcp.launch(share=True)