# Sääpäiväkirja #

Käyttäjä voi kirjata sovellukseen päivittäiset säähavaintonsa, ja tarkastella aiemmin kirjaamiaan havaintoja. Sovellukseen voi luoda käyttäjän, joka yksilöi omat säähavainnot.

## Dokumentaatio ##

- [Vaatimusmäärittely](https://github.com/sansilla/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/sansilla/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/sansilla/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Käyttöohje](https://github.com/sansilla/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

- [Testausdokumentti](https://github.com/sansilla/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

- [Arkkitehtuurikuvaus](https://github.com/sansilla/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Uusin release](https://github.com/sansilla/ot-harjoitustyo/releases/tag/viikko6)

## Asentaminen ##

1. Aloita asentamalla riippuvuudet komennolla:

- **poetry install**

2. Siirry virtuaaliympäristöön komennolla:

- **poetry shell**

3. Alusta sovellus komennolla:

- **poetry run invoke build**

4. Sovelluksen käynnistäminen tapahtuu komennolla:

- **poetry run invoke start**

## Komentorivin komennot ##

1. *Sovelluksen suoritus*

Sovelluksen saa suoritettua komennolla:

- **poetry run invoke start**

2. *Sovelluksen testaus*

Sovelluksen testauksen saa suoritettua komennolla:

- **poetry run invoke test**

3. *Testikattavuusraportti*

Testikattavuusraportti muodostuu htmlcov-hakemistoon komennolla:

- **poetry run invoke coverage-report**

4. *Pylint-tarkistus*

Sovelluksen Pylint-tarkistuksen .pylintrc-tiedoston määritelmien mukaan saa suoritettua komennolla:

- **poetry run invoke pylint**
