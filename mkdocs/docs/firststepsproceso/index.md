# Prost! Erste Schritte mit Proceso

[![](images/proseco-b.jpg)](https://www.flickr.com/photos/schockwellenreiter/54621770541/)

### PyScript und Processing (mit Proceso)

Das freie (Apache-2.0-Lizenz) Framework [PyScript](http://cognitiones.kantel-chaos-team.de/programmierung/python/pyscript.html), mit dem Benutzer umfangreiche Python-Anwendungen im Browser erstellen können, und das von einem Team bei [Anaconda](http://cognitiones.kantel-chaos-team.de/programmierung/python/anaconda.html) entwickelt wird, hatte ich lange links liegen lassen, weil mir eine »Killer-Applikation« fehlte. Bis ich auf der Seite »[Resources for teaching programming for artists, designers and architects](https://abav.lugaralgum.com/Resources-for-teaching-programming/)« von *Alexandre Villares* das Modul [Proceso](https://proceso.cc/) entdeckte.

Proceso ist ein Python-Paket für kreatives Programmieren im Web. Der Fokus liegt darauf, Programmieren für Künstler, Designer, Pädagogen, Anfänger und alle anderen zugänglich zu machen. Das Paket bietet eine Python-Schnittstelle zur [p5.js](http://cognitiones.kantel-chaos-team.de/programmierung/creativecoding/processing/p5js.html)-Bibliothek und ist stark von [Py5](http://cognitiones.kantel-chaos-team.de/programmierung/creativecoding/processing/py5.html) inspiriert. Proceso ist für [Pyodide](http://cognitiones.kantel-chaos-team.de/programmierung/python/pyodide.html)-basierte Umgebungen mit Schwerpunkt auf PyScript konzipiert.

Auch Proceso kann man sowohl in der Cloud (zum Beispiel bei [Anaconda](https://pyscript.com/) – Vorsicht! Wieder ein amerikanischer Server!), aber auch in einer selbstgehosteten Wolke oder in einer [lokalen Umgebung](https://proceso.cc/welcome/getting_started#local-anaconda-vs-code) zum Beispiel mit [Visual Studio Code](http://cognitiones.kantel-chaos-team.de/produktivitaet/visualstudiocode.html) betreiben.

Proceso scheint so etwas zu sein, von dem ich die letzten Monate geträumt habe: **[Py5 im Browser](https://kantel.github.io/posts/2024072701_py5_pyscript/)**.

### Ein erstes Beispielskript

Nachdem mich die [Dokumentation](https://proceso.cc/welcome/getting_started#local-anaconda-vs-code) erst einmal in die Irre führte (`pip install proceso` funktionierte bei mir einfach nicht), fand ich durch wildes Herumexperimentieren heraus, daß ich Proceso auch lokal auf meinem Rechner ohne eine vorhergegangene Installationsorgie betreiben kann:

Das Einzige, was vorhanden sein muß, ist ein installiertes, einigermaßen aktuelles Python und ein Texteditor Eures Vertrauens (bei mir ist es [Visual Studio Code](http://cognitiones.kantel-chaos-team.de/produktivitaet/visualstudiocode.html) mit den üblichen *Python Extensions*). Danach habe ich mir von [diesem Projekt-Template](https://pyscript.com/@4b2d42a1-0e0c-430f-8b20-4b2c7ff0dc3e/58197361-1c5f-4d47-93a9-91570255fe85/latest?files=index.html) einfach die Dateien `index.html`, `pyscript.json`, `style.css` und `sketch.py` heruntergeladen und zusammen in **einem** Projektverzeichnis abgelegt. Falls Ihr nichts seltsames vorhabt, könnt Ihr erst einmal die ersten drei Dateien unverändert lassen, lediglich in der Datei `sketch.py` müßt Ihr Euren eigenen Code hineinschreiben. In meinem Fall war das:

~~~python
from proceso import Sketch
from random import randint

p5 = Sketch()

def setup():
    p5.create_canvas(640, 400)
    p5.background(49, 197, 244)
    p5.fill(146, 82, 161)
    p5.rect(40, 40, p5.width - 80, p5.height - 80)
    p5.fill(randint(30, 220), randint(30, 220), randint(30, 220), 100)


def draw():
    p5.circle(p5.mouse_x, p5.mouse_y, 20)

def mouse_clicked():
    p5.fill(randint(30, 220), randint(30, 220), randint(30, 220), 100)

p5.run_sketch(setup=setup, draw=draw, mouse_clicked=mouse_clicked)
~~~

Wenn ich dann die `index.html` **hinter** einem (lokalen) Webserver (ich nutze dafür immer noch den betagten, aber bewährten [MAMP](http://cognitiones.kantel-chaos-team.de/webworking/mamp.html)) aufrufe, bekommt Ihr untenstehendes Ergebnis angezeigt:

<iframe src="proseco/index.html" width="644" height="404"></iframe>

Das ist eine abgewandelt Version des bekannten [Py5-Beispielskripts](https://py5coding.org/index.html) (ein Mausklick ändert die Farben der Bällchen), das ich noch ein wenig aufgepeppt habe.

Wenn Ihr Euch die `index.html` anschaut,

~~~html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Python mit Balls</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    
    <!-- Load PyScript -->
     <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.3/core.css" />
     <script type="module" src="https://pyscript.net/releases/2024.1.3/core.js"></script> 
    <!-- Load p5.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
    <!-- Load custom styles -->
    <link rel="stylesheet" href="style.css" />
</head>
<body>
    <main></main>   
    <!-- Load sketch -->
    <script type="py" src="sketch.py" config="pyscript.json"></script>
</body>
</html>
~~~

dann seht Ihr, daß die PyScript-Dateien (JavaScript und CSS) sowie die minimierte P5.js-Datei von extern geladen werden. Ich habe es versucht: Zwar kann ich die `p5.js`-Datei auch lokal auf meinem Rechner installieren und zur Mitarbeit bewegen, die PyScript `core.js`-Datei dagegen war ums Verrecken nicht zur lokalen Mitarbeit bereit, sie bestand darauf, auf dem Server von `pyscript.net` aufgerufen zu werden.

Das steht natürlich ein wenig meinen Bemühungen um digitale Souveränität im Wege, ist aber leider bei vielen Diensten, die über CDNs geladen werden, gängige Praxis. Daher habe ich das erst einmal hingenommen. Doch wenn jemand von Euch da draußen eine Idee hat, wie man die `core.js` und die `core.css` auch lokal installiert bekommt, bitte ich um Mitteilung in meinen Kommentaren.

Die (lokal) installierte `style.css` birgt keine Geheimnisse,

~~~css
html,
body {
    margin: 0;
    padding: 0;
}

canvas {
    display: block;
}
~~~

aber CSS-Gurus wissen sicher, wie sie sich darin austoben können.

Noch ein Geheimnis ist für mich die Konfigurationsdatei `pyscript.json`:

~~~json
{"packages": ["proceso"], "name": "proceso starter Copy"}
~~~

Das ist der einzige Ort, an dem überhaupt `proceso` vorkommt und darüber weiß vermutlich PyScript, daß und wo es sich das Modul Proceso hereinziehen muß. Momentan nehme ich daß noch einfach so hin (ich freue mich, daß ich alles zum Laufen. bekommen habe), aber irgendwann will ich die Zusammenhänge kapieren.

Proceso vermählt nicht nur [P5.js](http://cognitiones.kantel-chaos-team.de/programmierung/creativecoding/processing/p5js.html) mit dem Python-Ökosystem, sondern erlaubt auch die Erstellung von interaktiven Web-Anwendungen. Es ist daher für alle interessant, die – wie ich – Pickel von den geschweiften Klammern von JavaScript bekommen.