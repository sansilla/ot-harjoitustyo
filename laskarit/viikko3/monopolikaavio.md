
```mermaid
 classDiagram
      Pelaaja "1" --> "1" Pelinappula
      Pelinappula "*" --> "1" Ruutu
      Lauta "1" --> "*" Ruutu
      Ruutu "1" <|-- "1" Aloitusruutu
      class Ruutu{
          seuraava ruutu tiedossa
          40 kpl
      class Aloitusruutu{
      }
      class Vankila{
      }
      class Sattuma&Yhteismaa{
      }
      class Asemat&laitokset{
      }
      class Normaalit_kadut{
      }

      class Lauta{
          1 kpl
          sis. ruudut
      }
      class Pelaaja{
          2-4 kpl
          oma nappula
      }
      class Noppa{
          2 kpl
      }
      class Pelinappula{
          yhdessä ruudussa
      }
```
