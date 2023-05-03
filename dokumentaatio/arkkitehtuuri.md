# Arkkitehtuurikuvaus #

## Sovelluksen rakenne ##

Sovellus koostuu neljästä pääosiosta. *Base* pitää sisällään sovelluksen tarvitsemat luokat, joita sovellus käyttää kohdetyyppeinä. *Ui* vastaa sovelluksen käyttöliittymään liittyvästä koodista, ja *services* taas sovelluslogiikasta. *Working* sisältää tietojen tallennuksen toiminnallisuuden.

## Käyttöliittymä ##

Sovelluksen käyttöliittymässä on tietyt näkymät, jotka ovat

1. Kirjautumisikkuna
2. Ikkuna uuden käyttäjän luomiselle
3. Näkymä kirjatuista säähavainnoista

## Sovelluslogiikka ##

Luokat Note ja Diary toimivat sovelluksen pohjana, ja kuvaavat sovellukseen kirjautunutta käyttäjää sekä tämän kirjaamia käyttäjän säähavaintoja.


```mermaid
 classDiagram
      Diary "*" --> "1" User
     
      class Diary{
          notes/säähavainnot
          mahd. päivämäärä
      }
      class User{
          username/käyttäjänimi
      }
```

Luokka NoteService hoitaa sovelluksen toiminnallisuuden. Se mahdollistaa käyttöliittymän toiminnan erilaisilla metodeilla.
