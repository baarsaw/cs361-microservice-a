# cs361-microservice-a
Author: Sawyer Baar

## Description
A simple REST API microservice to manage study sessions.

## Deployment

This app is deployed to Google App Engine. There is a frontend provided for this app that allows the user to view the full contents of the database. The link is below. Once you make an HTTP request, please refresh the page to see any changes.

  https://cs361-microservice-a-123.uw.r.appspot.com/

As a note, this app will not run locally since it needs to communicate with the Datastore Database Instance located on the Google Cloud Platform.

## BASE URL
```
base_url:

"https://cs361-microservice-a-123.uw.r.appspot.com"
```

## Endpoints Available

### 1.POST - post a new session

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

### 2.GET - get all sessions

  In this example, we return a list of all sessions

  REQUEST:
  ```
    endpoint_url = base_url + "/sessions"
    response = requests.get(endpoint_url)
  ```
  In the response below, there are two sessions total in the database. They are returned as a list.

  RESPONSE:
  ```
  status_code: 200 OK
  [
      {
          "breakTime": 300,
          "duration": 1500,
          "id": 5634601401712640,
          "notes": "Completed reading.",
          "sessionSubject": "CS361 Project",
          "startTime": "2025-02-10T10:05:00Z"
      },
      {
          "breakTime": 300,
          "duration": 1500,
          "id": 5657818854064128,
          "notes": "Completed reading.",
          "sessionSubject": "CS361 Project",
          "startTime": "2025-02-10T10:05:00Z"
      }
  ]
  ```

### 3.GET - get a spsecified number of most recent sessions

  In this example, we set the limit parameter equal to 3 in order to retrieve the 3 most recent sessions.

  REQUEST:
  ```
    endpoint_url = base_url + "/sessions?limit=3"
    response = requests.get(endpoint_url)
  ```
  The three most recent sessions sorted chronologically are returned.

  RESPONSE:
  ```
  status_code: 200 OK
  [
    {
        "breakTime": 50000,
        "duration": 1,
        "id": 5080330100801536,
        "notes": "Didn't do anything.",
        "sessionSubject": "CS361 Project",
        "startTime": "2025-03-24T10:05:00Z"
    },
    {
        "breakTime": 1000,
        "duration": 1000,
        "id": 5106202648248320,
        "notes": "Completed next weeks assignemnt.",
        "sessionSubject": "CS361 Project",
        "startTime": "2025-02-10T11:05:00Z"
    },
    {
        "breakTime": 300,
        "duration": 1500,
        "id": 5634601401712640,
        "notes": "Completed reading.",
        "sessionSubject": "CS361 Project",
        "startTime": "2025-02-10T10:05:00Z"
    }
]
  ```

### 4.GET - get all sessions filtered by Subject 
  (CURRENTLY NOT WORKING)

  This functionality was working locally but is not working once deployed to GCP. I will continue to troubleshoot and attempt to add this functionality.

### 5.DELETE - delete by ID
  
  Delete a session entry by id. The session_id_number below should be an integer matching an id of session.
  
  REQUEST:
  ```
  endpoint_url = base_url + "/sessions/session_id_number"
  response = requests.delete(endpoint_url)
  ```
  
  RESPONSE:
  ```
  Status_code: 200 OK
  {
    "message": "Session deleted"
  }
  ```

### 6.DELETE - delete all
  
  Delete all sessions in the database.
  
  REQUEST:
  ```
  endpoint_url = base_url + "/sessions"
  response = requests.delete(endpoint_url)
  ```
  
  RESPONSE:
  ```
  Status_code: 200 OK
  {
    "message": "All sessions cleared"
  }
  ```


