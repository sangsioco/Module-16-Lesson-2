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
    
    #added for assignment m16l2
    def test_find_by_invalid_result(client):
    #test with invalid result value
        invalid_result = 9999  
        response = client.get(f'/sum/result/{invalid_result}')
        assert response.status_code == 200
        assert response.get_json() == []

if __name__ == '__main__':
    unittest.main()