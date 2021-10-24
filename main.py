import os
import threading
import time
import socket
import sys
import base64
from extra.sha256encrypter import sha256
from extra.reqinfo import op


modules = ["asyncio", "discord", "requests", "json", "webbrowser", "nmap"]
for library in modules:
    try:
        import asyncio, discord, requests, json, proxygen, webbrowser
        from colors import *
        from itertools import cycle
        from datetime import datetime
    except ImportError:
        os.system(f"pip install {library}")

proxies = proxygen.get_proxies()
proxy_pool = cycle(proxies)

class cmds():
    def repl(argument = None):
        if argument == None:
            print("\nInput something.")
        else:
            webbrowser.open(f"https://www.google.com/search?q={argument}+site%3Areplit.com&oq=sesso+site%3Areplit.com&aqs=chrome..69i57.6712j0j7&sourceid=chrome&ie=UTF-8")
    def http_server():
        port = input("Please tell the port you want to listen on \n")
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ("localhost", port)
        print("Server started")
        sock.bind(server_address)

        sock.listen(1)

        while True :
            print ("Waiting for a connection")
            connection, client_address = sock.accept()
                try:
                    client_address = str(client_address)
                    print("We got a connection from" + client_address)

                    while True:
                        data = connection.recv(16)
                        data = str(data)
                        print ("received \n "+ data)
                        if data:
                            print ("sending data back to the client")
                            connection.send(b'Hello Client !!')
                        else:
                            print("no more data from" + client_address)
                            break
                
                finally:
                    # Closing the connection
                    #connection.close()
                print("Done")
    def b64(argument = None):
        if argument == None:
            print("\nInput something.")
        else:
            m = input("Encode or Decode? (e/d) >")
            if m == "e":
                b = base64.b64encode(argument.encode("utf-8"))
                print(b)
            elif m == "d":
                try:
                   t = base64.b64decode(argument.encode("utf-8"))
                   print(t)
                except:
                    print("Something went wrong")
            else:
                print("Invalid option")



class SS():
    def options():
        a = """
1 - repl [Searches anything on replit]
2 - sha256 [Sha256 encrypter tool]
3 - http [Start an HTTP server]
4 - base64 [Encodes and decodes in base64]
5 - reqinfo [Gets the info about a request]
"""
        print(a)
    def sesso():
        print("""%s
                                                                                                                       
                                                                                                                       
  .--.--.                                               .--.--.               ,--,                       ___            
 /  /    '.                                            /  /    '. ,-.----.  ,--.'|              ,--,   ,--.'|_          
|  :  /`. /                                    ,---.  |  :  /`. / \    /  \ |  | :     ,---.  ,--.'|   |  | :,'         
;  |  |--`              .--.--.    .--.--.    '   ,'\;   |  |--`  |   :    |:  : '    '   ,'\ |  |,    :  : ' :         
|  :  ;_       ,---.   /  /    '  /  /    '  /   /   |   :  ;_    |   | .\ :|  ' |   /   /   |`--'_  .;__,'  /          
 \  \    `.   /     \ |  :  /`./ |  :  /`./ .   ; ,. : \  \    `. .   : |: |'  | |  .   ; ,. :,' ,'| |  |   |           
  `----.   \ /    /  ||  :  ;_   |  :  ;_   '   | |: :  `----.   \|   |  \ :|  | :  '   | |: :'  | | :__,'| :           
  __ \  \  |.    ' / | \  \    `. \  \    `.'   | .; :  __ \  \  ||   : .  |'  : |__'   | .; :|  | :   '  : |__         
 /  /`--'  /'   ;   /|  `----.   \ `----.   \   :    | /  /`--'  /:     |`-'|  | '.'|   :    |'  : |__ |  | '.'|        
'--'.     / '   |  / | /  /`--'  //  /`--'  /\   \  / '--'.     / :   : :   ;  :    ;\   \  / |  | '.'|;  :    ;        
  `--'---'  |   :    |'--'.     /'--'.     /  `----'   `--'---'  |   | :   |  ,   /  `----'  ;  :    ;|  ,   /         
             \   \  /   `--'---'   `--'---'                      `---'.|    ---`-'           |  ,   /  ---`-'          
              `----'                                               `---`                      ---`-'                   

%s                                                                                                                      
                                     [%s+%s] Made by %sLojacops%s and %sTakaso%s [%s+%s]

""" % (green(), reset(), green(), reset(), cyan(), reset(), blue(), reset(), green(), reset()))
        while True:
            opt = input("""[ %s@sesso%s:%s~%s$ """ % (magenta(), reset(), blue(), reset()))
            if opt == "help":
                SS.options()
            elif opt.startswith("repl"):
                repl_arg = opt.replace("repl", "")
                cmds.repl(repl_arg)
            elif opt == "sha256":
                sha256()
            elif opt == "http":
                cmds.http_server()
            elif opt.startswith("base64"):
                base64_arg = opt.replace("base64", "")
                cmds.b64(base64_arg)
            elif opt.startswith("reqinfo"):
                op()
            else:
                os.system(opt)
            


if __name__ == "__main__":
    SS.sesso()
