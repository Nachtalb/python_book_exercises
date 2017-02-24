Python 3
Lernen und professionell anwenden
Das umfassende Praxisbuch
6. Auflage
von Michael Weigend
mitp-Verlag 2016


Informationen zu den Beispielskripten
-------------------------------------

In diesem Ordner befinden sich alle Skripte, die  im Buchtext erwähnt werden. Zu jedem Kapitel des Buches gibt es einen Unterordner mit dem jeweiligen Kapitelnamen. Manche Beispiele sind komplex und bestehen aus mehreren Dateien. Bei Programmen mit grafischer Benutzungsoberfläche gibt es häufig neben dem eigentlichen Python-Skript noch Bild-Dateien mit Abbildungen, die im Anwendungsfenster dargestellt werden. In diesen Fällen gibt es zu dem Beispiel einen eigenes Unterverzeichnis, in dem sich alle Dateien des Projektes befinden. Der Name des Unterverzeichnisses ist so gewählt, dass man das Beispiel leicht finden kann.


Wie findet man ein Beispielskript?
----------------------------------

Listings im Buchtext haben zu Beginn eine Kommentarzeile mit dem Namen der Skriptdatei. Wenn man z.B. im Kapitel 6 auf ein Skript stößt, dass in der ersten Zeile den Kommentar #primzahl.py trägt, so findet man das Skript unter dem Pfad /Python-Programme/kap_06/primzahl.py


Wie testet man die Beispielskripte?
-----------------------------------

Es empfiehlt es sich, den kompletten Ordner Python-Programme auf die Festplatte zu kopieren.
Die meisten Skripte kann man  direkt (z.B. durch Anklicken des Programmicons) starten.
In Einzelfällen müssen Sie Pfadnamen, die innerhalb eines Skriptes verwendet werden, an Ihr System anpassen.


Wie testet man CGI-Skripte?
---------------------------

In diesem Ordner befindet sich das Verzeichnis httpserver. Darin ist die Datei httpd.py (HTTP-Server) und das Verzeichnis cgi-bin. Von allen CGI-Skripten des Buches, die auf verschiedene Kapitel verteilt sind, befinden sich Kopien im Ordner python/httpserver/cgi-bin.
Um ein CGI-Skript zu testen können Sie folgendermaßen vorgehen:
Starten Sie zunächst den HTTP-Server indem Sie das Skript httpd.py ausführen.

Nun gibt es mehrere Möglichkeiten ein CGI-Skript zu testen:
Entweder rufen Sie direkt das CGI-Skript auf, indem Sie einen Web-Browser starten und die Adresse des Skriptes in das Adressfenster eingeben. Die Adresse ist wie folgt aufgebaut:
http://localhost:8000/cgi-bin/skript.py

In vielen Fällen handelt es sich aber um CGI-Skripte, in denen Daten aus einem html-Formular verarbeitet werden. Dann gibt es meistens im Ordner des jeweiligen Kapitels eine HTML-Seite, die Sie einfach aufrufen können. Sie müsste eigentlich funktionieren, denn in der Definition des Formulars ist die passende localhost-Adresse definiert, die beim Anklicken des Submit-Buttons aufgesucht werden soll.

Manche cgi-Skripte speichern Daten. In diesem Fall müssen Sie die Pfade für die Dateien, auf die zugegriffen wird, anpassen.


Viel Spaß bei der Arbeit mit Python!

Michael Weigend, Oktober 2016



