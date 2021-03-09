## ¿Qué es un archivo CSV?

Un archivo de **Valores Separados por Comas** (o archivo CSV como se conoce comúnmente) es una forma muy básica de almacenar datos para uso en un programa Python. Es simplemente un archivo de texto donde los contenidos tienen un formato específico: separados por comas. Por ejemplo, este podría ser una muestra de datos almacenados en un archivo CSV:

```CSV
john, paul, george, ringo
```

A veces los valores están **encapsulados**. Por ejemplo, pueden encapsularse con comillas como esta:

```CSV
"john", "paul", "george", "ringo"
```

Esto es generalmente porque los datos en sí pueden contener comas, así que tenemos que evitar la confusión entre donde una coma representa una separación entre diferentes elementos de datos, y donde es simplemente parte de los datos. Por ejemplo, en este archivo CSV la encapsulación es definitivamente necesaria:

```CSV
"Tabitha, asesina de ratones", "Tiddles, bebedor de leche", "Tiffany, abandonadora de bolas de pelo"
```

La forma más básica de crear un archivo CSV es escribir datos en un archivo de texto en formato CSV, y luego guardar el archivo con la extensión `. csv`. Alternativamente, también puedes utilizar un programa como LibreOffice Calc o Microsoft Excel para crear y guardar un archivo en formato CSV.

