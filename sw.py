class Cell:
    cellValue = None

    upValue = None
    leftValue = None
    diagValue = None

    validTraces = [False, False, False]

    def __repr__(self) -> str:
        return f'{self.cellValue}'
    
    def setCellValue(self, value):
        self.cellValue = value

    def getCellValue(self):
        return self.cellValue

class scoreMatrix:
    def __init__(self, matchScore, missScore, gapScore, vSeq: str, hSeq: str):
        self.matchScore = matchScore
        self.missScore = missScore
        self.gapScore = gapScore

        self.vSeq = vSeq.upper() # Make sure the sequences are in uppercase
        self.hSeq = hSeq.upper()

        self.validSeq(vSeq) # Check if the sequences only contain 'A', 'C', 'G' or 'T'
        self.validSeq(hSeq)

        self.vSeq = vSeq.upper() + 'U' # Add a 'U' to the end of the sequences
        self.hSeq = hSeq.upper() + 'U'

        self.table = [[Cell() for i in range(len(self.hSeq))] for j in range(len(self.vSeq))]

        self.findScores() # Create the table

    def validSeq(self, seq):
        for i in seq:
            if i not in ['A', 'C', 'G', 'T']:
                raise ValueError(f"Invalid sequence. '{i}' is not a valid nucleotide.")

    def findScores(self):
        self.table[0][0].setCellValue(0)

        for i in self.table[0]:
            previousValue = 0 if i == self.table[0][0] else self.table[0][self.table[0].index(i) - 1].getCellValue()
            i.setCellValue(self.gapScore + previousValue)

        for i in self.table:
            previousValue = 0 if i == self.table[0] else self.table[self.table.index(i) - 1][0].getCellValue()
            i[0].setCellValue(self.gapScore + previousValue)

        self.printTable() #! remove

    def printTable(self): #! remove
        for i in self.table:
            print(i)

    def getBiggestAlignment(self): # todo
        pass

    def getBestAlignment(self): # todo
        pass

table = scoreMatrix(1, -1, -2, "ACGT", "ACGT")