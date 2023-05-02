import csv

async def verificar_usuario(username: str, password: str) -> bool:    
    with open('app/db/usuarios.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        headers = next(reader)
        print(username, password)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Logueado") 
                               
                return True
        return False