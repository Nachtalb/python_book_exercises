import time as t
import os as o


class LastEdited(object):
    def __init__(self, path, time):
        self.time = time
        self.path = path

    def __str__(self):

        message = "Path: {path}\n" \
                  "Timeframe: {time}h\n\n" \
                  "Time and path of the last edited files: \n\n"

        message = message.format(path=o.path.abspath(self.path), time=self.time)

        for file in self.getLastEdited():
            message += "{edited}: {file}\n".format(edited=file[1], file=file[0])
        return message

    def getLastEdited(self):
        timefstart = t.time() - self.time * 3600
        filelist = []
        for dic in o.walk(self.path):
            for file in dic[2]:
                filepath = o.path.join(dic[0], file)
                lastedited = o.path.getmtime(filepath)
                if timefstart - lastedited <= 0:
                    filelist += [(filepath, t.ctime(lastedited))]
        return filelist


print("Last edited files")
print("-----------------")

path = input("Path: ")
time = "x"

while not time.isnumeric():
    time = input("Timeframe (hours): ")
time = float(time)

print("\n\nStarting search")
print("---------------")
print(LastEdited(path, time))
