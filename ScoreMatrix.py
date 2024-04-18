def validSeq(seq):
        for i in seq:
            if i not in ['A', 'C', 'G', 'T']:
                raise ValueError(f"Invalid sequence. '{i}' is not a valid nucleotide.")

class ScoreCell:
    cellValue = None

    valueComeFromUp = None
    valueComeFromLeft= None
    valueComeFromDiag = None

    validTraces = [False, False, False]

    def __repr__(self) -> str:
        return f'{self.cellValue}'
    
    def setCellValue(self, value):
        self.cellValue = value

    def getCellValue(self):
        return self.cellValue
    
    def setValueComeFromUp(self):
        self.valueComeFromUp = True

    def setValueComeFromLeft(self):
        self.valueComeFromLeft = True

    def setValueComeFromDiag(self):
        self.valueComeFromDiag = True

    def haveValueComeFromUp(self):
        return self.valueComeFromUp
    
    def haveValueComeFromLeft(self):
        return self.valueComeFromLeft
    
    def haveValueComeFromDiag(self):
        return self.valueComeFromDiag

class ScoreMatrix:
    def __init__(self, matchScore, missScore, gapScore, vSeq: str, hSeq: str):
        self.matchScore = matchScore
        self.missScore = missScore
        self.gapScore = gapScore

        self.biggestAlignments = []
        self.bestAlignments = 0

        self.vSeq = vSeq.upper() # Make sure the sequences are in uppercase
        self.hSeq = hSeq.upper()

        validSeq(self.vSeq) # Check if the sequences only contain 'A', 'C', 'G' or 'T'
        validSeq(self.hSeq)

        self.vSeq = 'U' + self.vSeq # Add a 'U' to the beginning of the sequences
        self.hSeq = 'U' + self.hSeq

        self.matrix = [[ScoreCell() for i in range(len(self.hSeq))] for j in range(len(self.vSeq))]

        self.findScores() # Create the table

    def findScores(self):
        self.matrix[0][0].setCellValue(0) # Set the first cell to 0

        for i in range(1, len(self.matrix[0])): # Set the first row and column to the gap score
            previousValue = self.matrix[0][i - 1].getCellValue()
            
            self.matrix[0][i].setCellValue(self.gapScore + previousValue)

        for i in range(1, len(self.matrix)):
            previousValue = self.matrix[i - 1][0].getCellValue()

            self.matrix[i][0].setCellValue(self.gapScore + previousValue)

        for i in range(1, len(self.vSeq)): # Fill the rest of the table
            for j in range(1, len(self.hSeq)):
                upValue = self.matrix[i - 1][j].getCellValue() + self.gapScore
                leftValue = self.matrix[i][j - 1].getCellValue() + self.gapScore

                if self.vSeq[i] == self.hSeq[j]:
                    diagValue = self.matrix[i - 1][j - 1].getCellValue() + self.matchScore
                else:
                    diagValue = self.matrix[i - 1][j - 1].getCellValue() + self.missScore

                self.matrix[i][j].setCellValue(max(upValue, leftValue, diagValue))

                if upValue == self.matrix[i][j].getCellValue():
                    self.matrix[i][j].setValueComeFromUp()
                
                if leftValue == self.matrix[i][j].getCellValue():
                    self.matrix[i][j].setValueComeFromLeft()
                
                if diagValue == self.matrix[i][j].getCellValue():
                    self.matrix[i][j].setValueComeFromDiag()

        self.printTable() #! remove

    def printTable(self): #! remove
        for i in self.matrix:
            print(i)

    def getBiggestAlignments(self):
        return self.findAlignmentAt(-1, -1)
    
    def getBestAlignment(self):
        pass
        
    def findAlignmentAt(self, i, j):
        listOfAlignments = []
        
        vSeq = self.vSeq
        hSeq = self.hSeq

        matrix = self.matrix
        
        def backTrace(i, j, vAlign = "", hAlign = ""):
            if (i == -len(vSeq)) or (j == -len(hSeq)):
                alignment = f'{vAlign}\n{hAlign}\n\n'

                listOfAlignments.append(alignment)
            
            else:
                if matrix[i][j].haveValueComeFromUp():
                    tempV = vSeq[i] + vAlign
                    tempH = '-' + hAlign

                    backTrace(i - 1, j, tempV, tempH)

                if matrix[i][j].haveValueComeFromLeft():
                    tempV = '-' + vAlign
                    tempH = hSeq[j] + hAlign

                    backTrace(i, j - 1, tempV, tempH)

                if matrix[i][j].haveValueComeFromDiag():
                    tempV = vSeq[i] + vAlign
                    tempH = hSeq[j] + hAlign

                    backTrace(i - 1, j - 1, tempV, tempH)

        backTrace(i, j)

        return listOfAlignments

table = ScoreMatrix(1, -1, -2, "cctcagt", "taccta")
for i in table.getBiggestAlignments():
    print(i)