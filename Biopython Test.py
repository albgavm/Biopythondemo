

class dna():

    def __init__(self, seq):
        #seq has to be string
        #make a str and then make a list
        #DONE
        str(seq)
        self.seq = list(seq.lower())
        #empty protein list
        self.protein = []
        #empty compliment list
        self.compliment = []

    def showlist(self):
        print(self.seq)

    def show(self):
        #prints the string version
        #DONE
        print(str(self.seq))

    def transcribe(self):
        # converts the a to u
        for index, na in enumerate(self.seq):
            if na == "a":
                self.seq[index] = "u"
            elif na == "A":
                self.seq[index] = "U"

    def translate(self):
        # translates from DNA directly to protein, appends to self.protein

        for index, na in enumerate(self.seq):
        #NEED TO FIX TRIPLE CODON reading frame ERROR
        #triple codon reading frame ---> IDEA MAKE INTO LIST OF LIST with three on the entire list.
        #need to fix if no codon at the end
            #Codon Starts with A

            if self.seq[index] == "a":

                if self.seq[index + 1] =="a":
                    if self.seq[index + 2]=="a":
                        self.protein.append("k")

                    elif self.seq[index + 2]=="t":
                        self.protein.append("n")

                    elif self.seq[index + 2]=="g":
                        self.protein.append("k")

                    elif self.seq[index + 2]== "c":
                        self.protein.append("n")

                if self.seq[index + 1] =="t":

                    if self.seq[index + 2]=="a":
                        self.protein.append("i")

                    elif self.seq[index + 2]=="t":
                        self.protein.append("i")

                    elif self.seq[index + 2]=="g":
                        self.protein.append("m-str")

                    elif self.seq[index + 2] == "c":
                        self.protein.append("i")

                if self.seq[index + 1] =="g":
                    if self.seq[index + 2]=="a":
                        self.protein.append("r")
                    elif self.seq[index + 2]=="t":
                        self.protein.append("s")
                    elif self.seq[index + 2]=="g":
                        self.protein.append("r")
                    elif self.seq[index + 2]== "c":
                        self.protein.append("s")

                if self.seq[index + 1] =="c":
                    if self.seq[index + 2]=="a":
                        self.protein.append("t")
                    elif self.seq[index + 2]=="t":
                        self.protein.append("t")
                    elif self.seq[index + 2]=="g":
                        self.protein.append("t")
                    elif self.seq[index + 2]== "c":
                        self.protein.append("t")
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

    def search(self, searched_variable):
        len(searched_variable)

        #searches the sequence for a pattern returns true

    def count():
        pass
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
        pass
        #percentage gccontent

    def searchstopcodon():
        pass
        #search a stop codon

    def searchorf():
        pass
        #search an open reading frame

    def massdna():
        pass
        #calculates the mass of the DNA

    def showprotein(self):
        print(self.protein)
        #prints self.protein




