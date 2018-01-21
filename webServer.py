######## Making a webserver using BaseHTTPServer Class in Python. See documentation for more.
######## This class use sockets for communication between the server and the client.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# A class to handle out webserver
class webserverHandler(BaseHTTPRequestHandler):
    
    # Will handle all GET request that our server will receive 
    def do_GET(self):
        try:
            # I am handling the webRequest for the url which are ending with 'hello' only
            if self.path.endswith("/hello"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    responseMsg = ""

                    # Response in form of html doc
                    responseMsg += "<html><body>Hello Client! This is Your webServer</body></html>";
                    
                    # Sending Response to the cleint
                    self.wfile.write(responseMsg)
                    
                    # Just for debugging purpose
                    print responseMsg
                    return

        except IOError:

            # If the requested url is not ending with 'hello'
            self.send_error(404, "File Not Found %s!" % self.path)


def main():
    try:
        port = 8080
        
        # This function will create a server on address and port given as argument 1, webserverHandler is a class which will handle the serveri
        server = HTTPServer(('',port), webserverHandler)
        
        print "Web server running on the port %s" % port
        
        # This will let server to listen to any request
        server.serve_forever()

    # To stop the web server by pressing (^ + C) : keyboardInterrupt
    except KeyboardInterrupt:
        print "Web server has been stopped!"
        # To stop the server socket
        server.socket.close()


if __name__ == '__main__':
    main()
