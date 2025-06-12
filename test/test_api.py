import unittest
from app import app
import json

class TaskApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.post("/tasks", json={"title": "Test Task"})

    def test_create_task(self):
        response = self.client.post("/tasks", json={"title": "Another Task"})
        self.assertEqual(response.status_code, 201)

    def test_list_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_update_task(self):
        # create new task
        resp = self.client.post("/tasks", json={"title": "Test Task"})

        # take the list with task and get the ID
        task_list = self.client.get("/tasks").get_json()
        task_id = task_list[0]["id"]

        # update the task with PUT
        response = self.client.put(f"/tasks/{task_id}", json={"title": "Updated Title"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("updated", response.get_data(as_text=True))

    def test_delete_task(self):
        # create task
        self.client.post("/tasks", json={"title": "Task to Delete"})

        # get the ID of the task
        task_list = self.client.get("/tasks").get_json()
        task_id = task_list[0]["id"]

        # Delete it
        response = self.client.delete(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("deleted", response.get_data(as_text=True))

    def test_update_nonexistent(self):
        response = self.client.put("/tasks/999", json={"title": "Ghost"})
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
