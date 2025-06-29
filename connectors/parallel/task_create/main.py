import requests

# Get the API key from secrets
api_key = "{{secrets.chains_parallel}}"

base_headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

def create_task_run(payload):
    """Create a new task run"""
    url = "https://api.parallel.ai/v1/tasks/runs"
    response = requests.post(url, json=payload, headers=base_headers)
    
    if response.status_code == 202:  # Accepted - task queued successfully
        return response.json()
    else:
        raise Exception(f"Task creation failed with status code {response.status_code}: {response.text}")

# Build the request payload according to official API docs
payload = {
    "input": params["input"],
    "processor": params["processor"]
}

# Add task_spec with output_schema if provided
if params.get("output_schema"):
    payload["task_spec"] = {
        "output_schema": params["output_schema"]
    }

# Create the task and return the initial response
try:
    task_result = create_task_run(payload)
    
    # Return the task creation result with run_id and status
    return {
        "run_id": task_result.get("run_id"),
        "status": task_result.get("status"),
        "is_active": task_result.get("is_active"),
        "processor": task_result.get("processor"),
        "created_at": task_result.get("created_at"),
        "message": "Task created successfully. Use the run_id with 'Parallel Task Get Results' to retrieve the completed research."
    }
    
except Exception as e:
    # Return error in the expected format
    return {
        "error": str(e),
        "message": "Task creation failed"
    }
