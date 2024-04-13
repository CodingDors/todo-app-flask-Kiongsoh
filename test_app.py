# test_app.py
import unittest
from app import app

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200, "Home page should load with status code 200")
        self.assertIn(b'Add a New Task', result.data, "Home page should contain the 'Add a New Task' form")

    def test_add_task(self):
        result = self.app.post('/', data=dict(task="Test Task"), follow_redirects=True)
        self.assertEqual(result.status_code, 200, "Adding a task should redirect to home with status code 200")
        self.assertIn(b'Test Task', result.data, "The response should contain the added task 'Test Task'")

    def test_remove_task(self):
        self.app.post('/', data=dict(task="Task to Remove"), follow_redirects=True)
        remove_result = self.app.post('/remove', data=dict(task="Task to Remove"), follow_redirects=True)
        self.assertEqual(remove_result.status_code, 200, "Removing a task should redirect to home with status code 200")
        
        home_page_result = self.app.get('/')
        self.assertNotIn(b'Task to Remove', home_page_result.data, "After removal, the task 'Task to Remove' should not be in the response")

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
