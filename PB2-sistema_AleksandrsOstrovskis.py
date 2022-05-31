'''
Izveidoja: Aleksandrs Ostrovskis DP1-1

Programma palīdz matemātikas skolotājai izveidot un pārbaudīt testu skolēniem
'''

# Teorija prikeš uzdevumiem programmā

#Saskaitīšana:
'''Skaitļus, kurus saskaita, sauc par saskaitāmajiem.
 
Saskaitīšanas rezultātu sauc par summu. 
SASKAITĀMAIS + SASKAITĀMAIS  = SUMMA
 
Par summu sauc arī izteiksmi, kurā saskaita:
Piemērs:
2 + 4 + 5
d + 8
4 + 12 : 4  (ievēro - saskaitīšana ir pēdējā darbība!)

Likumi

Saskaitāmos drīkst pārvietot, summa no tā nemainās.
Piemērs:
2 + 4 = 4 + 2
 
3 + 4 + 7 + 6 = 3 + 7 + 4 + 6 
Saskaitāmos drīkst savienot, summa no tā nemainās.
( 9 + 3 ) + 7 = 9 + (3 + 7 ). Šajā piemērā izdevīgāk vispirms saskaitīt (3 + 7)
Piemērs:
Aprēķini summu 26 + 7 + 4 + 13 izdevīgākā veidā!
 
26 + 7 + 4 + 13 = (26 + 4) + (7 + 13) = 30 + 20 = 50 
 
Šādi būtu daudz grūtāk: 26 + 7 + 4 + 13 = 33 + 4 + 13 = 37 + 13 = 50
'''

#Starpība
'''
Mazināmais - skaitlis, no kura atņem.
 
Mazinātājs - skaitlis, kuru atņem.
 
Starpība - atņemšanas rezultāts.

Atņemšanas paņēmieni
Bez pārejas citā desmitā
 
Piemērs:
Vispirms jātņem desmitus un tikai pēc tam vienus
39 - 12: 12 = 10(desmitie) un 2(vienie)
39 - 12 = 39 - 10 - 2 = (39 - 10) - 2 = 29 - 2 = 27
      
   vai
 
Atņem atsevišķi desmitus un atsevišķi vienus
 
39 - 12 = (30 - 10) + (9 - 2) = 20 + 7 = 27 
 
Ar pāreju citā desmitā 
 
Piemērs:
Aprēķini starpību 37 - 9
Vispirms sadali vienus tā, lai, atņemot pirmo ciparu, būtu pilni desmiti
      
37 - 9 = 37 - 7 - 2 = (37 - 7) - 2 = 30 - 2 = 28
'''

#Reizināšana
'''
 Vienādu skaitļu saskaitīšanu var aizstāt ar reizināšanu
3⋅4=12
3 reizināt ar 4 ir 12.

3 + 3 + 3 + 3 = 12

Pirmais skaitlis tas nozīmē ko mēs reizināsim.
Otrais skaitlis nozīme cik reizes mēs pirmo skaitli reizināsim.
 
Reizināšana ar nulli (0)
1⋅6=1+1+1+1+1+1=6
1⋅6=6
Jebkuru skaitli reizinot ar 1,iegūst to pašu skaitli.
Skaitļa 0 reizināšana
 
0⋅5=0+0+0+0+0=0
0⋅5=0
Jebkuru skaitli reizinot ar 0, iegūst 0.
'''

#Dalīšana
'''
6 : 3 = 2
6  DALĪT  AR  3  IR  2
 
DALĀMAIS  :  DALĪTĀJS  =  DALĪJUMS 
                                              
Lai prastu dalīt, ir jāzina reizrēķins.
 
Dalīšanas pareizību pārbauda ar reizināšanu.  
Piemērs:
  6:3=2,jo 2⋅3=6
  42:7=6,jo 6⋅7=42
'''



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
   