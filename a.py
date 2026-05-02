import subprocess
import webbrowser		
import sqlite3										

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def osCmds():                                                                   ### Comandos                    ###
        while True:
            cmd = input("> ").strip()
            
            if not cmd:
                continue 

            parts = cmd.split()

            action = parts[0]
            target = parts[1] if len(parts) > 1 else None

            if action == "exit":
                quest = input("Do you really want to exit?: [y] Yes  [n] No\n")
                if quest == "y":
                    print("Exiting...")
                    break
                else:
                    continue
            
            if action == "help":
                print("Disponible commands:\nopen 'example'  |  exit ")
            
            elif action == "open":
                if not target:
                    print("Disponible programs:\nchrome  |  calc  |  listCreator")
                    continue

                if target == "calc":
                    subprocess.Popen(["calc.exe"])

                elif target == "chrome":
                    chrome()

                elif target == "listCreator":
                    listCreator()

                else:
                    print("Unrecognized application!")

            else:
                print("Invalid command!")
            
def osMainPage():                                                               ### Página inicial              ###
        print("")
        print("="*50)
        print(f"WELCOME TO A OS!")
        print("="*50)
        print("")
        print("Write 'help' to view the disponible commands!")
        osCmds()

def osCreateAc():                                                               ### Criar conta                 ###
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()  
    
    print("")
    print("="*50)
    print("CREATE ACCOUNT")
    print("="*50)
    print("")

    cursor.execute('''

            CREATE TABLE IF NOT EXISTS users(
                        
                        user VARCHAR(50) NOT NULL,
                        password VARCHAR(30) NOT NULL

                        )

        ''')
    conn.commit()

    try:
        user = input("Username: ")
        password = input("Password: ")

        if user or password != "exit":

            cursor.execute('INSERT INTO users (user, password) VALUES (?, ?)', (user, password))
            conn.commit()

            print(f"Account '{user}' created!")

            osLogin()
        else:
            quest = input("Do you really want to exit?: [y] Yes  [n] No\n")
            if quest == "y":
                print("Exiting...")
                return False

    except sqlite3.IntegrityError:
        print("Account already exists!") 

def checkAc():                                                                  ### Verifica se conta existe    ###
    while True:
        q = input("Do you have an account?:\n[y] Yes  [n] No\n")
        if q == "y":
            osLogin()
            break
        elif q == "n":
            osCreateAc()
            break
        else:
            print("")

def osLogin():                                                                  ### Login                       ###
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        print("")
        print("="*50)
        print("ACCOUNT LOGIN")
        print("="*50)
        print("")
        
        attempts = 3
        while attempts > 0:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            
            comptUser = input("Username: ")
            comptPassword = input("Password: ")

            cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", (comptUser, comptPassword))
            result = cursor.fetchone()

            if result:
                osMainPage()
                return True
            else:
                attempts -= 1
                print(f"Invalid credentials! {attempts} attempts remaining.")
    
        print("Too many failed attempts! Exiting...")
        return False

def chrome():                                                                   ### Chrome                      ###
     search = input("Search: ")
     url = f"https://www.google.com/search?q={search}"
     webbrowser.open(url)

def listCreator():                                                              ### Lista                       ###
    listas = {}

    print("")
    print("="*50)
    print("List Creator")
    print("="*50)

    while True:
        comando = input("\n> ").strip().lower()

        if comando == "exit":
            print("Exiting...\n")
            break

        elif comando == "create":
            nome = input("List name: ")

            if nome in listas:
                print("This list alredy exists!")
            else:
                listas[nome] = []
                print(f"List '{nome}' created!")

        elif comando == "add":
            nome = input("List name: ")

            if nome not in listas:
                print("This list doesn't exists!")
            else:
                item = input("Item to add: ")
                listas[nome].append(item)
                print("Item add!")

        elif comando == "view":
            nome = input("List name: ")

            if nome not in listas:
                print("List doesn't exists!")
            else:
                print(f"\nList: {nome}")
                for i, item in enumerate(listas[nome], start=1):
                    print(f"{i}. {item}")

        elif comando == "remove":
            nome = input("List name: ")

            if nome not in listas:
                print("This list doesn't exists!")
            else:
                item = input("Item to remove: ")
                if item in listas[nome]:
                    listas[nome].remove(item)
                    print("Item removido!")
                else:
                    print("Item not found!")

        elif comando == "lists":
            print("\nCreated lists:")
            for nome in listas:
                print("-", nome)

        else:
            print("Disponible commands:")
            print("create | add | view | remove | lists | exit")

def osLogo():																	### Logo                        ###
		print("                                    ⠈⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢀⠀⠀⠀⠀⡆⠀⢠⡄⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠁  ")
		print("              .88888.  .d88888b         ⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣥⣀⣀⣀⣿⣿⣿⣅⣄⣠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋      ")
		print("             d8'   `8b 88.    ''           ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀ ")
		print(" .d8888b.    88     88 `Y88888b.            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ")
		print(" 88'  `88    88     88       `8b            ⠿⠟⠛⠛⠛⠿⠿⠿⢿⣿⣿⣿ ⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠛⠿⠆⠀⠀⠀⠀⠀⠀ ")
		print(" 88.  .88    Y8.   .8P d8'   .8P                      ⠉⠛⠿    ⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		print(" `88888P8     `8888P'   Y88888P                          ⠙⢿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
		print("                                                                           ⣿⠅⠀                     \n")

def OS():																		### OS				            ###

    osLogo()
    checkAc()

OS()																			### Inicia o OS		            ###