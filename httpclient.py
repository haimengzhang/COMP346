import socket
import string
import urllib

class HttpResponse:
    """
        Holds a structured http response.
        You will be responsible for translating an http response
        string into this structure.
    """
    def __init__(self):
        self.statusCode = 200
        self.statusMessage = 'OK'
        self.headers = {}
        self.body = ''
    
    def __repr__(self):
        return (
                'status=%s headers=%s body=%s...' %
                (self.statusCode, self.headers, self.body)
            )
        
class HttpClient:
    def __init__(self, host, port=80):
        """Constructs a new http client."""
        self.host = host
        self.port = port
    
    def doGet(self, path):
        """
            Executes an HTTP GET method and returns the result
            as an HttpResponse object.
        """
        sock = self._writeRequest(self._constructGetRequest(path))
        return self._readResponse(sock)
        
    def doPost(self, path, body):
        """
            Executes an HTTP POST method and returns the result
            as an HttpResponse object.
        """
        sock = self._writeRequest(self._constructPostRequest(path, body))
        return self._readResponse(sock)
    
    def doGetWithParams(self, path, params):
        """
            Executes an HTTP GET method and returns the result
            Params should be a dictionary of unencoded query parameters
            as an HttpResponse object.
        """
        
        return ""
    
    def doPostWithParams(self, path, params):
        """
            Executes an HTTP POST method and returns the result
            Params should be a dictionary of unencoded query parameters
            as an HttpResponse object.
        """
        return ""
    
    def _constructGetRequest(self, path):
        """
            Returns a string containing an HTTP 1.0 GET request
            for self.host and the requested path.
        """
        request = "GET {}  HTTP/1.0 \r\nHost: {}\r\n".format(path,self.host)
        return request
    
    def _constructPostRequest(self, path, body):
        """
            Returns a string containing an HTTP 1.0 GET request
            for self.host and the requested path and body.
        """
        return ""
    
    def _writeRequest(self, request):
        """
            Creates a socket connected to the host and port
            Writes the request out and returns the socket object.
        """
        s = socket.socket()
        s.connect((self.host, self.port))
        s.send(request.encode('utf-8'))
        return s
    
    def _readResponse(self, sock):
        """
            Reads in a response from a socket object.
            Returns a filled-in HttpResponse object.
        """
        # fill in the member variables for the http response object
        # by parsing the responseLines list of strings

        responseLines = self._readResponseStr(sock).split('\r\n')

        #Create a response object
        response = HttpResponse()

        # Get the statusline containing "HTTP/1.0", statusCode and message
        statusLine = responseLines[0].split()


        # Extract HTTP/1.0 200 OK from the statusLine
        httpType = statusLine[0]
        response.statusCode = statusLine[1]
        response.statusMessage = statusLine[2]

        # Create a response header dictionary
        response.headers = {}
        # Create a list to collect header strings, e.g. "Content-Type: text/html"
        headersList = []
        
        # Fill in the headerList by appending the items before the blank line.
        i = 1
        while responseLines[i]!= '\r\n':
            headersList.append(responseLines[i]+'\r\n')
            i =+ 1

        # Take the blankline, use it later to build the response
        blankLine = (responseLine[i])

        # Fill the response body
        response.body = responseLines[i+1]

        # Put headers to dictionary, by splitting each of the header string into "key" and "value" strings.
        for header in headersList:
            header.split(":\s")
            response.headers[header[0]] = header[2]

        response = response.statusCode +blankLine+response.headers+response.body
        print(response)

        return response

    
    def _readResponseStr(self, sock):
        """
            Reads in a response from a socket object.
            Returns the string contents of the response.
        """
        # Reads the response.
        # Since we are using HTTP 1.0, we can read until EOF
        bytesRead = 'foo'
        response = ''        
        while len(bytesRead) > 0: 
            bytesRead = sock.recv(1024)
            response += bytesRead.decode('utf-8')
        return response  
    
if __name__ == '__main__':
    client1 = HttpClient('www.npr.org')
    # request = client1._constructGetRequest(client1.host)
    # sock = client1._writeRequest(request)
    # print(client1._readResponse(sock))

    # print(client1._readResponse())
    print(client1.doGet('/index.html'))
    # client1 = HttpClient('webapps.macalester.edu')
    # request = client1._constructGetRequest(client1.host)
    # sock = client1._writeRequest(request)
    # print(client1._readResponse(sock))
    # print(client1.doPost('/directory/search.cfm', 'Name=kyle'))

    
