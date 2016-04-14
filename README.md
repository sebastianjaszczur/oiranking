# Badanie losowości Olimpiady Informatycznej

**tl;dr**
Zrobiłem wykresy pomiędzy wynikiem poszczególnych osób na różnych etapach OI w różnych latach,
żeby zobaczyć jak bardzo wyniki są losowe. Wyszły bardzo losowe.
**Niżej są wykresy.**

**Ogólnie.**
Zawsze wydawało mi się, że OI daje mało miarodajne wyniki.
Nawet nie chodzi o to jak bardzo wynik z OI koreluje z produktywnością w pracy czy podobnymi - ale,
że nawet w obrębie samych zawodów losowość jest bardzo duża.
Żeby to sprawdzić chciałem porównać wynik konkretnych osób na dwóch kolejnych etapach OI
(najlepiej na 2. i 3. etapie, bo są najbardziej podobne)
i zobaczyć jak bardzo korelują.

**Metodyka.**
Żeby mieć więcej danych wziąłem wiele edycji OI (od XI do XXII edycji włącznie), więc nie mogłem porównać
wyników tak po prostu (bo rozkład punktów na różnych edycjach był... różny).
Więc np. jeśli porównywałem 2. i 3. etap to wziąłem wszystkie osoby, które były na obu rankingach i miały określoną
pozycję na tym rankingu. Dla tych osób wyznaczyłem nowy ranking (zawierający tylko te osoby), a każdą osobę
przedstawiłem jako punkt na wykresie (przeskalowana pozycja na 2. etapie, przeskalowana pozycja na 3. etapie) -
gdzie pozycję przeskalowałem liniowo tak, żeby najlepszy zawodnik miał "pozycję" 1, a najgorszy 0.
(Tak, żeby można było porównywać pozycje z różnych edycji, gdzie mogła być różna liczba zawodników).

**Dane i skrypty.**
  - Dane, czyli rankingi wziąłem z [oi.edu.pl](https://oi.edu.pl/). (są w folderze raw_html; wygenerowane przez download.py).
  - Parsowanie jest w preprocess.py; z powyższych plików html tworzy data.json z rankingami w poszczególnych edycjach/etapach.
  - Tworzenie samych wykresów jest w generate.py.

**Moja interpretacja i krytyka.** Wyniki z OI wydają się zaskakująco losowe (korelacja poniżej 0.4; patrz: wykresy),
nawet mimo tego, że losowości można było się spodziewać. Oznaczałoby to, że w dużej części OI to gra losowa, co nie jest raczej
efetem pożądanym. Istnieją jednak czynniki, które obniżają korelację, a które losowe nie są:
  - Korelacja między 1 etapem a 2 lub 3 musi być mniejsza, bo zawody te mają inną formę
(1 etap trwa miesiąc i rozwiązuje się zadania w domu). Jednak forma 2 i 3 etapu jest praktycznie taka sama.
  - Inny dobór zadań - zadania na dalszych etapach są trudniejsze i mogą przez to wymagać innych umiejętności.
  - Inna presja - niektórzy zawodnicy mogą czuć mniejszą lub większą presję na poszczególnych etapach.
  - Trening zawodników pomiędzy poszczególnymi etapami.

Ciekawe byłoby zmierzyć w jakiś sposób powyższe czynniki tak, żeby oddzielić wpływ losowści (a więc czegoś niepożądanego w konkursie)
od czynników zamierzonych przez organizatorów konkursu. Ciekawym zagadnieniem też byłoby porównanie losowości wyników w OI z innymi
konkursami algorytmicznymi, innymi olimpiadami lub zawodami sportowymi.

**Wykresy**

![Wykres miejsc 2 do 3 etapu](charts/oi_2_3.png?raw=true "wow, korelacja taka mała, losowo bardzo, wow")
![Wykres miejsc 1 do 2 etapu](charts/oi_1_2.png?raw=true "wow, korelacja taka mała, losowo bardzo, wow")
![Wykres miejsc 1 do 3 etapu](charts/oi_1_3.png?raw=true "wow, korelacja taka mała, losowo bardzo, wow")
