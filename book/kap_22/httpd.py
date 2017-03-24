# ----------------------------------------------------
# Dateiname:  httpd.py 
# HTTP-Server, der CGI-Skripte verarbeiten kann.
# Die CGI-Skripte müssen in einem Unterverzeichnis des
# Verzeichnisses sein, in dem die Programmdatei des Servers ist.
# Dieses Unterverzeichnis hat den Namen cgi-bin.
#
# Objektorientierte Programmierung mit Python
# Kap. 22
# Michael Weigend 17. 10. 09
# ----------------------------------------------------


from http.server import HTTPServer, CGIHTTPRequestHandler

serveradresse = ("", 8000)  # 1
server = HTTPServer(serveradresse,
                    CGIHTTPRequestHandler)  # 2
server.serve_forever()  # 3
