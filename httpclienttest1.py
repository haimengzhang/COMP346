import unittest
import httpclient

class TestHttpClient(unittest.TestCase):
    
    def setUp(self):
        pass

    def testGetMethod(self):
        client = httpclient.HttpClient('www.shilad.com', 80)
                
        response = client.doGet('/nonExistentPage')
        self.assertEquals(response.statusCode, 404)
        self.assertEquals(response.statusMessage.lower(), 'not found')

        response = client.doGet('/index.html')
        self.assertEquals(response.statusCode, 200)
        self.assertEquals(response.statusMessage, 'OK')
        self.assertEquals(response.headers['Content-Type'], 'text/html; charset=UTF-8' )
        self.assertTrue(response.body.find('ssen@macalester.edu') > 0)
    
if __name__ == '__main__':
    unittest.main()
