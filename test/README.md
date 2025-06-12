# 📋 Task Manager API
# 📋 Task Manager API

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)


A simple Flask-based REST API for managing tasks. Built with Python and SQLite.

## 🧪 Test Coverage

The tests in this project ensure that the core functionalities of the Task Manager API work correctly. Covered features include:

- ✅ Creating a task (POST `/tasks`)
- ✅ Retrieving all tasks (GET `/tasks`)
- ✅ Updating a task by ID (PUT `/tasks/<id>`)
- ✅ Deleting a task by ID (DELETE `/tasks/<id>`)
- ✅ Handling invalid requests (e.g. missing title, non-existent ID)

Total: **5 automated tests using Python `unittest`**, located in the `test/` directory.

All tests pass successfully and cover both standard and edge-case scenarios.
