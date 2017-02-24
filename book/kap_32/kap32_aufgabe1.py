#----------------------------------------------------
# Dateiname:  kap32_aufgabe1.py
# In einem langen Text werden parallel von mehreren
# Prozessen die Vorkommen eines Suchbegriffs gezählt.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 32
# Michael Weigend 24.10.2016
#----------------------------------------------------
from multiprocessing import Process, Queue

def search(q, text, word):
    n = text.lower().count(word.lower()) 
    q.put(n)
            
if __name__ == '__main__':
    word = input("Suchbegriff: ")  
    f = open("marktwain.txt")
    text = f.read()
    f.close()
    q = Queue()
    n = len(text)
    chunks = [text[:n//4], text[n//4:n//2],
              text[n//2:3*n//4], text[3*n//4:]]

    processes = [Process(target=search, args=(q, chunk, word))
                 for chunk in chunks]
    for p in processes: p.start()
    n = 0
    for i in range(4):
            n += q.get()
    for p in processes: p.join()
    print("Das Wort '%s' kommt %i Mal in Mark Twains Werk vor."
          % (word, n))

    
