'''
Izveidoja: Aleksandrs Ostrovskis DP1-1

Programma palīdz matemātikas skolotājai izveidot un pārbaudīt testu skolēniem
'''

# Teorija prikeš uzdevumiem programmā

faila_mainigais = open('teory.txt')
print( faila_mainigais.read())
faila_mainigais.close


import os
from time import sleep


print('No sākuma būs jautājumi bez atzīmes! ')

pareizas_atbildes = 0
def saskaitisana_teorija():

    global pareizas_atbildes
    print('3 + 3 = ?')
    skolnieka_atb = int(input('Ievadiet atbildi uz augstāk uzdoto jautājumu: '))
    if skolnieka_atb == 6:
        pareizas_atbildes += 1
        print('Pareiza atbilde\n')
    else:
        print('Nepareizi\n')
    


def atnemsanas_teorija():

    global pareizas_atbildes
    print('23 - 11 = ?')
    skolnieka_atb = int(input('ievadiet atbildi uz augstāk uzdoto jautājumu: '))
    if skolnieka_atb == 12:
        print('Pareiza atbilde\n')
        pareizas_atbildes += 1
    else:
        print('Neparezi\n')


def reizinasanas_teorija():

    global pareizas_atbildes
    print('6 * 7 = ?')
    skolnieka_atb = int(input('ievadiet atbildi uz augstāk uzdoto jautājumu: '))
    if skolnieka_atb == 42:
        print('Pareiza atbilde\n')
        pareizas_atbildes += 1
    else:
        print('Nepareizi\n')
    

def dalisanas_teorija():

    global pareizas_atbildes
    print('64 / 8 = ?')
    skolnieka_atb = int(input('ievadiet atbildi uz augstāk uzdoto jautājumu: '))
    if skolnieka_atb == 8:
        print('Pareiza atbilde\n')
        pareizas_atbildes += 1
    else:
        print('Nepareizi\n')
    print(f'Jūs atbildejat pareizi uz {pareizas_atbildes} jautājumiem.')
    os.system('pause')
    os.system('cls')


def skolotaja_tests(n):
    

    """
    jautājumu ievadīšana:
    skolēns ievada atbildi.

    >>> 15 + 25
    40
    >>> 19 - 11
    8
    >>> 8 * 9
    72
    >>> 9 / 3
    3.0
    """

    atbildes = [0] * n
    skol_jautajums = [0] * n
    skolnieks = [0] * n
    balles = 0                      # skolēna punkti, kuri skaitīsies ballēs

    for i in range(n):
        skol_jautajums[i] = input(f'Skolotāja uzdevums {i + 1}. ')      # skolotājs ievada jautājumus
        atbildes[i] = input('Skolotāja ievada parteizas atbildes:  ')       # skolotājs ievada atbildes pie jautājumiem

    os.system('cls')
    print('Tagad būs tests uz atzīmi! ')

    for j in range(n):    
        print(f'{j + 1}. Jautājums ir: {skol_jautajums[j]}')        # jautājumu printēšana priekš skolēna
        skolnieks[j] = input(f'Jūsu atbilde uz {j + 1}. jautājumu = ')      # skolnieks ievada atbildi testā
        if skolnieks[j] == atbildes[j]:
            balles += 1

    print()
    print(f'Skolnieks saņēma {balles}. punktus.', end=" ")       # balles izvade un atzīme skolotājam
    print(f'Tas ir {round((balles)/n * 10)}. balles.')

saskaitisana_teorija()
atnemsanas_teorija()
reizinasanas_teorija()
dalisanas_teorija()
skolotaja_tests(int(input('Izvēlaties cik jūs gribat uzdevumus: ')))      # funkcijas izsaukšana

os.system('pause')