

class dna():

    def __init__(self, seq):
        #seq has to be string
        #make a str and then make a list
        #DONE
        str(seq)
        #self.seq is the main list
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

        #Makes a nested list with codons separated
        self.codon = []
        self.length = len(self.seq)
        self.codon_number = (self.length // 3)
        print(self.codon_number) #just to test

        self.dna_index = 0
        self.codon_counter = 0

        #makes blank nested lists based on #of codons
        while self.codon_counter != self.codon_number:
            self.codon_counter = self.codon_counter + 1
            self.codon.append([])

        print(self.codon)

        #attaches the sequence by threes to self.codon
        for empty_codon in self.codon:
            empty_codon.append(self.seq[self.dna_index])
            empty_codon.append(self.seq[self.dna_index + 1])
            empty_codon.append(self.seq[self.dna_index + 2])
            self.dna_index = self.dna_index + 3

        print(self.codon)

        # translates from DNA directly to protein, appends to self.protein
        for first_index, codon_list in enumerate(self.codon):

            #starts with A
            if codon_list[0] == "a":

                if codon_list[1] == "a":

                    if codon_list[2] == "a":
                        self.protein.append("k")
                    elif codon_list[2] == "t":
                        self.protein.append("n")
                    elif codon_list[2] == "g":
                        self.protein.append("k")
                    elif codon_list[2] == "c":
                        self.protein.append("n")
                    else:
                        print("3rd codon error")

                elif codon_list[1] =="t":
                    if codon_list[2]=="a":
                        self.protein.append("i")
                    elif codon_list[2]=="t":
                        self.protein.append("i")
                    elif codon_list[2] =="g":
                        self.protein.append("m-start")
                    elif codon_list[2] =="c":
                        self.protein.append("i")
                    else:
                        print("3rd codon error")


                elif codon_list[1] =="g":
                    if codon_list[2] =="a":
                        self.protein.append("r")
                    elif codon_list[2] =="t":
                        self.protein.append("s")
                    elif codon_list[2] =="g":
                        self.protein.append("r")
                    elif codon_list[2] == "c":
                        self.protein.append("s")
                    else:
                        print("3rd codon error")

                elif codon_list[1] =="c":
                    if codon_list[2] =="a":
                        self.protein.append("t")
                    elif codon_list[2] =="t":
                        self.protein.append("t")
                    elif codon_list[2] =="g":
                        self.protein.append("t")
                    elif codon_list[2] == "c":
                        self.protein.append("t")
                    else:
                        print("3rd codon error")
                else:
                    print("2nd codon error")

            #Codon starts with t
            if codon_list[0] == "t":

                if codon_list[1] == "a":
                    if codon_list[2] == "a":
                        self.protein.append("stop")
                    elif codon_list[2] == "t":
                        self.protein.append("y")
                    elif codon_list[2] == "g":
                        self.protein.append("stop")
                    elif codon_list[2] == "c":
                        self.protein.append("y")
                    else:
                        print("3rd codon error")

                elif codon_list[1] == "t":
                    if codon_list[2] == "a":
                        self.protein.append("l")
                    elif codon_list[2] == "t":
                        self.protein.append("f")
                    elif codon_list[2] == "g":
                        self.protein.append("l")
                    elif codon_list[2] == "c":
                        self.protein.append("f")
                    else:
                        print("3rd codon error")


                elif codon_list[1] == "g":
                    if codon_list[2] == "a":
                        self.protein.append("stop-trp")
                    elif codon_list[2] == "t":
                        self.protein.append("c")
                    elif codon_list[2] == "g":
                        self.protein.append("stop-trp")
                    elif codon_list[2] == "c":
                        self.protein.append("c")
                    else:
                        print("3rd codon error")

                elif codon_list[1] == "c":
                    if codon_list[2] == "a":
                        self.protein.append("s")
                    elif codon_list[2] == "t":
                        self.protein.append("s")
                    elif codon_list[2] == "g":
                        self.protein.append("s")
                    elif codon_list[2] == "c":
                        self.protein.append("s")
                    else:
                        print("3rd codon error")
                else:
                    print("2nd codon error")

            # Codon starts with g
            if codon_list[0] == "g":

                if codon_list[1] == "a":
                    if codon_list[2] == "a":
                        self.protein.append("e")
                    elif codon_list[2] == "t":
                        self.protein.append("d")
                    elif codon_list[2] == "g":
                        self.protein.append("e")
                    elif codon_list[2] == "c":
                        self.protein.append("d")
                    else:
                        print("3rd codon error")

                elif codon_list[1] == "t":
                    if codon_list[2] == "a":
                        self.protein.append("v")
                    elif codon_list[2] == "t":
                        self.protein.append("v")
                    elif codon_list[2] == "g":
                        self.protein.append("v")
                    elif codon_list[2] == "c":
                        self.protein.append("v")
                    else:
                        print("3rd codon error")


                elif codon_list[1] == "g":
                    if codon_list[2] == "a":
                        self.protein.append("g")
                    elif codon_list[2] == "t":
                        self.protein.append("g")
                    elif codon_list[2] == "g":
                        self.protein.append("g")
                    elif codon_list[2] == "c":
                        self.protein.append("g")
                    else:
                        print("3rd codon error")

                elif codon_list[1] == "c":
                    if codon_list[2] == "a":
                        self.protein.append("a")
                    elif codon_list[2] == "t":
                        self.protein.append("a")
                    elif codon_list[2] == "g":
                        self.protein.append("a")
                    elif codon_list[2] == "c":
                        self.protein.append("a")
                    else:
                        print("3rd codon error")
                else:
                    print("2nd codon error")

            # Codon starts with c
            if codon_list[0] == "c":

                if codon_list[1] == "a":
                    if codon_list[2] == "a":
                        self.protein.append("q")
                    elif codon_list[2] == "t":
                        self.protein.append("h")
                    elif codon_list[2] == "g":
                        self.protein.append("q")
                    elif codon_list[2] == "c":
                        self.protein.append("h")
                    else:
                        print("3rd codon error")

                elif codon_list[1] == "t":
                    if codon_list[2] == "a":
                        self.protein.append("l")
                    elif codon_list[2] == "t":
                        self.protein.append("l")
                    elif codon_list[2] == "g":
                        self.protein.append("l")
                    elif codon_list[2] == "c":
                        self.protein.append("l")
                    else:
                        print("3rd codon error")


                elif codon_list[1] == "g":
                    if codon_list[2] == "a":
                        self.protein.append("r")
                    elif codon_list[2] == "t":
                        self.protein.append("r")
                    elif codon_list[2] == "g":
                        self.protein.append("r")
                    elif codon_list[2] == "c":
                        self.protein.append("r")
                    else:
                        print("3rd codon error")

                elif codon_list[1] == "c":
                    if codon_list[2] == "a":
                        self.protein.append("p")
                    elif codon_list[2] == "t":
                        self.protein.append("p")
                    elif codon_list[2] == "g":
                        self.protein.append("p")
                    elif codon_list[2] == "c":
                        self.protein.append("p")
                    else:
                        print("3rd codon error")
                else:
                    print("2nd codon error")
        print(self.protein)

    def compliment(self):
        #makes a complimentary strand names it self.compliment
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


    def search(self, sequence_search):
        #searches self.seq for a successive sequence
        #get length of search
        length_search = int(len(str(self.sequence_search)))
        #makelist
        list_search = list(self.sequence_search)
        for index_search , str_search in list_search:
        #self.seq
        
        x = range(0,length_search)

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

'''
dna1 = dna("aaaaat")
dna1.translate()
dna1.show()