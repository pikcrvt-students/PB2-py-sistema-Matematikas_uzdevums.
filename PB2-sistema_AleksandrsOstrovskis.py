'''
Izveidoja: Aleksandrs Ostrovskis DP1-1

Programma palīdz matemātikas skolotājai izveidot un pārbaudīt testu skolēniem
'''

# Teorija prikeš uzdevumiem programmā

faila_mainigais = open('teory.txt')
print( faila_mainigais.read())
faila_mainigais.close


import os


def skolotaja_uzdevumi_izvade(n):

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

    for j in range(n):    
        print(f'{j + 1}. Jautājums ir: {skol_jautajums[j]}')        # jautājumu printēšana priekš skolēna
        skolnieks[j] = input(f'Jūsu atbilde uz {j + 1}. jautājumu = ')      # skolnieks ievada atbildi testā
        if skolnieks[j] == atbildes[j]:
            balles += 1

    print()
    print(f'Skolnieks saņēma {balles}. punktus.', end=" ")       # balles izvade un atzīme skolotājam
    print(f'Tas ir {round((balles)/n * 10)}. balles.')

skolotaja_uzdevumi_izvade(int(input('Izvēlaties cik jūs gribat uzdevumus: ')))      # funkcijas izsaukšana

os.system('pause')
   