while True:
    try:
        x = int(input("Digite um valor:"))
    except ValueError:
        print("Digite apenas números")
        x = 0
    duzentos = 0
    cem = 0
    cinquenta = 0
    vinte = 0
    dez = 0
    cinco = 0
    dois = 0
    um = 0
    while x != 0:
        if x >= 200:
            x-= 200
            duzentos += 1
        elif x >= 100:
            x -= 100
            cem += 1
        elif x >= 50 and x < 100:
            x-= 50
            cinquenta += 1
        elif x >= 20 and x < 50:
            x-= 20
            vinte +=1
        elif x>= 10 and x < 50:
            x -= 10
            dez += 1
        elif x >= 5 and x < 10:
            x -= 5
            cinco +=1
        elif x >=2 and x < 5:
            x -= 2
            dois += 1
        else:
            x -= 1
            um += 1
    print(f"{duzentos} notas de 200\n"
          f"{cem} notas de 100\n"
          f"{cinquenta} notas de 50\n"
          f"{vinte} notas de 20\n"
          f"{dez} notas de 10\n"
          f"{cinco} notas de 5\n"
          f"{dois} notas de 2\n"
          f"{um} moedas de 1\n")