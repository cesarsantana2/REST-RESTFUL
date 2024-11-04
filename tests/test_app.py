import unittest
from src.app import app

class TodoApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        response = self.app.post('/todos', json={"task": "Test Task", "completed": False})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Task", response.get_data(as_text=True))

    def test_update_todo(self):
        # Test updating a task that exists
        response = self.app.put('/todos/1', json={"task": "Updated Task", "completed": True})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated Task", response.get_data(as_text=True))

    def test_delete_todo(self):
        # Test deleting a task
        response = self.app.delete('/todos/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

