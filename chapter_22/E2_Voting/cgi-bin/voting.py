#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import os
import cgi, cgitb
import pickle
from http.cookies import SimpleCookie

cgitb.enable()


class Voting:
    template_path = "templates/"
    data_path = "data/"
    data_file = "voting_data.dat"
    voted_temaplte = "voted_template.html"
    not_voted_temaplte = "not_voted_template.html"

    def __init__(self, vote):
        self.template = ""
        self.vote = vote
        self.voting_data = {}
        self.cookie = SimpleCookie()
        self.placeholder = {}
        self.__get_cookie()
        self.__get_votings()

        if self.__check_already_voted():
            self.__get_template(self.voted_temaplte)
        else:
            if self.vote is None:
                self.__get_template(self.not_voted_temaplte)
            else:
                self.__get_template(self.voted_temaplte)
                self.__save_votings(vote)
                self.__set_cookie()

        self.placeholder = self.voting_data.copy()

    def __check_already_voted(self):
        try:
            return self.cookie["voted"].value != ""
        except KeyError:
            return False

    def __get_template(self, template):
        f = open(os.path.join(self.template_path, template))
        self.template += "Content-Type: text/html\n\n"
        self.template += self.cookie.output()
        self.template += "\n" + f.read()
        f.close()

    def __set_cookie(self):
        self.cookie["voted"] = "1"

    def __get_cookie(self):
        try:
            self.cookie.load(os.environ["HTTP_COOKIE"])
        except:
            self.cookie["voted"] = ""

    def __get_votings(self):
        try:
            f = open(os.path.join(self.data_path, self.data_file), "rb")
            self.voting_data = pickle.load(f)
            f.close()
        except:
            self.voting_data = {"hillary": "0", "trump": "0"}

    def __save_votings(self, vote):
        self.__get_votings()

        self.voting_data[vote] = str(int(self.voting_data[vote]) + 1)
        try:
            f = open(os.path.join(self.data_path, self.data_file), "wb")
            pickle.dump(f, self.voting_data)
            f.close()
        except:
            print("Error while saving vote.")

    def __str__(self):
        return self.template.format(hillary=self.placeholder["hillary"], trump=self.placeholder["trump"])


form = cgi.FieldStorage()
if form.getvalue("president") is not None:
    president = form.getvalue("president")
else:
    president = None

print(Voting(president))
