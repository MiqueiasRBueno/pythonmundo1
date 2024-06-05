# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num not in lista:
        if c == 0 or num > lista[-1]:
            lista.append(num)
            print('Este valor vai para o final da lista...')
        else:
            pos = 0
            while pos <= len(lista):
                if num < lista[pos]:
                    lista.insert(pos, num)
                    print(f'Este valor foi adicionado na posição {pos} da lista...')
                    break
                pos += 1
print(f"Os valores digitados em ordem foram: {lista}")
