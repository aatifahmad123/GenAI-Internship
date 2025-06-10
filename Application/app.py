import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
import gradio as gr

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

# Gemini response function
def get_gemini_response(transcription, timestamps, metadata, agent_id, call_id):
    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = (
        f'''
        Analyze the following call transcript and respond in the following JSON format.
        There can be multiple intents in a single call, and each intent should be captured separately in the JSON array.
        The transcription is an alternating conversation between a customer and an agent starting with the customer.
        You may use timestamps or the nature of conversation in transcript to identify the interruptions.
        There can be multiple issues for same intent so keep the issues as a list of dictionaries.
        The JSON format is as follows:
        
        {{
            "call id": "<Unique identifier for the call>",
            "agent id": "<Unique identifier for the agent>",
            "call duration": "<Duration of the call in seconds, you can get this from metadata file>",
            "summary": "<One professional sentence, no more than 10 words>",
            "intents": [
                {{
                    "intent": "<Intent recognized from the conversation>",
                    "confidence": "<Confidence level of intent recognition, as a percentage (0-100)>",
                    "keywords": "<The part of transcription that identifies the intent, it has to be specific not a large part of transcription, atmost 10-15 words stretch, give a couple of beginning and ending words separated by '...' (mandatorily)>",
                    "intent timestamp": "<Beginning and Ending timestamp of the above keywords that identify the intent, give a relaxed timeframe of 5 seconds (mandatorily), you may use the timstamps data provided>",
                    "products": "<List of products related to intent>",
                    "issues": [
                        {{
                            "issue": "<Brief description of the issue identified by the agent if any>",
                            "reason(s)": "<Brief description of the reason for the issue identified by the agent if any>",
                            "issue type": "<Type of issue out of 
                            1. 'Technical': software bugs, hardware malfunctions, connectivity, or system errors,
                            2. 'Billing': invoices, payments, refunds, overcharges, or subscription,
                            3. 'Service': long wait times, unhelpful support, or lack of follow-up,
                            4. 'General Inquiry': questions not related to specific issues>",
                        }}
                    ],
                    "actions of agent": "<Brief description of the actions taken by the agent to handle the intent>",
                    "resolution status": "<Status of resolution, One out of: 'Resolved', 'Unresolved', Pending with Callback'>",
                    "Process Request": "<Brief description of the process request if any, otherwise 'N/A'. Process request happens when the agent has to do something in the backend or with a third party to resolve the issue>",
                    "resolution": "<Brief description of the resolution irrespective of resolution status>",
                    "resolution timestamp": "<Beginning and Ending timestamp of transcription that determines the resolution, again it has to be very specific atmost 10-15 words stretch, give a relaxed timeframe of 5 seconds (mandatorily), you may use the timstamps data provided>",
                    "dominant emotions (customer)": "[<list main emotions expressed by the customer>]",
                    "conversation sentiment": "<sentiment of the conversation: Positive/Negative/Neutral for that intent>",
                    "customer satisfaction": "<Satisfaction of the customer with the agent's handling of the intent, as a percentage (0-100)>",
                }}
            ],
            "basic greeting and closing": "<Yes/No, whether the agent greeted and closed the call properly>",
            "fatal behaviour": "<Yes/No, whether the agent exhibited any fatal behaviour during the call>",
            "agent professionalism (out of 10)": "<Score from 1 to 10>",
            "agent performance (out of 10)": "<Score from 1 to 10>",
            "customer satisfaction (out of 10)": "<Score from 1 to 10>",
            "interruptions by customer": "<Number of times the customer interrupted the agent>",
            "interruptions by agent": "<Number of times the agent interrupted the customer>",
            "callback promise": "<Yes/No>",
            "callback time": "<Date (relative for eg. same day or next day and Time if applicable, otherwise 'N/A'>"
        }}
        
        Call ID: {call_id}
        Agent ID: {agent_id}
        
        Transcription: {transcription}
        
        Timestamps: {timestamps}
        
        Metadata: {metadata}
        
        Please ensure the JSON is well-formed and valid.
        ''')
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=1750,
            temperature=0.2
        )
    )
    response_text = response.text.strip()
    if response_text.startswith("```json"):
        response_text = response_text.lstrip("```json").strip()
    if response_text.endswith("```"):
        response_text = response_text.rstrip("```").strip()
    return response_text

# Main processing function
def process_call_analysis(call_id, agent_id):
    try:
        # Construct file paths
        dir_path = f'../Calls Data Google Cloud/Agent {agent_id:02d}/Call {call_id:02d}'
        transcription_path = os.path.join(dir_path, 'transcription.txt')
        timestamps_path = os.path.join(dir_path, 'timestamps.json')
        metadata_path = os.path.join(dir_path, 'metadata.txt')
        
        # Check if files exist
        missing_files = []
        if not os.path.exists(transcription_path):
            missing_files.append(f"transcription.txt in {dir_path}")
        if not os.path.exists(timestamps_path):
            missing_files.append(f"timestamps.json in {dir_path}")
        if not os.path.exists(metadata_path):
            missing_files.append(f"metadata.txt in {dir_path}")
        
        if missing_files:
            return None, f"Missing files:\n" + "\n".join(f"• {file}" for file in missing_files)
        
        # Read files
        with open(transcription_path, 'r', encoding='utf-8') as f:
            transcription = f.read()
        with open(timestamps_path, 'r', encoding='utf-8') as f:
            timestamps = f.read()
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = f.read()
        
        # Get Gemini response
        response = get_gemini_response(transcription, timestamps, metadata, agent_id, call_id)
        
        # Parse response to JSON
        try:
            response_json = json.loads(response)
            return response_json, f"Successfully analyzed Call {call_id:02d} for Agent {agent_id:02d}"
        except json.JSONDecodeError:
            return None, f"Invalid JSON response from AI:\n\n{response}"
            
    except Exception as e:
        return None, f"Error: {str(e)}"

# Function to format JSON response into readable format
def format_analysis_results(json_data):
    if not json_data:
        return "No analysis results available."
    
    formatted = f"""
# Call Analysis Report

## Call Information
- **Call ID:** {json_data.get('call id', 'N/A')}
- **Agent ID:** {json_data.get('agent id', 'N/A')}
- **Duration:** {json_data.get('call duration', 'N/A')} seconds
- **Summary:** {json_data.get('summary', 'N/A')}
- **Callback Promise:** {json_data.get('callback promise', 'N/A')}
- **Callback Time:** {json_data.get('callback time', 'N/A')}

## Overall Scores
- **Agent Professionalism:** {json_data.get('agent professionalism (out of 10)', 'N/A')}/10
- **Agent Performance:** {json_data.get('agent performance (out of 10)', 'N/A')}/10
- **Customer Satisfaction:** {json_data.get('customer satisfaction (out of 10)', 'N/A')}/10

## Call Quality
- **Basic Greeting & Closing:** {json_data.get('basic greeting and closing', 'N/A')}
- **Fatal Behaviour:** {json_data.get('fatal behaviour', 'N/A')}
- **Customer Interruptions:** {json_data.get('interruptions by customer', 'N/A')}
- **Agent Interruptions:** {json_data.get('interruptions by agent', 'N/A')}

## Intents Analysis
"""
    
    intents = json_data.get('intents', [])
    for i, intent in enumerate(intents, 1):
        formatted += f"""
### Intent {i}: {intent.get('intent', 'N/A')}
- **Confidence:** {intent.get('confidence', 'N/A')}%
- **Keywords:** "{intent.get('keywords', 'N/A')}"
- **Timestamp:** {intent.get('intent timestamp', 'N/A')}
- **Products:** {', '.join(intent.get('products', [])) if intent.get('products') else 'N/A'}

#### Issues Identified
"""
        issues = intent.get('issues', [])
        for j, issue in enumerate(issues, 1):
            formatted += f"""
**Issue {j}:**
- **Description:** {issue.get('issue', 'N/A')}
- **Reason:** {issue.get('reason(s)', 'N/A')}
- **Type:** {issue.get('issue type', 'N/A')}
"""
        
        formatted += f"""
#### Resolution Details
- **Agent Actions:** {intent.get('actions of agent', 'N/A')}
- **Resolution Status:** {intent.get('resolution status', 'N/A')}
- **Process Request:** {intent.get('Process Request', 'N/A')}
- **Resolution:** {intent.get('resolution', 'N/A')}
- **Resolution Timestamp:** {intent.get('resolution timestamp', 'N/A')}

#### Customer Experience
- **Dominant Emotions:** {', '.join(intent.get('dominant emotions (customer)', [])) if intent.get('dominant emotions (customer)') else 'N/A'}
- **Conversation Sentiment:** {intent.get('conversation sentiment', 'N/A')}
- **Customer Satisfaction:** {intent.get('customer satisfaction', 'N/A')}%

---
"""
    
    return formatted

# Custom CSS for wide layout
custom_css = """
.gradio-container {
    max-width: 100% !important;
    width: 100% !important;
}
"""

# Gradio interface
with gr.Blocks(css=custom_css, title="ICICI Bank Call Analysis") as demo:
    gr.Markdown("# AI Powered Voice Call Summarization with Emotion and Sentiment Analysis")
    gr.Markdown("## Made by Aatif")
    
    # Input section
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Enter Call Details")
            with gr.Row():
                call_id = gr.Number(
                    label="Call ID [1-10]",
                    value=1,
                    minimum=1,
                    maximum=10,
                    step=1,
                    precision=0
                )
                agent_id = gr.Number(
                    label="Agent ID [1-5]", 
                    value=1,
                    minimum=1,
                    maximum=5,
                    step=1,
                    precision=0
                )
    
    # Submit button
    with gr.Row():
        submit_btn = gr.Button("Analyze Call",
                               variant="primary",)
    
    # Status message
    status_output = gr.Textbox(
        label="Status",
        interactive=False,
        visible=False
    )
    
    # Results section
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Analysis Results")
            formatted_output = gr.Markdown(
                label="Formatted Report",
                value="Run analysis to see results here..."
            )
            
            # Keep JSON output in a collapsible section
            with gr.Accordion("Raw JSON Data", open=False):
                output_json = gr.JSON(
                    label="Detailed Analysis JSON"
                )

    
    # Event handlers
    def handle_analysis(call_id, agent_id):
        result, message = process_call_analysis(int(call_id), int(agent_id))
        
        if result:
            formatted_report = format_analysis_results(result)
            return {
                formatted_output: formatted_report,
                output_json: result,
                status_output: gr.update(value=message, visible=True)
            }
        else:
            return {
                formatted_output: "Analysis failed. Check status message below.",
                output_json: None,
                status_output: gr.update(value=message, visible=True)
            }
    
    submit_btn.click(
        fn=handle_analysis,
        inputs=[call_id, agent_id],
        outputs=[formatted_output, output_json, status_output]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        inbrowser=True
    )