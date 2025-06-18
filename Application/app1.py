import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.cloud import speech
import gradio as gr
from datetime import datetime
import wave
import io

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

# Initialize Google Cloud Speech client
speech_client = speech.SpeechClient()

# Function to get audio duration
def get_audio_duration(audio_path):
    try:
        with wave.open(audio_path, 'rb') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            return duration
    except Exception as e:
        return f"Error calculating duration: {str(e)}"

# Function to transcribe audio
def transcribe_audio(audio_path, language="en-IN"):
    
    try:
        with io.open(audio_path, "rb") as audio:
            content = audio.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=24000,
            language_code=language,
            model="latest_short",
            audio_channel_count=1,
            enable_automatic_punctuation=True,
        )

        response = speech_client.recognize(config=config, audio=audio)
        transcript_lines = []
        for result in response.results:
            transcript = result.alternatives[0].transcript
            transcript_lines.append(transcript)
        
        return "\n".join(transcript_lines)
    except Exception as e:
        return f"Error during transcription: {str(e)}"

# Function to generate timestamps
def generate_timestamps(audio_path, language="en-IN"):
    
    try:
        with io.open(audio_path, "rb") as audio:
            content = audio.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=24000,
            language_code=language,
            model="latest_short",
            audio_channel_count=1,
            enable_word_time_offsets=True,
            enable_automatic_punctuation=True,
        )

        response = speech_client.recognize(config=config, audio=audio)
        all_words_data = []
        for result in response.results:
            for word_info in result.alternatives[0].words:
                start_time = word_info.start_time.total_seconds()
                end_time = word_info.end_time.total_seconds()
                word_data = {
                    "word": word_info.word,
                    "start_time": f"{start_time:.3f} sec",
                    "end_time": f"{end_time:.3f} sec",
                }
                all_words_data.append(word_data)
        
        return all_words_data
    except Exception as e:
        return {"error": f"Error generating timestamps: {str(e)}"}

# Gemini response function (modified to remove call_id and agent_id)
def get_gemini_response(transcription, timestamps, metadata):
    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = (
        f'''
        Analyze the following call transcript and respond in the following JSON format.
        There can be multiple intents in a single call, and each intent should be captured separately in the JSON array.
        The transcription is a conversation without explicit speaker tags.
        You may use timestamps or the nature of conversation in transcript to identify the interruptions.
        There can be multiple issues for same intent so keep the issues as a list of dictionaries.
        The JSON format is as follows:
        
        {{
            "call duration": "<Duration of the call in seconds, you can get this from metadata>",
            "summary": "<One professional sentence, no more than 10 words>",
            "intents": [
                {{
                    "intent": "<Intent recognized from the conversation>",
                    "confidence": "<Confidence level of intent recognition, as a percentage (0-100)>",
                    "keywords": "<The part of transcription that identifies the intent, it has to be specific not a large part of transcription, atmost 10-15 words stretch, give a couple of beginning and ending words separated by '...' (mandatorily)>",
                    "intent timestamp": "<Beginning and Ending timestamp of the above keywords that identify the intent, give a relaxed timeframe of 5 seconds (mandatorily), you may use the timestamps data provided>",
                    "products": "<List of products related to intent>",
                    "issues": [
                        {{
                            "issue": "<Brief description of the issue identified if any>",
                            "reason(s)": "<Brief description of the reason for the issue identified if any>",
                            "issue type": "<Type of issue out of 
                            1. 'Technical': software bugs, hardware malfunctions, connectivity, or system errors,
                            2. 'Billing': invoices, payments, refunds, overcharges, or subscription,
                            3. 'Service': long wait times, unhelpful support, or lack of follow-up,
                            4. 'General Inquiry': questions not related to specific issues>",
                        }}
                    ],
                    "actions of agent": "<Brief description of the actions taken to handle the intent>",
                    "resolution status": "<Status of resolution, One out of: 'Resolved', 'Unresolved', Pending with Callback'>",
                    "Process Request": "<Brief description of the process request if any, otherwise 'N/A'. Process request happens when something is done in the backend or with a third party to resolve the issue>",
                    "resolution": "<Brief description of the resolution irrespective of resolution status>",
                    "resolution timestamp": "<Beginning and Ending timestamp of transcription that determines the resolution, again it has to be very specific atmost 10-15 words stretch, give a relaxed timeframe of 5 seconds (mandatorily), you may use the timestamps data provided>",
                    "dominant emotions (customer)": "[<list main emotions expressed by the customer>]",
                    "conversation sentiment": "<sentiment of the conversation: Positive/Negative/Neutral for that intent>",
                    "customer satisfaction": "<Satisfaction of the customer with the handling of the intent, as a percentage (0-100)>",
                }}
            ],
            "basic greeting and closing": "<Yes/No, whether the call included proper greeting and closing>",
            "fatal behaviour": "<Yes/No, whether any fatal behaviour was exhibited during the call>",
            "professionalism (out of 10)": "<Score from 1 to 10>",
            "performance (out of 10)": "<Score from 1 to 10>",
            "customer satisfaction (out of 10)": "<Score from 1 to 10>",
            "interruptions by customer": "<Number of times the customer interrupted>",
            "interruptions by agent": "<Number of times the agent interrupted>",
            "callback promise": "<Yes/No>",
            "callback time": "<Date (relative for eg. same day or next day and Time if applicable, otherwise 'N/A'>"
        }}
        
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

# Function to format JSON response into readable format
def format_analysis_results(json_data):
    if not json_data:
        return "No analysis results available."
    
    formatted = f"""# Call Analysis Report

## Call Information
- **Duration:** {json_data.get('call duration', 'N/A')} seconds
- **Summary:** {json_data.get('summary', 'N/A')}
- **Callback Promise:** {json_data.get('callback promise', 'N/A')}
- **Callback Time:** {json_data.get('callback time', 'N/A')}

## Overall Scores
- **Professionalism:** {json_data.get('professionalism (out of 10)', 'N/A')}/10
- **Performance:** {json_data.get('performance (out of 10)', 'N/A')}/10
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
- **Actions:** {intent.get('actions of agent', 'N/A')}
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

# Function to create downloadable file
def create_download_file(formatted_report):
    if not formatted_report or formatted_report == "No analysis results available.":
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Call_Analysis_{timestamp}.md"
    
    header = f"""---
title: Call Analysis Report
generated_on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
---

"""
    
    full_content = header + formatted_report
    temp_filepath = f"/tmp/{filename}"
    try:
        with open(temp_filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        return temp_filepath
    except Exception as e:
        print(f"Error creating download file: {e}")
        return None

# Custom CSS for wide layout
custom_css = """
.gradio-container {
    max-width: 100% !important;
    width: 100% !important;
}
.download-btn {
    background: linear-gradient(45deg, #4CAF50, #45a049) !important;
    color: white !important;
    font-weight: bold !important;
}
"""

# Gradio interface
with gr.Blocks(css=custom_css, title="ICICI Bank Call Analysis") as demo:
    gr.Markdown("# AI Powered Voice Call Summarization with Emotion and Sentiment Analysis")
    
    # Input section
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Upload Audio and Select Options")
            audio_input = gr.Audio(label="Upload Audio File (WAV)", type="filepath")
            language = gr.Dropdown(
                label="Select Language",
                choices=[
                    ("English", "en-IN"),
                    ("Hindi", "hi-IN"),
                    ("Hinglish", "en-IN")
                ],
                value="en-IN"
            )
    
    # Action buttons
    with gr.Row():
        duration_btn = gr.Button("Get Call Duration", variant="primary")
        transcribe_btn = gr.Button("Generate Transcript", variant="primary")
        timestamps_btn = gr.Button("Generate Timestamps", variant="primary")
        analyze_btn = gr.Button("Generate Call Report", variant="primary")
    
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
            
            # Duration output
            with gr.Accordion("Call Duration", open=False):
                duration_output = gr.Textbox(
                    label="Duration",
                    value="Click 'Get Call Duration' to see results..."
                )
            
            # Transcription output
            with gr.Accordion("Transcription", open=False):
                transcription_output = gr.Textbox(
                    label="Transcript",
                    value="Click 'Generate Transcript' to see results..."
                )
            
            # Timestamps output
            with gr.Accordion("Timestamps", open=False):
                timestamps_output = gr.JSON(
                    label="Timestamps JSON",
                    value=None
                )
            
            # Call analysis output
            with gr.Accordion("Call Analysis Report", open=False):
                formatted_output = gr.Markdown(
                    label="Formatted Report",
                    value="Click 'Generate Call Report' to see results..."
                )
                download_btn = gr.DownloadButton(
                    "Download Report",
                    variant="secondary",
                    visible=False,
                    elem_classes=["download-btn"]
                )
                with gr.Accordion("Raw JSON Data", open=False):
                    output_json = gr.JSON(
                        label="Detailed Analysis JSON",
                        value=None
                    )
    
    # Event handlers
    def handle_duration(audio_path):
        if not audio_path:
            return {
                duration_output: "Please upload an audio file first.",
                status_output: gr.update(value="No audio file provided.", visible=True)
            }
        duration = get_audio_duration(audio_path)
        return {
            duration_output: f"Duration: {duration:.2f} seconds" if isinstance(duration, float) else duration,
            status_output: gr.update(value="Duration calculated successfully.", visible=True)
        }
    
    def handle_transcription(audio_path, language):
        if not audio_path:
            return {
                transcription_output: "Please upload an audio file first.",
                status_output: gr.update(value="No audio file provided.", visible=True)
            }
        transcription = transcribe_audio(audio_path, language)
        return {
            transcription_output: transcription,
            status_output: gr.update(value="Transcription generated successfully.", visible=True)
        }
    
    def handle_timestamps(audio_path, language):
        if not audio_path:
            return {
                timestamps_output: {"error": "Please upload an audio file first."},
                status_output: gr.update(value="No audio file provided.", visible=True)
            }
        timestamps = generate_timestamps(audio_path, language)
        return {
            timestamps_output: timestamps,
            status_output: gr.update(value="Timestamps generated successfully.", visible=True)
        }
    
    def handle_analysis(audio_path, language):
        if not audio_path:
            return {
                formatted_output: "Please upload an audio file first.",
                output_json: None,
                status_output: gr.update(value="No audio file provided.", visible=True),
                download_btn: gr.update(visible=False)
            }
        
        try:
            transcription = transcribe_audio(audio_path, language)
            timestamps = json.dumps(generate_timestamps(audio_path, language))
            duration = get_audio_duration(audio_path)
            metadata = f"Duration: {duration:.2f} seconds" if isinstance(duration, float) else "N/A"
            
            response = get_gemini_response(transcription, timestamps, metadata)
            response_json = json.loads(response) if response else None
            
            if response_json:
                formatted_report = format_analysis_results(response_json)
                download_file = create_download_file(formatted_report)
                return {
                    formatted_output: formatted_report,
                    output_json: response_json,
                    status_output: gr.update(value="Successfully generated call analysis report.", visible=True),
                    download_btn: gr.update(value=download_file, visible=True if download_file else False)
                }
            else:
                return {
                    formatted_output: "Analysis failed. Check status message below.",
                    output_json: None,
                    status_output: gr.update(value="Invalid JSON response from AI.", visible=True),
                    download_btn: gr.update(visible=False)
                }
        except Exception as e:
            return {
                formatted_output: "Analysis failed. Check status message below.",
                output_json: None,
                status_output: gr.update(value=f"Error: {str(e)}", visible=True),
                download_btn: gr.update(visible=False)
            }

    duration_btn.click(
        fn=handle_duration,
        inputs=[audio_input],
        outputs=[duration_output, status_output]
    )
    
    transcribe_btn.click(
        fn=handle_transcription,
        inputs=[audio_input, language],
        outputs=[transcription_output, status_output]
    )
    
    timestamps_btn.click(
        fn=handle_timestamps,
        inputs=[audio_input, language],
        outputs=[timestamps_output, status_output]
    )
    
    analyze_btn.click(
        fn=handle_analysis,
        inputs=[audio_input, language],
        outputs=[formatted_output, output_json, status_output, download_btn]
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        inbrowser=True
    )