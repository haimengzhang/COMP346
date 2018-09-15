import unittest
import json

import httpclient
import httpclienttest2

class TestHttpClient(httpclienttest2.TestHttpClient):

    def testPostWithParams(self):
        client = httpclient.HttpClient('httpbin.org')
        response = client.doPostWithParams('/post', {'Foo' : 'Bar'})
        data = json.loads(response.body)
        self.assertEquals(data['form']['Foo'], 'Bar')

    def testGetWithParams(self):
        client = httpclient.HttpClient('httpbin.org')
        response = client.doGetWithParams('/get', {'Foo' : 'Bar', 'foo' : 'bar'})
        data = json.loads(response.body)
        self.assertEquals(data['args'], {'Foo' : 'Bar', 'foo' : 'bar'})
    
    def testGetParamEncoding(self):
        client = httpclient.HttpClient('httpbin.org')
        response = client.doGetWithParams('/get', {'$foo' : 'bar &z' })
        data = json.loads(response.body)
        self.assertEquals(data['args'], {'$foo' : 'bar &z' })
    
if __name__ == '__main__':
    unittest.main()
