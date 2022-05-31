# PB2-py-sistema-Matematikas_uzdevums_Aleksandrs_Ostrovskis

### Izveidoju programmu, kura palīdz skolotājam izveidot un pārbaudīt testu.

**1.** Mums ir teorija priekš mūsu koda, Es pirms teksta vienā rindā lieku "#", bet jā es gribu tekstu vairākās rindās, man vajag '''   '''   pa trīm opostrofiem augšā un lejā no teksta

**2.** Es importoju os(system) priekš koda, lai cmd viņš būtu rādijies un neaizvērās.

**4.** Es izmantoju funkciju(def), funkciju izveidošanu, funkcijas nosaukumu "skolotaja_uzdevumi_izvade" un parametru(n) kuru ievadīšu.

**5.** Pēc def vajag likt kolu lai norādītos kā tā ir funkcija un nākamā rinda būtu 4 atstarpēm tālāk, tālāk es visu rakstīšu tajā fukcijā.

**6.** Es ievadu četras mainīgas priekš masīva izveidošanai (masīvs ir list, kur glabāsies lietotāja dati) reizinu to uz n, jo n es ievadu, cik uzdevumu skolotājs grib uzdot.

**7.** 130 rindā es ievadiju tikai nulli, priekš pareizo atbildi skaitīšanas un glabāšanas (mainīgais)

**8.** izveidoju ciklu for, lai tas darbotos tik reižu, cik iepriekš ievadīju numuru.
Piemēram:
ievadiju 5 
būs pieci cikli 

* 9. rakstu mainīgu, kura bija iepriekš "skol_jautājumi". 
* 9.1 es ievadu mainīgu un [i] tas norāda un cikla mainīgo, cik reizes mums būs cikls
* 9.2 es ievadu 'input'. Tā ir funkcija priekš tā, lai lietotājs pats ievadītu tekstu.
* 9.3 es ievadu f pirms opostrofiem, lai es varētu rakstīt tekstu un {funkcijas}, bez + un komatiem
* 9.4 rakstu funkcijā i + 1, lai skaitļi ietu pēc kārtas.
1
2
3
4
5

**10.** Ievadu mainīgu atbildes lai es varētu uzrakstīt visas atbildes priekš uzdevumiem jar funkcijām input un pēc mainīgas []

**11.** Ievadu "os.system('cls')", lai pēc tā kā skolotājs ierakstija uzdevumus un atbildes, prikeš skolnieka atbildes izdzēsās.

**12.** Rakstu ciklu for, lai norādi cik būtu ciklu.

**13.** Rakstu print (tas ir izvadīšanas operātors) lai uz ekrāna izvadītos, Piemēram, 
print(f'{j + 1}. Jautājums ir: {skol_jautajums[j]}')
__1.__  1. Jautājums ir: 1+1 
__2.__ 2. Jautājums ir: 2/2
__3.__ 3. Jautājums ir: 3*3

**14** Rakstu mainīgo, kurā glabāsies skolēna ievadītas atbildes. ar funkciju 'input' lietotājs var ievadīt tekstu.
* 14.1 Pēc mainīgas es uzrakstiju skolnieks[j], lai šis mainīgais darbotos un satur to ciklu, kura mainīgais bija j
__1.__ Jūsu atbilde uz 1. jautājumu = 2
__2.__ Jūsu atbilde uz 2. jautājumu = 1
__3.__ Jūsu atbilde uz 3. jautājumu = 9


**15.** Es uzrakstiju funkciju if, tā ir funkcija, kura salīdzina divus nosacījumus. 
* 15.1 es salīdzināju ievadītas skolēna atbildes un skolotājas atbildes
__1.__ 2 == 2, jā  
__2.__ 1 == 1, jā
__3.__ 10 == 9, nē 


**16.** jā atbildes ir vienādas tad mainīgajā "balles" iet + 1 punkts, no kura pēc tam skaitīsies balles.
__1.__ balle + 1
**2.** balle + 1
__3.__ balle + 0

**17.** Es ievadu print(), lai būtu tukša rinda

**18.** Es izvadīšu cik punktus dabūja skolēns un reķināsu, kāda skolēnam ir balle.
- __1.__ balle = 2/3.    skolēns dabūja 7 balles.
* 18.1  Es izsaucu funkciju un rakstu 'int' kurš rāda, kā ievadīt vajad tikai pilnos skaitļus.
* 18.2 funkcija input, lai lietotājs varētu pats ievadīt skaitli.
* 18.3 Šeit lietotājs ievadīs cik būs uzdevumu.
- __1.__ 3 uzdevumi
* 18.4 vienmēr pec funkcijas nosaukuma vajag iekavas, lai funkcija izsauktos.

**19.** os.system('pause'), tas lai cmd vidē mums neaizvērtos.

