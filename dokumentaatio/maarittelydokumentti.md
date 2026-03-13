# Hahmontunnistus

Projektin ohjelmointikielenä käytän pythonia. Olen myös kykenevä vertaisarvioimaan projekteja, jotka ovat toteutettu esimerkiksi Javalla, JavaScriptillä tai projekteja, jotka ovat toteutettu englanniksi.

Vaatimuksesta, että vaativat matriisilaskennan operaatiot täytyy toteuttaa itse, en siis aio hyödyntää NumPy-kirjastoa laskennan operaatioihin, vaan toteutan kaikki tarvittavat matriisit sekä niiden laskennalliset operaatiot Pythonin perusominaisuuksilla, kuten kaksiulotteisilla listoilla.

Toteutan kasvojentunnistuksen ohjeissa mainitulla Eigenface-menetelmällä, jossa hyödynnetään pääkomponenttianalyysiä (PCA). Jotta, tämä onnistuu, täytyy minun siis toteuttaa ainakin seuraavat menetelmät: Matriisioperaatiot, kovarianssimatriisin laskeminen, ominaisarvojen sekä ominaisvektorien laskeminen. Tietorakenteina aion käyttää 2D-listoja eli matriiseja sekä 1D-listoja eli vektoreita. 

Ohjelmalla ratkaisen kuvantunnistusongelman. Ohjelman tavoitteena on ottaa syötteenä kuva, jota algoritmi ei ole aiemmin tunnistanut ja todeta, että kuvassa on ihminen ja mahdollisesti kuka ihminen kuvassa on.

Ohjelma saa siis syötteenä paljon kasvokuvia digitaalisessa muodossa. Nämä annetut syötteet jaetaan harjoitus- sekä testidataan, joista jokainen 2D-kuva litistetään ohjelmassa yhdeksi pitkäksi 1D-vektoriksi, joka sisältää pikselit kuvasta. Näisät muodostetaan algoritmin vaatima datamatriisi.

Jos M on harjoituskuvien lukumäärä, jossa N on yhden kuvan pikselien kokonaismäärä, tällöin kokonais tilavaativuus on O(M * N). Sijaiskovarianssinmatriisin laskenta, jossa optimaalinen sijaiskovarianssimatriisi lasketaan kaavalla: L = A^T * A, jossa A^T on kokoa M x N ja A puolestaan kokoa N x M, muodostaa aikavaativuuden O(M²N). Ominaisarvojen sekä ominaisvektorien laskenta O(M³). Tunnistusvaiheessa, tunnistettavan kuvan pikselit, joita on N kappaletta, heijastetaan laskettuun ominaisavaruuteen, jossa on K-määrä valittuja ominaiskasvoja, kerrotaan K x N, josta muodostuu aikavaativuus O(K * N).

Lähteinä toimii kurssilla tarjotun materiaalin lisäksi: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11286184
https://en.wikipedia.org/wiki/QR_decomposition
https://files01.core.ac.uk/download/pdf/14980993.pdf
https://www.face-rec.org/algorithms/PCA/jcn.pdf
https://en.wikipedia.org/wiki/Eigenface

Aiheen ytimenä toimii pääkomponenttianalyysi (PCA) sekä koneoppiminen ja kaiken sen vaatiman laskennallisen toiminnan toteuttaminen. Paljon kehitysajasta kuluu matriisioperaatioiden kehittämiseen sekä niiden optimoimiseen. 

Suoritan tietojenkäsittelytieteen kandidaatin tutkintoa. Projektin dokumentaatio toteutetaan suomeksi.
