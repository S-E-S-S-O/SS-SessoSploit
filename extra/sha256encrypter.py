import hashlib
import sys                                                



def sha256():
    print('''
        Simple Hash sha256 crypter by Lojacops.
            .  *   -   .   -   .   -   .  *    -  .
          -  * - *insert a shitty text art* -   *    .  
           *    *     .   *   -     *  .  *   .   -  *
        Enter an option:
        1) Crypt word in sha256
        2) Crypt a word in sha256 hexdigest
        3) Exit.
        ''')
    try:    
        while True:
            option = input('\ryour option: ')
            if option == "1":
                e = hashlib.sha256()
                word = input('word to encrypt: ')
                e.update(b"{word}")
                print("Success! here word " + word + " crypted:\n")
                print(e.digest())
            elif option == "2":
                d = hashlib.sha256() 
                wordd = input('word to encrypt: ')
                d.update(b"{wordd}")
                print("Success! here word " + wordd + " crypted:\n")
                print(d.hexdigest())
            elif option == "3":
                print("Goodbye.")
                break
                sys.exit()      
    except:
        print("Error, please retry.")