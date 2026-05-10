# Toteutusdokumentti

## 1. Ohjelman yleisrakenne

Ohjelma toteuttaa Eigenfaces-algoritmin (PCA) kokonaan ilman valmiita matriisikirjastoja. Data kulkee kolmessa vaiheessa: esikäsittely, mallin opetus ja tunnistus.

**Esikäsittely**
- `PGM_parser.py` lukee P5-tyyppiset PGM-kuvat, normalisoi pikselit välille 0.0-1.0, jakaa kuvat opetus- ja testidataan (1-7 opetus, 8-10 testaus per henkilö) ja kirjoittaa CSV-tiedostot `data/training_data.csv` ja `data/testing_data.csv`.

**Mallin opetus**
- `Operations/Matrix.py`: oma matriisiluokka (add, subtract, dot, transpose, map).
- `Operations/mean_face.py`: laskee keskiarvokasvon opetusdatasta.
- `Operations/mean_subtraction.py`: rakentaa datamatriisin $A$ (koko $N \times M$), jossa jokainen sarake on keskiarvosta vähennetty kasvovektori.
- `Operations/jacobi_operation.py`: laskee $L = A^T A$ -matriisin ominaisarvot ja -vektorit Jacobin menetelmällä.
- `Operations/sort_eigen.py`: lajittelee ominaisparit laskevaan järjestykseen.
- `Operations/normalize.py`: normalisoi ominaiskasvot yksikköpituiksi.
- `Operations/projection.py`: valitsee top-$K$ ominaiskasvot, projisoi opetusdatan ja muodostaa signatuurit (painovektorit).
- `Operations/model_io.py`: tallentaa ja lataa mallin `data/trained_model.json`-tiedostoon.
- `test.py`: ajaa koko opetusputken ja tallentaa mallin.

**Tunnistus**
- `recognize.py`: lukee yksittäisen PGM-kuvan, projisoi sen ominaisavaruuteen ja tekee kasvo/ei-kasvo -päätöksen rekonstruointi-virheen avulla.
- `Operations/reconstruction.py`: laskee rekonstruktiovirheen.
- `Operations/distance.py`: euklidinen etäisyys lähimmän naapurin haussa.
- `recognize_face.py`: ajaa testidatan läpi ja raportoi tarkkuuden.

## 2. Saavutetut aika- ja tilavaativuudet

Merkit:
- $M$ = opetuskuvien lukumäärä (ORL-datassa 40 henkilöä * 7 kuvaa = 280)
- $N$ = yhden kuvan pikselimäärä (92 * 112 = 10304)
- $K$ = käytettävä ominaiskasvojen määrä (test.py:ssa 50)
- $T$ = testikuvien lukumäärä (40 henkilöä * 3 kuvaa = 120)

**Opetusvaihe**
- Datan lukeminen ja normalisointi: $O(MN)$, tila $O(MN)$.
- Keskiarvokasvon laskenta: $O(MN)$, tila $O(N)$ (käytännön toteutus lukee koko CSV:n muistiin, joten $O(MN)$).
- Matriisi $A$ (keskiarvovähennys): $O(MN)$, tila $O(MN)$.
- $L = A^T A$ (koko $M \times M$): $O(M^2 N)$, tila $O(M^2)$.
- Jacobin ominaisarvot ja -vektorit: pahimmillaan $O(M^3)$, tila $O(M^2)$.
- Ominaisparien lajittelu: $O(M^2)$.
- Ominaiskasvot $U = A V$: $O(N M^2)$, tila $O(NM)$.
- Normalisointi: $O(NM)$.
- Top-$K$ valinta: $O(NK)$, tila $O(NK)$.
- Projisointi opetusdataan (painomatriisi): $O(K N M)$, tila $O(KM)$.

Opetusvaiheen kokonaisaika dominoituu termeista $O(M^2 N)$ ja $O(N M^2)$ (ORL-datalla $N \gg M$).

**Tunnistusvaihe (yksi kuva)**
- Keskiarvovähennys: $O(N)$.
- Projisointi ominaisavaruuteen: $O(KN)$.
- Rekonstruktiovirhe: $O(KN)$ + etäisyys $O(N)$.
- Lähimmän naapurin haku: $O(MK)$.

Yhden tunnistuksen kokonaisaika on $O(KN + MK)$, ja tilavaativuus on $O(N + K + MK)$.

## 3. Suorituskyky- ja O-analyysivertailu

**Sijaiskovarianssinmatriisi (Turk-Pentland -optimointi)**
- Naivi kovarianssi $C = A A^T$ olisi kooltaan $N \times N$, jolloin laskenta on $O(N^2 M)$ ja tila $O(N^2)$.
- Toteutuksessa lasketaan $L = A^T A$ (koko $M \times M$), jolloin laskenta on $O(M^2 N)$ ja tila $O(M^2)$. Tämän jälkeen ominaisvektorit muunnetaan takaisin alkuperäiseen avaruuteen kaavalla $U = A V$.
- ORL-datalla ($N=10304$, $M=280$) ero on merkittävä: $N^2$ on käytännössä liian suuri, kun taas $M^2$ mahtuu muistiin.

**K:n vaikutus**
- Tunnistuksen kustannus pienenee, kun $K$ pienenee: $O(KN + MK)$. Suurempi $K$ parantaa ilmaisukykyä, mutta kasvattaa mallin kokoa ($O(NK)$) ja ajonaikaa.

## 4. Puutteet ja parannusehdotukset

- `PGM_parser.write_data` kirjoittaa vain toisen CSV-tiedoston (training tai testing) `elif`-haaran vuoksi. Parempi on kirjoittaa molemmat aina, jos puuttuvat.
- `mean_face.py` laskee keskiarvokasvon ja tulostaa tietoja jo import-vaiheessa. Tämän voisi siirtää funktiokutsun taakse tai `if __name__ == "__main__"` -lohkoon.
- `test.py` on kiinteä opetusajuri (esim. $K=50$). Kannattaa lisätä komentoriviparametrit ja valintaprosessi $K$:lle (esim. validaatiosetillä).
- Kasvo/ei-kasvo -kynnys (24.0) on kovakoodattu. Sille kannattaisi hakea dataan perustuva raja (ROC/PR-analyysi) ja erottaa se konfiguraatioksi.
- Suorituskyky: kaikki laskenta on puhtaalla Pythonilla. Jos sallittua, NumPy nopeuttaisi moninkertaisesti. Jos ei, dot-operaatiota voi optimoida blokituksella ja minimoida turhat transponoinnit.
- Mallin tallennus JSON-muodossa on iso ja hidas. Binaarinen formaatti (esim. pickle tai oma tiivis muoto) pienentäisi I/O-kustannusta.

## 5. Laajojen kielimallien käyttö

Projektissa hyödynnettiin laajoja kielimalleja dokumentoinnin selkeyttämisessä ja O-analyysin jäsentelyssä. Käytetty malli: GPT-5.2-Codex (GitHub Copilot). Varsinaista algoritmista laskentaa tai koodia ei generoitu mallilla.

## 6. Lähteet

- https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11286184
- https://en.wikipedia.org/wiki/QR_decomposition
- https://files01.core.ac.uk/download/pdf/14980993.pdf
