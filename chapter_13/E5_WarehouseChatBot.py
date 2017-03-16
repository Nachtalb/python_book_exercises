from random import randint
from re import *


class Complaint(object):
    e1 = "Hello, I am Melanie. \n" \
         "What can I do for you?\n"

    ue1 = "I can't say anything to this.\n"
    ue2 = "Sadly I can't help you with this.\n"
    not_understood = [ue1, ue2]

    nh1 = "Can I help you somehow?\n"
    nh2 = "What can I do for you?\n"
    help = [nh1, nh2]

    ll1 = "That is a long time. \n" \
          "We proccess every order as fast as possible. \n" \
          "But sometimes there are difficulties with the delivery. \n"
    ll2 = "That long? I'll take care of it.\n"
    deliverytime = [ll1, ll2]

    dg1 = "Please send us the product back.\n"
    dg2 = "You have the right to send any defect product back to us.\n"
    defect = [dg1, dg2]

    def choose(self, l):
        return l[randint(0, len(l) - 1)]

    def answer(self, inp):
        inp = inp.lower()
        doesNotWork = compile("defect|does not work|doesn't work|destroyed|not working|broken")

        answer = ""
        if inp.count("week") + inp.count("month") > 0:
            answer += self.choose(self.deliverytime)
        elif doesNotWork.search(inp):
            answer += self.choose(self.defect)
        else:
            answer += self.choose(self.not_understood)
        return answer + self.choose(self.help)

    def chat(self):
        satisfied = compile("nothing|thanks|no", I)
        print(self.e1)
        inp = input("Client: ")
        while not satisfied.search(inp):
            print(self.answer(inp))
            inp = input("Client: ")
        print("Good day, bye.")


complaint = Complaint()
complaint.chat()
