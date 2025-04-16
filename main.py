from conversor import SHA256

checar = 1

if not checar:
    with open("arquivos/joazinho.png", "rb") as file:
        sha = SHA256(file.read())
    
        chave = sha.criptografar()
            
    with open("chaves/joazinho.chave", "w") as file:
        file.write(chave)

    
else:
    
    with open("chaves/joazinho.chave", "r") as file:
        chave = file.read()

    with open("arquivos/joazinho.png", "rb") as file2:    
        sha = SHA256(file2.read())
    
        resp = sha.criptografar()
    
        if (resp != chave):
            print("Joazinho errado")
        else:
            print("Joazinho certo")
            

