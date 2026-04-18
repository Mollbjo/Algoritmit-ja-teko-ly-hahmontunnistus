# Käyttöohje

Ohjelma on alusta alkaen Pythonilla toteutettu kasvojentunnistusalgoritmi, joka hyödyntää Eigenface-algoritmia (PCA). Kaikki on toteutettu ilman NumPy- tai muita vastaavia matematiikkakirjastoja.

## 1. Hyväksytyt syötteet

Ohjelma on suunniteltu käsittelemään ORL-tietokantaa.

- Kuvatiedostojen tulee olla Portable GrayMap -muodossa
- Oletuskuvakoko on 92 x 112 pikseliä
- Algoritmin esikäsitteljä olettaa, että data sijaitsee kansiossa datasets/archive, jonka sisällä on 40 alikansiota, jotka edustavat eri henkilöitä.

## 2. Ohjelman suorittaminen ja toiminnallisuudet

Ohjelman käyttö on jaettu kolmeen selkeään vaiheeseen: datan esikäsittelyyn, mallin kouluttamiseen ja uusien ei-käsiteltyjen kasvojen tunnistamiseen. 

1. Mallin opettamista varten PGM-kuvat täytyy lukea, normalisoida ja jakaa harjoitus- sekä testidataan.

python3 PGM_parser.py, toteuttaa tämän.

2. Kun data on esikäsitelty, ohjelma voi oppia tunnistamaan kavojen ominaispiirteet laskemalla kovarianssimatriisin ominaisarvot ja -vektorit.

oython3 test.py

Tällä hetkellä, tämä on kehitysvaiheessa, joten tämä ei ole viimeinen muoto.