objetos = ('LÁPIS.............................R$\033[33m1,75\033[m',
           'CADERNO..........................R$\033[33m32,00\033[m',
           'ESTOJO............................R$\033[33m8,00\033[m',
           'PAPEL ALMAÇO......................R$\033[33m5,46\033[m',
           'BORRACHA..........................R$\033[33m3,45\033[m',
           'CANETA............................R$\033[33m2,00\033[m')
tabela = ('{:^48}'.format('\033[32;1mTABELA DE PREÇOS\033[m'))
print('-' * 40)
print(tabela)
print('-' * 40)
for ob in objetos:
    print(ob)
