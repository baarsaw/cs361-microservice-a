import requests
import json

# testing = "local"  # "local" or "cloud"
testing = "cloud"  # "local" or "cloud"

# Use localhost for testing
local_url = "http://127.0.0.1:8000"
cloud_url = "https://cs361-microservice-a-123.uw.r.appspot.com"

if testing == "local":
    base_url = local_url
else:
    base_url = cloud_url

def print_response(endpoint, response):
    print(f"\n=== Testing {endpoint} ===")
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:", json.dumps(response.json(), indent=2))
    except:
        print("Response:", response.text)
    print("="*50)

def wait_for_user(message="Press 'y' to continue to the next step: "):
    while True:
        if input(message).lower() == 'y':
            break

# First, delete all existing sessions to start fresh
print("\nClearing all existing sessions...")
requests.delete(f"{base_url}/sessions")

# Create 5 test sessions with different subjects and times
base_time = "2025-02-24T13:48:41-07:00"
test_sessions = [
    {
    "id": 1675971650984,
    "startTime": "2025-02-10T10:05:00Z",
    "duration": 1500,
    "breakTime": 300,
    "sessionSubject": "CS361 Project",
    "notes": "Completed reading."
    },
    {
    "id": 1675971650984,
    "startTime": "2025-02-10T18:05:00Z",
    "duration": 1500,
    "breakTime": 300,
    "sessionSubject": "CS361 Project",
    "notes": "Completed reading."
    },
    {
    "id": 1675971650984,
    "startTime": "2025-02-10T15:05:00Z",
    "duration": 1500,
    "breakTime": 300,
    "sessionSubject": "CS361 Project",
    "notes": "Completed reading."
    },
    {
    "id": 1675971650984,
    "startTime": "2025-03-24T10:05:00Z",
    "duration": 1,
    "breakTime": 50000,
    "sessionSubject": "CS361 Project",
    "notes": "Didn't do anything."
    },
    {
    "id": 1675971650984,
    "startTime": "2024-02-10T10:05:00Z",
    "duration": 3,
    "breakTime": 3,
    "sessionSubject": "CS361 Project",
    "notes": "Completed Assignment."
    }
]

print("\nCreating 5 test sessions...")
created_sessions = []
for session in test_sessions:
    response = requests.post(f"{base_url}/sessions", json=session)
    if response.status_code == 201:
        created_sessions.append(response.json())
    print_response("POST /sessions", response)

print("\n=== Testing GET Operations ===")
# Test 1: Get all sessions
wait_for_user("\nPress 'y' to get all sessions: ")
print_response("GET /sessions", requests.get(f"{base_url}/sessions"))

# Test 2: Get sessions with limit=3
wait_for_user("\nPress 'y' to get sessions with limit=3: ")
print_response("GET /sessions?limit=3", requests.get(f"{base_url}/sessions?limit=3"))

# Test 3: Get sessions filtered by subject 
wait_for_user("\nPress 'y' to get sessions filtered by subject (CS361 Project): ")
print_response("GET /sessions?sessionSubject=CS361 Project", 
              requests.get(f"{base_url}/sessions?sessionSubject=CS361 Project")) 

print("\n=== Testing DELETE Operations ===")
# Test 4: Delete a specific session 
if created_sessions:
    cs361_session = next((s for s in created_sessions if s.get('sessionSubject') == 'CS361 Project'), None)
    if cs361_session:
        wait_for_user(f"\nPress 'y' to delete CS361 Project session (ID: {cs361_session['id']}): ")
        print_response(f"DELETE /sessions/{cs361_session['id']}", 
                      requests.delete(f"{base_url}/sessions/{cs361_session['id']}"))


# Test 5: Delete all sessions
wait_for_user("\nPress 'y' to delete all sessions: ")
print_response("DELETE /sessions", requests.delete(f"{base_url}/sessions"))


# Test 7: Health check
wait_for_user("\nPress 'y' to perform health check: ")
print_response("POST /test_if_online", requests.post(f"{base_url}/test_if_online"))

print("\nAll tests completed!")