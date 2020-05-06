

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

    def translate(self):
        # translates directly to protein
        for index, na in enumerate(self.seq):
        #NEED TO FIX TRIPLE CODON ERROR
            #Codon Starts with A
            if self.seq[index] == "a":

                if self.seq[index + 1] =="a":
                    if self.seq[index + 2]=="a":
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



    def search():
        #searches the sequence for a pattern returns true

    def count():
        #searches the pattern in the instance of the class
        #how many patterns are in the DNA sequence

    def reversetranscribe(self):
        #reverse transcribes from RNA to DNA
        attributes = [a for a in dir(seq) if not a.startswith("_")
