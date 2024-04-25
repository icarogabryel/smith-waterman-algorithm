def validSeq(seq):
        for i in seq:
            if i not in ['A', 'C', 'G', 'T']:
                raise ValueError(f"Invalid sequence. '{i}' is not a valid nucleotide.")

def makeStrLenThree(string): # Todo: remove
    if len(string) > 3:
        raise ValueError("The string is longer than 3 characters.")
    
    result = ' ' * (3 - len(string)) + string

    return result

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

    def printMatrix(self):

        print('\033[36m' + '   ' + ''.join([f'  {i}  ' for i in self.hSeq]) + '\033[0m')
        
        for i in range(len(self.matrix)):
            print('\033[36m' + f' {self.vSeq[i]} ' + '\033[0m' + '\033[32m' + ''.join([f' {makeStrLenThree(str(j))} ' for j in self.matrix[i]]) + '\033[0m')

    def getBiggestAlignments(self):
        return self.findAlignmentAt(len(self.vSeq) - 1, len(self.hSeq) - 1)
    
    def getBestScoreAlignments(self):
        borderCells = []

        # append the cells from last row and column
        for i in range(len(self.vSeq)):
            for j in range(len(self.hSeq)):
                if (i == len(self.vSeq) -1)  or (j == len(self.hSeq) -1):
                    borderCells.append((self.matrix[i][j].getCellValue(), i, j))

        # find the best score
        bestScoresCells = [i for i in borderCells if i[0] == max(borderCells)[0]]

        bestScoreAlignments = []

        for i in bestScoresCells:
            bestScoreAlignments += self.findAlignmentAt(i[1], i[2])
        
        return bestScoreAlignments
        
    def findAlignmentAt(self, i, j):
        listOfAlignments = []
        
        vSeq = self.vSeq
        hSeq = self.hSeq

        matrix = self.matrix
        
        def backTrace(i, j, vAlign = "", hAlign = ""):
            if (i == 0) or (j == 0):
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
