from flask import Flask, request, jsonify
from models import Task
from database import (
    init_db,
    get_all_tasks,
    add_task,
    update_task_in_db,
    delete_task_from_db
)

app = Flask(__name__)
init_db()

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_all_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    task = Task(title=data["title"])
    add_task(task)
    return jsonify({"message": "Task created"}), 201
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    updated = update_task_in_db(task_id, data["title"])
    if not updated:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task updated"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = delete_task_from_db(task_id)
    if not deleted:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True)
