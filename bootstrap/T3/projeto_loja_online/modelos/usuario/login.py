def logar(usuario, senha):
    d = {}
    with open("userdb.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    try:
        if d[usuario] == senha:
            print("logado com sucesso!")
        else:
            print("senha incorreta!")
    except KeyError:
        print("Usuario incorreto")