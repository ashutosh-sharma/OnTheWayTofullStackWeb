# Follow this to host your own WebServer using python:

## Technologies used:
1. Python 2.7
2. A linux machine/ (windows would also work but I have done it on linux)

## How to make?:
I have used BaseHTTPRequestHandler class of python to create serverSide code.
I am sending a GET request from client side and hadnlign it in the sever side.
For the sake of simplicity, I am handling the url which are ending with 'hello'.
You will find helpful comments in the code, see the code for more.

## How to use?:
1. Download the file from my github.
2. Use terminal to get the python code running:
    ![runwebserver](https://user-images.githubusercontent.com/25898173/35195030-479f93b4-fee3-11e7-8346-8dfbe1cb4dbb.JPG)
    See the message 'web server is running on port 8080'.
3. Use *wget* command to use terminal to send a request to a server:
     You have to open other instance of terminal to check if the server is working or not.
     Now, use *wget* command to request localhost:8080. We will get our file downloaded.Use *cat* command to see whats in that.
    ![clientside](https://user-images.githubusercontent.com/25898173/35195100-6c0b0070-fee4-11e7-96a5-046d72da2b06.JPG)
    *This is client side*
    
    ![serverside](https://user-images.githubusercontent.com/25898173/35195137-df490758-fee4-11e7-88e1-ee4884ae19ea.JPG)
    *This is server side*


# done.
            
