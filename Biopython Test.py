

class dna():

    def __init__(self, seq):
        self.seq = seq
        return [char for char in self.seq]

    def makeseq(self):
        # makes a sequence list from a string
        self.list = yield(for char in self.seq)

    def show(self):
        #makes a string from self.list

    def transcribe(self):
        # converts the a to u
        for na in self.list:
            if na == "a":
                na = "u"
            elif na == "A":
                na = "U"
            else:
                return
    def translate():
        # translates directly to protein
        for na in self.list:
            if na == ""


    def search():
        #searches the sequence for a pattern

    def count():
        #searches the pattern in the instance of the class
        #how many patterns are in the DNA sequence

    def reversetranscribe(self):
        #reverse transcribes from RNA to DNA
        attributes = [a for a in dir(seq) if not a.startswith("_")
