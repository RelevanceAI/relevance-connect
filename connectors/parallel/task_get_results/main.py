import requests
import time

# Get the API key from secrets
api_key = "{{secrets.chains_parallel}}"

base_headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

def get_task_result_with_polling(run_id, max_total_wait_time=300, poll_interval=30):
    """Poll for task result with shorter intervals to avoid infrastructure timeouts"""
    url = f"https://api.parallel.ai/v1/tasks/runs/{run_id}/result"
    start_time = time.time()
    
    while time.time() - start_time < max_total_wait_time:
        try:
            # Use shorter timeout for each individual request to avoid CloudFront timeouts
            response = requests.get(url, headers=base_headers, timeout=60)  # 60 second timeout
            
            if response.status_code == 200:
                # Check if we got HTML error page (like CloudFront timeout)
                if response.text.strip().startswith('<!DOCTYPE') or response.text.strip().startswith('<HTML'):
                    # Wait and retry on infrastructure timeout
                    time.sleep(poll_interval)
                    continue
                
                return response.json()
                
            elif response.status_code == 408:  # Request timeout
                # Wait and retry
                time.sleep(poll_interval)
                continue
                
            else:
                raise Exception(f"Result retrieval failed with status code {response.status_code}: {response.text}")
                
        except requests.Timeout:
            # On timeout, wait and retry rather than failing immediately
            time.sleep(poll_interval)
            continue
            
        except requests.RequestException as e:
            # For other request errors, wait and retry
            time.sleep(poll_interval)
            continue
    
    # If we've exceeded max wait time
    raise Exception(f"Task {run_id} did not complete within {max_total_wait_time} seconds")

def check_task_status(run_id):
    """Check task status without waiting for completion"""
    url = f"https://api.parallel.ai/v1/tasks/runs/{run_id}"
    try:
        response = requests.get(url, headers=base_headers, timeout=30)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

# Get parameters
run_id = params["run_id"]
timeout = params.get("timeout", 300)

# Validate run_id format
if not run_id or not run_id.startswith("trun_"):
    return {
        "error": "Invalid run_id format",
        "message": "run_id must start with 'trun_' and be obtained from 'Parallel Task Create'"
    }

# Check task status first to provide better feedback
task_status = check_task_status(run_id)
if task_status and task_status.get("status") == "failed":
    return {
        "error": f"Task {run_id} failed",
        "message": task_status.get("error", "Task failed for unknown reason"),
        "task_status": task_status
    }

# Retrieve the results with polling
try:
    final_result = get_task_result_with_polling(run_id, timeout)
    
    # Return the complete result
    return final_result
    
except Exception as e:
    # Return error with helpful context
    return {
        "error": str(e),
        "message": f"Failed to retrieve results for task {run_id}",
        "run_id": run_id,
        "suggestion": "If the task is still running, try again later or increase the timeout value."
    } 