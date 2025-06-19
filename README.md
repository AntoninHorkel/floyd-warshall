# Grafové algoritmy: Teoretický přehled

## 1. Základní terminologie grafů
- **Definice grafu**:
  - **Orientovaný graf**: Hrany mají explicitní směr (A → B ≠ B → A)
  - **Neorientovaný graf**: Hrany nemají směr (A-B ≡ B-A)
  - **Ohodnocený graf**: Hrany mají přiřazenou váhu (např. vzdálenost, cena)

- **Kostra grafu**: Podgraf spojující všechny vrcholy bez cyklů. Minimální kostra minimalizuje součet vah hran.

- **Reprezentace grafů**:
  - **Matice sousednosti**: 2D pole kde `matrix[i][j]` udává váhu hrany z `i` do `j` (nebo speciální hodnotu pro neexistenci hrany)
  - **Seznam sousedů**: Kolekce (slovník/seznam) kde `adj_list[i]` obsahuje dvojice `(soused, váha)`

- **Aplikační domény**:
  - Navigace (optimalizace tras), analýza sítí (sociální, počítačové), projektové plánování

## 2. Problém nejkratší cesty
- **Cíl**: Nalezení cesty mezi dvěma vrcholy s minimálním součtem vah hran
- **Negativní váhy**: Může vést k nekonečnému snižování délky cest při existenci záporných cyklů. Některé algoritmy s nimi neumí pracovat.

## 3. Algoritmy pro hledání nejkratších cest

### a) Dijkstrův algoritmus
- **Princip**: Greedy přístup s prioritní frontou. V každém kroku expanduje vrchol s nejnižší aktuální vzdáleností
- **Omezení**: Funguje pouze pro grafy bez záporných vah
- **Časová složitost**: O((V + E) log V) s prioritní frontou

### b) Bellman-Fordův algoritmus
- **Princip**: Iterativní relaxace všech hran. Vyžaduje |V|-1 iterací pro konvergenci
- **Detekce záporných cyklů**: Možná po |V|-1 iteracích testem další relaxace
- **Časová složitost**: O(V · E)
- **Výhoda**: Zvládá grafy se zápornými vahami (bez záporných cyklů)

### c) Floyd-Warshallův algoritmus
- **Princip**: Dynamické programování řešící všechny páry vrcholů najednou
- **Časová složitost**: O(V³)
- **Vhodné použití**: Husté grafy nebo když je potřeba nejkratší cesty mezi všemi páry vrcholů

## 4. Návrh praktického řešení
- **Zvolený algoritmus**: Floyd-Warshallův algoritmus (pro řešení všech párů)
