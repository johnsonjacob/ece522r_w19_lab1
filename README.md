# Lab 1 -- HTTP Server

## Goals

- Get experience with the HTTP protocol through parsing a HTTP request and building a HTTP response
- Understand TCP ports

## Description

Write a simple HTTP server that can serve up any file. A real web browser (such as Chrome) should be able to make a request to your server and display a webpage. I've provided some boilerplate code in Python. You are welcome to do this lab in a different programming language, but I will only be able to help debug for C, C++, and Python. Your program must use TCP sockets and not a library that provides HTTP functionality. I want you to parse the HTTP request and build the HTTP response yourself! The server does not need to be multi-threaded or handle multiple requests at once (though you are welcome to implement that if you would like).


## Requirements

- [ ] Point a web browser to `http://localhost:8080/page.html` and the webpage should show.
- [ ] If you request a file does not exist (e.g. `http://localhost:8080/fdfasd.html`), a proper error message is returned (`HTTP/1.1 404 File Not Found`)
- [ ] Provide a command line option to change the port that your server is running on


## Testing

To test your server, use a web browser to to request a file. For the example files I gave you, you would enter `http://localhost:8080/page.html`. The web browser will take care of creating an HTTP GET request for the page and send it to your server.


## Grading

See Testing section.


## Resources

[HTTP Message Format](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Message_format)

[netcat](http://netcat.sourceforge.net) for debugging. netcat (or nc) allows you to open a raw TCP socket to a server. From there, you can manually enter in the HTTP request and see how your server response. This is installed on most Linux computers.


## Troubleshooting

"Address already in use" error. TCP sockets have timers set up so that the port that the socket was bound to is not immediately available. This happens when your server crashes without properly closing down the socket. To work around this issue, use a different port.
