from transformers import pipeline

def summarize_call(conversation_json):
    # Format conversation
    formatted_text = "\n".join(
        [f"{turn['speaker']}: {turn['text']}" for turn in conversation_json['conversation']]
    )

    # Initialize a summarization pipeline
    summarizer = pipeline(
        "summarization", 
        model="philschmid/bart-large-cnn-samsum"
    )

    # Generate and return the summary
    summary = summarizer(formatted_text)[0]['summary_text']
    
    return summary

# Input conversation
input_data = {
    "conversation": [
        {"speaker": "Customer", "text": "Hey, I’ve been charged twice on my credit card for the same transaction! This is ridiculous!"},
        {"speaker": "RM", "text": "I’m so sorry to hear that, Sir. Can you share the transaction details so I can check the chargeback status?"},
        {"speaker": "Customer", "text": "It’s from last week, uh, some restaurant bill… ₹5,200. I saw it twice on my statement!"},
        {"speaker": "RM", "text": "Got it. Let me pull up your account. It sounds like a duplicate charge; we can initiate a chargeback request right away."},
        {"speaker": "Customer", "text": "You better! I can’t keep paying for your mistakes!"},
        {"speaker": "RM", "text": "Absolutely, I understand your frustration. I’ve flagged this for a refund, and it should reflect in 5-7 business days."}
    ]
}

# Generate and print summary
print("Call Summary:\n", summarize_call(input_data))