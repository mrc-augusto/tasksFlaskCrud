from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(
    id=task_id_control,
    title=data['title'],
    description=data.get('description', ''),
  )
  task_id_control += 1
  tasks.append(new_task)
  return jsonify({'message': 'Nova tarefa criada com sucesso!'}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
  total_tasks = len(tasks)
  task_list = [task.to_dict() for task in tasks]

  output={
    'tasks': task_list,
    'total': total_tasks
  }
  return jsonify(output), 200

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for task in tasks:
    if task.id == id:
      return jsonify(task.to_dict())
  return jsonify({'message': 'Tarefa não encontrada'}), 404
  
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  data = request.get_json()
  for task in tasks:
    if task.id == id:
      task.title = data.get('title', task.title)
      task.description = data.get('description', task.description)
      task.completed = data.get('completed', task.completed)
      return jsonify({
        'message': 'Tarefa atualizada com sucesso!',
        'task': task.to_dict()
        }), 200
  return jsonify({'message': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  task_to_delete = None
  for task in tasks:
    if task.id == id:
      task_to_delete = task
  
  if not task_to_delete:
    return jsonify({'message': 'Tarefa não encontrada'}), 404
  
  deleted_task = task_to_delete.to_dict()
  tasks.remove(task_to_delete)
  return jsonify({
    'message': 'Tarefa deletada com sucesso!',
    'deleted_task': deleted_task
  }), 200

if __name__ == '__main__':
  app.run(debug=True)