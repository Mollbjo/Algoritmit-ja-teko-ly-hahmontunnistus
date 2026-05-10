# Viikkoraportti 6

Käytetyt työtunnit: 13 h

Tällä viikolla sain projektin ohjelmointivaiheen ja ydintoiminnallisuudet onnistuneesti päätökseen. Toteutin mallin tallennuksen ja lataamisen (model_io.py), jotta matemaattisesti raskasta opetusvaihetta ei tarvitse suorittaa jokaisella tunnistuskerralla. Lisäksi ohjelmoin euklidisen etäisyyden laskennan (distance.py) ja varsinaisen tunnistusohjelman (recognize.py), joka projisoi uuden kuvan ominaisavaruuteen ja etsii sille lähimmän vastineen opetetusta tietokannasta.

Ohjelma on edistynyt loistavasti ja ylitti odotukset. Suoritin algoritmin empiirisen testauksen koko 120 testikuvan aineistolla, ja ohjelma saavutti erinomaisen 94,17 % tunnistustarkkuuden (113/120 oikein). Tämä on erittäin vahva tulos alusta asti itse koodatulle Eigenface-toteutukselle.

Opin tällä viikolla, miten koneoppimismallin koulutus- ja päättelyvaiheet (inference) eroavat toisistaan arkkitehtuurillisesti ja suorituskyvyltään. Tuloksia ja virheellisiä ennustuksia analysoimalla opin myös PCA-pohjaisen Eigenface-menetelmän fyysisiä rajoitteita: algoritmi saattaa hämääntyä esimerkiksi silmälasien lisäyksestä tai ilmeiden muutoksista, koska menetelmä nojaa vahvasti pikselitason globaaliin varianssiin.

Seuraavaksi aloitan projektin loppudokumentaation (toteutusdokumentti) kirjoittamisen ja päivitän testausdokumenttiin empiiriset tulokset. Tämän jälkeen aion toteuttaa ohjelmaan vielä yhden lisäominaisuuden, jossa käyttäjä voi syöttää itse ykisttäisen kuvan, joka tunnistetaan joko ihmiseksi tai ei.