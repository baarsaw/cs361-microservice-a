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

1.POST - post a new session
  In this example, we post a new session with the data below to the database.
  REQUEST:
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
  RESPONSE:
  ```
    Status_Code = 201 Created
    {
    "breakTime": 300,
    "duration": 1500,
    "id": 5657818854064128,
    "notes": "Completed reading.",
    "sessionSubject": "CS361 Project",
    "startTime": "2025-02-10T10:05:00Z"
    }
  ```

2.GET - get all sessions
  In this example, we return a list of all sessions
  ```
    endpoint_url = base_url + "/sessions"
    response = requests.get(endpoint_url)
  ```

3.GET - get a specific number of most recent sessions
  In this example, we set the limit parameter equal to 3 to retrieve the 3 most recent sessions.
  ```
    endpoint_url = base_url + "/sessions?limit=3"
    response = requests.get(endpoint_url)
  ```
4.GET - get all sessions filtered by Subject (CURRENTLY NOT WORKING)

  ```
    endpoint_url = base_url + "/sessions?subject=3"
    response = requests.get(endpoint_url)
  ```
