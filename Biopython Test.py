

class dna():


    def __init__(self, seq):
        #seq has to be string
        #make a str and then make a list
        #DONE
        str(seq)
        self.seq = list(seq.lower())

    def showlist(self):
        print(self.seq)

    def show(self):
        #prints the string version
        #DONE
        print(str(self.seq))

    def transcribe(self):
        # converts the a to u
        #done
        for index, na in enumerate(self.seq):
            if na == "a":
                self.seq[index] = "u"
            elif na == "A":
                self.seq[index] = "U"

    def translate():
        # translates directly to protein
        for index, na in enumerate(self.seq):
            if na == ""


    def search():
        #searches the sequence for a pattern

    def count():
        #searches the pattern in the instance of the class
        #how many patterns are in the DNA sequence

    def reversetranscribe(self):
        #reverse transcribes from RNA to DNA
        attributes = [a for a in dir(seq) if not a.startswith("_")
