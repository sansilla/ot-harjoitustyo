# Testausdokumentti #

Ohjelmaa ja sen toimivuutta on testattu yksikkötesteillä sekä eri luokkia yhdistelevillä testeillä unittestillä.

## Sovelluslogiikka ##

Luokka *NoteService*, joka vastaa sovelluslogiikasta, on testattu testiluokassa *TestNoteService*. Testissä on mukana *TemporaryNote*- sekä *TemporaryAboutUsers*-luokat, jotka tallentavat testin aikaiset tiedot, ja ne alustavat *NoteService*-olion testejä varten.

## Base-osion luokat ##

Base-osion luokkia *User* ja *Diary* testataan omissa testiluokissaan *TestBaseUser* ja *TestBaseDiary*, joissa luodaan väliaikaisesti käyttäjä, sekä muistiinpano jolla on tietty kirjaaja.

## Working-osion luokat ##

Working-osion luokkia *AboutUsers* ja *Note* testataan luokissa *TestAboutUsers* ja *TestNote*. Luokkia testataan vain testien aikana luoduilla tiedostoilla.

## Testikattavuus ##

Sovelluksen haaraumakattavuus on 87%. Käyttöliittymäosiota ei otettu testeihin mukaan.

KUVA TÄHÄN
![](./kuvat/coverage_report_5.png)
