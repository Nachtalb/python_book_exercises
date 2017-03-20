from http.client import HTTPConnection
from re import compile, findall
from tkinter import *


class Gui:
    def __init__(self):
        font = ("Arial", 14)
        self.w = Tk()
        self.w.title('Ozon-Check')

        self.place = StringVar()
        self.result = StringVar()

        self.frame = Frame(self.w)
        Label(self.frame, font=font, text='Ort: ').pack(side=LEFT)
        Entry(self.frame, font=font, textvariable=self.place).pack(side=LEFT)
        Button(self.frame, font=font, text=' Ozon ', command=self.ozoncheck).pack(side=LEFT, padx=5)
        self.frame.pack(padx=5, pady=5)

        Label(self.w, font=font, height=4, textvariable=self.result).pack()

        self.w.mainloop()

    def ozoncheck(self):
        information = str(Ozoncheck(self.place.get()))
        if information != "":
            self.result.set(information)
        else:
            self.result.set("Place not found")




class Ozoncheck:
    url = "www.lanuv.nrw.de"
    uri = "/fileadmin/lanuv/luft/immissionen/aktluftqual/eu_o3_akt"

    def __init__(self, place):
        self.place = place
        self.websitedata = ""

        self.__get_websitedata()

    def __get_websitedata(self):
        con = HTTPConnection(self.url)
        con.request("GET", self.uri)
        answer = con.getresponse()
        self.websitedata = answer.read().decode("iso-8859-1")

    def __find_information(self):
        start = self.websitedata.find(self.place)
        end = self.websitedata.find("</tr>", start)
        re = compile("<td .+?</td>")
        columns = re.findall(self.websitedata[start:end])
        return int(compile("\d+").findall(columns[2])[0])

    def __str__(self):
        if self.websitedata.find(self.place) == -1:
            return ""
        else:
            return str(self.__find_information()) + " micrograms"

if __name__ == "__main__":
    ozon = Gui()