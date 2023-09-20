WebServer.py and simpleHTML.html README
---------------------------------------

Overview
--------
This README explains how to run a simple web server using Python 3 and how to access an HTML file through this server.

Files Included
--------------
- WebServer.py: The Python script for the web server.
- simpleHTML.html: A simple HTML file to be served by the web server.

Requirements
------------
- Python 3.x installed on your machine.

Steps to Run the Web Server
---------------------------
1. Place Files in Same Directory: Make sure WebServer.py and simpleHTML.html are in the same directory.
2. Open Terminal: Open a terminal and navigate to the directory where WebServer.py and simpleHTML.html are located.
3. Run Python Script: Type "python WebServer.py" and hit Enter to run the web server. You should see a message saying "Web server is active on port 8080".
4. Access HTML File:
    - On the Same Machine: Open a web browser and go to http://localhost:8080/simpleHTML.html.
    - On a Different Machine: Open a web browser and go to http://[Server's IP Address]:8080/simpleHTML.html.
5. View HTML Content: The content of simpleHTML.html should be displayed in the web browser.
6. Error Handling: If you try to access a file that doesn't exist, you'll get a "404 Not Found" message.

To Stop the Web Server
-----------------------
- Simply close the terminal window.
