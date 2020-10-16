## Openen en lezen vanuit een bestand

- Open **Python 3 IDLE**.

- Klik op `Bestand` > `Nieuw bestand` en sla het bestand op als `shakespeare.py`.

- Voeg de volgende code toe om het bestand (`insults.csv`) in leesmodus te openen (`"r"` betekent *leesmodus*), lees de volledige inhoud en voer het resultaat uit:

    ```python
    with open("insults.csv", "r") as f:
        contents = f.read()
        print(contents)
    ```

- Wat is het verschil tussen de huidige coderegel...

  ```Python
  contents = f.read()
  ```

  ... en deze coderegel?

  ```Python
  contents = f.readline()
  ```

  Wijzig de code en kijk of je het verschil kunt vinden tussen `read()` en `readline()`.

- Tot nu toe kunnen we de beledigingen uit het bestand lezen in de volgorde waarin ze zijn geschreven, maar we kunnen er niet veel mee doen. Je hebt misschien gemerkt dat de verschillende kolommen die de delen van de belediging vormen verschillende soorten woorden waren. De eerste twee kolommen (A en B) bevatten **bijvoeglijke naamwoorden** (die woorden beschrijven) en de laatste kolom (C) bevat **zelfstandige naamwoorden**, meestal in dit geval verwijzend naar een 'ding' waar de persoon op lijkt. Als we ze zouden kunnen opsplitsen, kunnen we beledigingen maken in de vorm "Gij \[Lijst A\] \[Lijst B\] [Lijst C]" door een willekeurig woord uit elke lijst te kiezen. Een voorbeeld zou kunnen zijn: "Gij onbeschaamde achterwerksboer".

