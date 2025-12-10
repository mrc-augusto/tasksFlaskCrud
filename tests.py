import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_create_task():
  url = f'{BASE_URL}/tasks'
  payload = {
    'title': 'taskTitle',
    'description': 'taskDescription'
  }
  response = requests.post(url, json = payload)
  assert response.status_code == 201
  response_json = response.json()
  assert 'message' in response_json
  assert 'id' in response_json

def test_get_tasks():
  url = f'{BASE_URL}/tasks'
  payload = {
    'title': 'task title',
    'description': 'task description'
  }
  response = requests.post(url, json = payload)
  task_id = response.json().get('id', 1)

  response = requests.get(url)
  assert response.status_code == 200
  response_json = response.json()
  assert 'tasks' in response_json
  assert 'total' in response_json

  url = f'{BASE_URL}/tasks/{task_id}'
  response = requests.get(url)
  assert response.status_code == 200
  response_json = response.json()
  assert 'id' in response_json
  assert response_json['id'] == task_id

def test_update_task():
  url = f'{BASE_URL}/tasks'
  payload = {
    'title': 'taskToUpdate',
    'description': 'descriptionToUpdate'
  }
  response = requests.post(url, json = payload)
  assert response.status_code == 201
  task_id = response.json().get('id', 1)

  url = f'{BASE_URL}/tasks/{task_id}'
  update_payload = {
    'title': 'new title',
    'description': 'new description',
    'completed': True
  }
  response = requests.put(url, json = update_payload)
  assert response.status_code == 200
  response_json = response.json()
  assert 'message' in response_json
  assert response_json['task']['title'] == update_payload['title']
  assert response_json['task']['description'] == update_payload['description']
  assert response_json['task']['completed'] == update_payload['completed']


def test_delete_task():
  url = f'{BASE_URL}/tasks'
  payload = {
    'title': 'taskToDelete',
    'description': 'descriptionToDelete'
  }
  response = requests.post(url, json = payload)
  assert response.status_code == 201
  task_id = response.json().get('id', 1)

  url = f'{BASE_URL}/tasks/{task_id}'
  response = requests.delete(url)
  assert response.status_code == 200
  assert 'message' in response.json()

  url = f'{BASE_URL}/tasks/{task_id}'
  response = requests.get(url)
  assert response.status_code == 404