# NetworkP_LE3

TCP Sockets Lab
Run Instructions
Run python3 server.py.  

In a new terminal, run python3 client.py.  

Type messages to echo; type exit to quit.  

## TCP Guarantees
TCP ensures reliable, ordered delivery of data so bytes arrive exactly as sent. However, it is a byte stream rather than a message channel, meaning it does not guarantee message boundaries. It is the application's responsibility to manage these boundaries using techniques like delimiters or length prefixes.