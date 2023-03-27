
```mermaid
 classDiagram
      Pelaaja "1" --> "1" Pelinappula
      Pelinappula "*" --> "1" Ruutu
      Lauta "1" --> "*" Ruutu
      Ruutu <|-- Aloitusruutu
      Ruutu <|-- Vankila
      Ruutu <|-- SattumaYhteismaa
      Ruutu <|-- AsematLaitokset
      Ruutu <|-- NormaalitKadut
      class Ruutu{
          seuraava ruutu tiedossa
          40 kpl
      }
      class AsematLaitokset{
      }
      class NormaalitKadut{
      }
      class Aloitusruutu{
      }
      class Vankila{
      }
      class SattumaYhteismaa{
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
