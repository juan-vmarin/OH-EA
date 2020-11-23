# Memoria

## Índice
1.  Algoritmo implementado
2. Funcionamiento específico
3. foo
4. foo
5. Pruebas realizadas
6. Conclusiones
7. Bibliografía


## Algoritmo implementado

**En nuestro caso hemos implementado el algoritmo genético (GA)**. 

Los algoritmos genéticos son métodos de optimización heurística que se emplean para hallar un valor o valores que consiguen maximizar o minimizar una función. Y obviamente su funcionamiento esta inspirado en la [teoría evolutiva de la selección natural](https://es.wikipedia.org/wiki/Selecci%C3%B3n_natural#:~:text=La%20selecci%C3%B3n%20natural%20fue%20propuesta,los%20individuos%20de%20una%20poblaci%C3%B3n.). 

En nuestro caso, hemos implementado este algoritmo con una configuración específica, el *intercambio genético uniforme*, *mutación uniforme*, *selección competitiva (tournament)* y *reemplazo en estado estacionario (Steady-state)*. 

El funcionamiento de este algoritmo es el siguiente:
1. Crear una población inicial aleatoria con **N** individuos.
2. Calcular el fitness de cada individuo de la población.
3. Crear una nueva población aplicando los siguientes pasos:
	1. Seleccionar dos individuos de la población ya creada en función del método de selección realizado.
	2. Cruzar los dos individuos seleccionados para generar un nuevo individuo en función del intercambio genético realizado.
	3. Realizar el método de mutación sobre el individuo.
	4. Añadirlo en la nueva población.
	5. Repetir todos estos pasos hasta obtener el mismo número de individuos que la antigua población. 

	```mermaid
		graph LR
		A(Selección) --> B(Cruzamiento)
		B --> C(Mutación)
		C --> D(Inserción)
		D -- Si tenemos N individuos--> E(Fin)
		D -- Si no tenemos N individos --> A
	```
4. Reemplazar la nueva población por la antigua.

## Funcionamiento específico

### Intercambio genético uniforme (Uniform crossover)
El intercambio genético tiene la función de generar nuevos individuos a partir de los anteriores, sustituyendo los anteriores por los nuevos.

### Mutación uniforme (Uniform mutation)
lorem

### Selección competitiva (Tournament selection)
Este tipo de selección, se llama competitiva porque se van comprobando el fitness de dos individuos aleatorios hasta obtener el individuo con mejor fitness.
 
### Reemplazo (Steady-state replacement)
lorem



## Pruebas realizadas
lorem

## Conclusiones
lorem

## Bibliografía
https://es.wikipedia.org/wiki/Selecci%C3%B3n_natural#:~:text=La%20selecci%C3%B3n%20natural%20fue%20propuesta,los%20individuos%20de%20una%20poblaci%C3%B3n.

https://www.cienciadedatos.net/documentos/py01_optimizacion_ga#Crear-poblaci%C3%B3n










# Welcome to StackEdit!

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. Once you have finished with me, you can create new files by opening the **file explorer** on the left corner of the navigation bar.


# Files

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

## Create files and folders

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

## Switch to another file

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Rename a file

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Delete a file

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

## Export a file

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.


# Publication

Publishing in StackEdit makes it simple for you to publish online your files. Once you're happy with a file, you can publish it to different hosting platforms like **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **WordPress** and **Zendesk**. With [Handlebars templates](http://handlebarsjs.com/), you have full control over what you export.

> Before starting to publish, you must link an account in the **Publish** sub-menu.

## Publish a File

You can publish your file by opening the **Publish** sub-menu and by clicking **Publish to**. For some locations, you can choose between the following formats:

- Markdown: publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).

## Update a publication

After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the **Publish now** button in the navigation bar.

> **Note:** The **Publish now** button is disabled if your file has not been published yet.

## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```
