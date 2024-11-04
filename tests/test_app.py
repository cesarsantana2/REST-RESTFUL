import unittest
import json
import os
from src.app import app, save_todos

class TodoApiTest(unittest.TestCase):
    def setUp(self):
        # Limpar o arquivo todos.json antes de cada teste
        with open('todos.json', 'w') as file:
            json.dump([], file)

        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Limpar o arquivo todos.json após cada teste
        with open('todos.json', 'w') as file:
            json.dump([], file)

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])  # Espera-se que esteja vazio inicialmente

    def test_create_todo(self):
        response = self.app.post('/todos', json={"task": "Test Task", "completed": False})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Task", response.get_data(as_text=True))

        # Verificar se o todo foi salvo corretamente no arquivo
        with open('todos.json', 'r') as file:
            todos = json.load(file)
            self.assertEqual(len(todos), 1)
            self.assertEqual(todos[0]['task'], "Test Task")

    def test_update_todo(self):
        # Cria uma tarefa para atualizar
        self.app.post('/todos', json={"task": "Old Task", "completed": False})

        # Atualizar a tarefa
        response = self.app.put('/todos/1', json={"task": "Updated Task", "completed": True})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated Task", response.get_data(as_text=True))

        # Verificar se a tarefa foi atualizada no arquivo
        with open('todos.json', 'r') as file:
            todos = json.load(file)
            self.assertEqual(todos[0]['task'], "Updated Task")
            self.assertTrue(todos[0]['completed'])

    def test_delete_todo(self):
        # Cria uma tarefa para deletar
        self.app.post('/todos', json={"task": "Task to Delete", "completed": False})

        # Deletar a tarefa
        response = self.app.delete('/todos/1')
        self.assertEqual(response.status_code, 204)

        # Verificar se a tarefa foi removida do arquivo
        with open('todos.json', 'r') as file:
            todos = json.load(file)
            self.assertEqual(len(todos), 0)

if __name__ == '__main__':
    unittest.main()
