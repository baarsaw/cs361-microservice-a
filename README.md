# cs361-microservice-a
Author: Sawyer Baar

## Description
A simple REST API microservice to manage study sessions.

The app will not run locally since it needs to communicate with the Datastore Instance located on the Google Cloud Platform.

### BASE URL
```
base_url:

"https://cs361-microservice-a-123.uw.r.appspot.com"
```

### Endpoints Available

1.POST
  a. post a new session
  b. example
  ```
    new_session = {
    "startTime": "2025-02-24T14:10:56-07:00",
    "duration": 30,
    "breakTime": 5,
    "sessionSubject": "CS361 Project",
    "notes": "Completed reading"
    }

    endpoint_url = base_url + "/sessions"
    response = requests.post(endpoint_url, json=new_session)
  ```
