from openai import OpenAI
import json

# Get the API key from secrets
api_key = "{{secrets.chains_parallel}}"

# Create OpenAI client pointed to Parallel's API
client = OpenAI(
    api_key=api_key,
    base_url="https://beta.parallel.ai"
)

def validate_messages(messages):
    """Validate messages array format"""
    if not isinstance(messages, list) or len(messages) == 0:
        raise Exception("messages must be a non-empty array")
    
    for i, msg in enumerate(messages):
        if not isinstance(msg, dict):
            raise Exception(f"Message {i} must be an object")
        if "role" not in msg or "content" not in msg:
            raise Exception(f"Message {i} must have 'role' and 'content' fields")
        if msg["role"] not in ["system", "user", "assistant"]:
            raise Exception(f"Message {i} role must be 'system', 'user', or 'assistant'")

# Helper functions removed - using OpenAI client directly

# Get and validate parameters
messages = params["messages"]
response_format = params.get("response_format", {"type": "text"})
stream = params.get("stream", False)
max_tokens = params.get("max_tokens")

try:
    # Validate input
    validate_messages(messages)
    
    # Make the API request using OpenAI client
    if stream:
        raise Exception("Streaming not yet implemented - set stream=false")
    
    response = client.chat.completions.create(
        model="speed",
        messages=messages,
        response_format=response_format if response_format.get("type") != "text" else None,
        stream=stream
    )
    
    result = response
    
    # Return the complete response or extract content based on response format
    content = result.choices[0].message.content
    
    if response_format.get("type") == "json_schema":
        # For JSON schema responses, return the parsed content
        try:
            parsed_content = json.loads(content) if isinstance(content, str) else content
            return {
                "response": parsed_content,
                "raw_response": result.model_dump(),
                "format": "json_schema"
            }
        except json.JSONDecodeError:
            return {
                "response": content,
                "raw_response": result.model_dump(),
                "format": "text",
                "warning": "Response was not valid JSON despite JSON schema request"
            }
    else:
        # For text responses, return the content directly
        return {
            "response": content,
            "raw_response": result.model_dump(),
            "format": "text"
        }
    
except Exception as e:
    return {
        "error": str(e),
        "message": "Chat request failed using OpenAI client"
    }