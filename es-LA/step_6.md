## Abrir y leer desde un archivo

- Abre **Python 3 IDLE**.

- Haz clic en `Archivo` > `Nuevo archivo` y guarda el archivo como `shakespeare.py`.

- Agrega el siguiente código para abrir el archivo (`insults.csv`) en modo de lectura (`"r"` significa *modo de lectura*), lee los contenidos completos y genera el resultado:

    ```python
    with open("insults.csv", "r") as f:
        contents = f.read()
        print(contents)
    ```

- ¿Cuál es la diferencia entre la línea actual de código...

  ```Python
  contenido = archivo.read()
  ```

  ...y esta línea de código?

  ```Python
  contenido = archivo.readline()
  ```

  Cambia el código y comprueba si puedes ver la diferencia entre `read()` y `readline()`.

- Hasta ahora, podemos leer los insultos del archivo en el orden en que fueron escritos, pero no podemos hacer mucho con ellos. Puedes haber notado que las diferentes columnas que forman las partes del insulto tienen diferentes tipos de palabras. Las dos primeras columnas (A y B) contienen **adjetivos** (describiendo palabras) y la última columna (C) contiene **sustantivos**, mayormente en este caso refiriéndose a una "cosa" a la que la persona se parece. Si pudiéramos dividirlos, podríamos crear insultos con este formato "Tú \[Lista A\] \[Lista B\] [Lista C]" eligiendo una palabra aleatoria de cada lista. Un ejemplo podría ser "Tú, impertinente mimado sinvergüenza".

