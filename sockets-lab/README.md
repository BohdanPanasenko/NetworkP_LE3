# NetworkP_LE3

### TCP Sockets Lab
#### Run Instructions
Run python3 server.py.  
In a new terminal, run python3 client.py.  

Type messages to echo; type exit to quit.  
<img width="690" height="178" alt="image" src="https://github.com/user-attachments/assets/ab92c191-b14a-4321-94d0-96bf93089118" />
<img width="679" height="128" alt="image" src="https://github.com/user-attachments/assets/253ff507-956d-4f2c-b3d7-77a57fd92cb2" />


### TCP Guarantees
TCP ensures reliable, ordered delivery of data so bytes arrive exactly as sent. However, it is a byte stream rather than a message channel, meaning it does not guarantee message boundaries. It is the application's responsibility to manage these boundaries using techniques like delimiters or length prefixes.
