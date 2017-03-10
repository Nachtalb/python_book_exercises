import time

with open('marathondata.txt', 'a') as marathonFile:
    startNr = input("Startnumber: ")
    while startNr is not '':
        t = time.asctime()
        marathonFile.write(startNr + ': ' + t + "\n")
        marathonFile.flush()
        startNr = input("Startnumber: ")
    marathonFile.close()
