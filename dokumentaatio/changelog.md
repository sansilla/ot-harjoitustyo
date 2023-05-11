## Viikko 3

- Käyttäjän pitäisi pystyä luomaan oma käyttäjä sekä nähdä lista kaikista käyttäjistä
- Lisätty AboutUsers-luokka, joka huolehtii käyttäjien luomisesta ja listaamisesta
- Yritetty testata, että AboutUsers-luokka toimii
- Testit eivät saa tietokantaa auki

## Viikko 4

- Lisätty data-kansio
- Lisätty .env -tiedostoon polut
- Unittest toimii (jee!), mutta antaa samalla jonkin varoituksen
- Muokattu jo olemassa olleita tiedostoja pylintin ilmoittamista virheistä

## Viikko 5

- Kirjautumisnäkymän saa viimein auki! (voi kirjautua sisään tai luoda uuden käyttäjän)
- Tasks.py -tiedostoa korjattu ohjeen mukaan, mutta coverage_raport antaa edelleen varoituksen

## Viikko 6

- Sovellus muistaa jo luodun käyttäjän, ja sillä voi kirjautua uudelleen sisään
- Jonkin näköinen lista muistiinpanoja näkyy, mutta lista koostuu Diary-olioista (sekä näkyy kaikille käyttäjille samanlaisena)

## Viikko 7 (+loppupalautusta ennen olevat päivät)

- Muistiinpanot näkyvät käyttäjälle
- Jos sovellukseen kirjautuu ensimmäistä kertaa, näkyy käyttäjä User-oliona, eikä kirjoitetut muistiinpanot tallennu myöhemmin katseltaviksi (tosin kun uudelleen kirjautuu luodulla käyttäjällä, sovellus toimii sitten normaalisti)
- Sovellus näyttää kuka sovellukseen on kirjautunut
- Testejä AboutUsers-luokalle sekä Note-luokalle

- Ensimmäisen kerran kirjautumisongelmat poissa!
- Sovellus toimii niin kuin kuuluukin
- Dokumentaatio valmis
