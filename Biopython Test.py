

class dna():

    def __init__(self, seq):
        #seq has to be string
        #make a str and then make a list
        #DONE
        str(seq)
        self.seq = list(seq.lower())
        #empty protein
        self.protein = []
        self.compliment = []

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

    def translate(self):
        # translates directly to protein, appends to self.protein

        for index, na in enumerate(self.seq):
        #NEED TO FIX TRIPLE CODON ERROR
            #Codon Starts with A

            if self.seq[index] == "a":

                if self.seq[index + 1] =="a":
                    if self.seq[index + 2]=="a":

                    self.protein.append("k")


                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2]== "c":

                if self.seq[index + 1] =="t":

                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2] == "c":

                if self.seq[index + 1] =="g":
                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2]== "c":

                if self.seq[index + 1] =="c":
                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2]== "c":
                        else:
                            print("codon error")

            # Codon Starts with t
            if self.seq[index] == "t":

                if self.seq[index + 1] =="a":
                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2] == "c":
                    else:
                        print("codon error")

                if self.seq[index + 1] =="t":

                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2]== "c":
                    else:
                        print("codon error")

                if self.seq[index + 1] =="g":

                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2] == "t":
                    elif self.seq[index + 2] == "g":
                    elif self.seq[index + 2] == "c":
                    else:
                        print("codon error")

                if self.seq[index + 1] =="c":
                    if self.seq[index + 2]=="a":
                    elif self.seq[index + 2]=="t":
                    elif self.seq[index + 2]=="g":
                    elif self.seq[index + 2]== "c":
                    else:
                        print("codon error")

    def compliment(self):
        #makes a complimentary strand
        for index, na in enumerate(self.seq):
            if na == "a":
                self.compliment.append("t")
            elif na == "A":
                self.compliment.append("T")
            elif na == "t":
                self.compliment.append("a")
            elif na == "T":
                self.compliment.append("A")
            elif na == "g":
                self.compliment.append("c")
            elif na == "G":
                self.compliment.append("C")
            elif na == "C":
                self.compliment.append("g")
            elif na == "C":
                self.compliment.append("C")
            else:
                print("Error Cannot Compliment")

    def search(self):
        #searches the sequence for a pattern returns true

    def count():
        #searches the pattern in the instance of the class
        #how many patterns are in the DNA sequence

    def reverse(self):
        #reverse transcribes from RNA to DNA
        for index, na in enumerate(self.seq):
            if na == "u":
                self.seq[index] = "a"
            elif na == "U":
                self.seq[index] = "A"

    def gccontent():
        #percentage gccontent

    def searchstopcodon():
        #search a stop codon


