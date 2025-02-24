from flask import Flask, request, jsonify, send_file, render_template
from google.cloud import datastore, storage
import io
import datetime
import requests
import json

app = Flask(__name__)
datastore_client = datastore.Client()


# entities  
SESSIONS = "sessions"
TEST_IF_ONLINE = "test_if_online"

# error messages
#400 ERROR
ERROR_BAD_REQUEST = {"Error": "The request body is invalid"} #400
#401 ERROR
ERROR_UNAUTHORIZED = {"Error": "Unauthorized"} #401
#403 ERROR
ERROR_NO_PERMISSION = {"Error": "You don't have permission on this resource"} #403
#404 ERROR
ERROR_NOT_FOUND = {"Error": "Not found"} #404
# #409 ERROR
ERROR_409 = {"Error": "Session data is invalid"} #409

# PROPERTIES
SESSION_PROPERTIES = ['id', 'startTime', 'duration', 'breakTime', 'sessionSubject', 'notes']

# HELPER FUCNTIONS ---------------------------------------
def invalid_content(content, properties):
    return False

# SESSION: Endpoints ---------------------------------------
@app.route('/')
def index():
    query = datastore_client.query(kind=SESSIONS)
    sessions = list(query.fetch())
    return render_template('index.html', sessions=sessions)

# GET ALL SESSIONS
@app.route('/' + SESSIONS, methods=['GET'])
def get_sessions():
    """
    Protection: None
    Description: Return all sessions.
    """
    if request.method == 'GET':
        try:
            session_limit = int(request.args.get('limit', default=0))
        except (ValueError, TypeError):
            session_limit = 0
            
        session_subject = request.args.get('sessionSubject', default=None, type=str)
        
        # get all sessions 
        query = datastore_client.query(kind=SESSIONS)
        
        # Add filters if provided
        if session_subject:
            query.add_filter('sessionSubject', '=', session_subject)
        
        # Order by startTime descending (most recent first)
        query.order = ['-startTime']
        
        # Get results with limit
        results = list(query.fetch(limit=session_limit if session_limit > 0 else None))
        return_array = []
        
        for r in results:
            r['id'] = r.key.id
            return_array.append({
                'id': r['id'],
                'startTime': r['startTime'],
                'duration': r['duration'],
                'breakTime': r['breakTime'],
                'sessionSubject': r['sessionSubject'],
                'notes': r['notes']
            })
        return return_array
    else: 
        return jsonify(error='Method not recognized')

# # GET A SPECIFIC SESSION with ID
# @app.route('/' + SESSIONS + '/<session_id>', methods=['GET'])
# def get_session(session_id):
#     """
#     Protection: None
#     Description: Return a session.
#     """
#     if request.method == 'GET':
#         # get a specific session 
#         key = datastore_client.key(SESSIONS, int(session_id))
#         session = datastore_client.get(key)
#         return session
#     else: 
#         return jsonify(error='Method not recogonized')

# CREATE A SESSION
@app.route('/' + SESSIONS, methods=['POST'])
def create_session():
    """
    Protection: None
    Description: Create a new session.
    """
    if request.method == 'POST':
        content = request.get_json()
        # return 400 if invalid request body
        if invalid_content(content, SESSION_PROPERTIES):
            return ERROR_BAD_REQUEST, 400
        else:
            #finally post new session
            new_session = datastore.Entity(key=datastore_client.key(SESSIONS))
            new_session.update({
                'startTime': content['startTime'],
                'duration': content['duration'],
                'breakTime': content['breakTime'],
                'sessionSubject': content['sessionSubject'],
                'notes': content['notes']
            })
            datastore_client.put(new_session)
            new_session['id'] = new_session.key.id
            return (new_session, 201)
    else:
        return ERROR_BAD_REQUEST, 400

# UPDATE A SESSION
# Not implemented at this time.

# DELETE A SESSION
@app.route('/' + SESSIONS + '/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    """
    Protection: None
    Description: Delete a session.
    """
    if request.method == 'DELETE':
        # Delete a session
        key = datastore_client.key(SESSIONS, int(session_id))
        datastore_client.delete(key)
        return jsonify({"message": "Session deleted"}), 200
    else:
        return ERROR_BAD_REQUEST, 400

# DELETE ALL SESSIONS
@app.route('/' + SESSIONS, methods=['DELETE'])
def delete_sessions():
    """
    Protection: None
    Description: Clear all sessions
    """
    if request.method == 'DELETE':
        # Delete all sessions
        query = datastore_client.query(kind=SESSIONS)
        sessions = list(query.fetch())
        for session in sessions:
            datastore_client.delete(session.key)
        return jsonify({"message": "All sessions cleared"}), 200
    else:
        return ERROR_BAD_REQUEST, 400

# TEST IF ONLINE 
@app.route('/' + TEST_IF_ONLINE, methods=['POST'])
def test_if_online():
    return jsonify({"message": "Online"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
