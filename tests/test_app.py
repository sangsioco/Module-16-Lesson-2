import unittest
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_sum(self):
        payload = {'num1': 2, 'num2': 3}
        response = self.app.post('/sum', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 5)
    
    # added for assignment m16l2
    def test_find_by_invalid_result(self):
        # test with invalid result
        invalid_result = 9999
        response = self.app.get(f'/sum/result/{invalid_result}')
        self.assertEqual(response.status_code, 404) 
        self.assertEqual(response.get_json(), {'error': 'Result not found'})

if __name__ == '__main__':
    unittest.main()