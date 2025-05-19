# Função que implementa o AFD
def e_numero(lexema):
    # Variável que informa o estado corrente
    estado = 'q0'
    # Variável que vai conter o lexema retornado
    numero = ''
    # Índice pra percorrer a cadeia
    i = 0

    # O laço verifica cada caractere que foi informado no lexema
    while i < len(lexema):
        c = lexema[i]

        # Estado q0
        if estado == 'q0':
            if c in "-":
                numero += c
                estado = 'q1'

            elif c.isdigit():
                numero += c
                estado = 'q2'
    
        # Estado q1
        elif estado == 'q1':
            if c.isdigit():
                numero += c
                estado = 'q2'
            else:
                estado = 'q1'
        
        # Estado q2
        elif estado == 'q2':
            if c.isdigit():
                numero += c
                estado = 'q2'
            elif c in ",":
                numero += c
                estado = 'q3'
            else:
                estado = 'q5'
        
        # Estado q3
        elif estado == 'q3':
            if c.isdigit():
                numero += c
                estado = 'q4'
            else:
                estado = 'q5'
        
        # Estado q4
        elif estado == 'q4':
            if c.isdigit():
                numero += c
                estado = 'q4'
            else:
                estado = 'q5'

        # Estado q5
        elif estado == 'q5':
            break

        i += 1

    if estado == 'q2' or estado == 'q4' or estado == 'q5':
        print("Entrada aceita")
        return numero
    else:
        print("Nenhum token foi reconhecido")
        return None


# Fornecendo a entrada
cadeia = input("Forneça uma entrada: ")

print(f"{e_numero(cadeia)}")