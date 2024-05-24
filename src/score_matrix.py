class Alignment:
    def __init__(self, vAlign: str, hAlign: str, path: list[tuple[int, int]]):
        self.vAlign = vAlign
        self.hAlign = hAlign
        self.path = path


class ScoreCell:
    def __init__(self) -> None:
        self.__value = None

        self.haveValueComeFromUp = False
        self.haveValueComeFromLeft = False
        self.haveValueComeFromDiag = False

    def __repr__(self) -> str:
        return str(self.__value)
    
    def getValue(self) -> int:
        return self.__value
    
    def setValue(self, value: int) -> None:
        if value < 0:
            self.__value = 0
        else:
            self.__value = value


class ScoreMatrix:
    def __init__(self, matchScore, missScore, gapScore, vSeq: str, hSeq: str):
        self.matchScore = matchScore
        self.missScore = missScore
        self.gapScore = gapScore

        self.vSeq = '-' + vSeq # Add a '-' to the beginning of the sequences
        self.hSeq = '-' + hSeq

        self.matrix = [[ScoreCell() for i in range(len(self.hSeq))] for j in range(len(self.vSeq))] # Initialize the matrix

        self.findScores() # Fill the matrix with the scores

    def findScores(self): # Find and fill the matrix with the scores
        self.matrix[0][0].setValue(0) # Set the first cell to 0

        for i in range(1, len(self.matrix[0])): # Set the first row
            previousValue = self.matrix[0][i - 1].getValue()
            
            self.matrix[0][i].setValue(self.gapScore + previousValue)
            self.matrix[0][i].haveValueComeFromLeft = True

        for i in range(1, len(self.matrix)): # Set the first column
            previousValue = self.matrix[i - 1][0].getValue()

            self.matrix[i][0].setValue(self.gapScore + previousValue)
            self.matrix[i][0].haveValueComeFromUp = True

        for i in range(1, len(self.vSeq)): # Fill the rest of the table
            for j in range(1, len(self.hSeq)):
                upValue = self.matrix[i - 1][j].getValue() + self.gapScore # Pick the value from the cell above
                leftValue = self.matrix[i][j - 1].getValue() + self.gapScore # Pick the value from the cell to the left

                if self.vSeq[i] == self.hSeq[j]: # Pick the value from the diagonal cell
                    diagValue = self.matrix[i - 1][j - 1].getValue() + self.matchScore
                else:
                    diagValue = self.matrix[i - 1][j - 1].getValue() + self.missScore

                self.matrix[i][j].setValue(max(upValue, leftValue, diagValue)) # Pick the maximum value to be the cell value

                if upValue == self.matrix[i][j].getValue(): # Check where the value came from
                    self.matrix[i][j].haveValueComeFromUp = True
                
                if leftValue == self.matrix[i][j].getValue():
                    self.matrix[i][j].haveValueComeFromLeft = True
                
                if diagValue == self.matrix[i][j].getValue():
                    self.matrix[i][j].haveValueComeFromDiag = True

    def findMaxIndexes(self) -> list[tuple[int, int]]: # Find the indexes of the maximum value(s) in the matrix
            maxIndexes = []
            maxValue = 0

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j].getValue() > maxValue:
                        maxIndexes = [(i, j)]
                        maxValue = self.matrix[i][j].getValue()
                    
                    elif self.matrix[i][j].getValue() == maxValue:
                        maxIndexes.append((i, j))

            return maxIndexes
        
    def findAlignmentsAt(self, i: int, j: int) -> list[Alignment]: # Find the alignments at a specific cell
        alignments = []

        def backTrace(i: int, j: int, vAlign = "", hAlign = "", cellsPath = []): # Backtrace to find the different alignments
            nonlocal alignments
            nonlocal self
            
            if self.matrix[i][j].getValue( )== 0: # If the value is 0, add the alignment to the list
                alignment = Alignment(vAlign, hAlign, cellsPath)

                alignments.append(alignment)

            else:
                if self.matrix[i][j].haveValueComeFromUp: # Check where the value came from up
                    tempVAlign = self.vSeq[i] + vAlign
                    tempHAlign = '-' + hAlign

                    tempCellsPath = cellsPath + [(i, j)]

                    backTrace(i - 1, j, tempVAlign, tempHAlign, tempCellsPath)

                if self.matrix[i][j].haveValueComeFromLeft: # Check where the value came from left
                    tempVAlign = '-' + vAlign
                    tempHAlign = self.hSeq[j] + hAlign

                    tempCellsPath = cellsPath + [(i, j)]

                    backTrace(i, j - 1, tempVAlign, tempHAlign, tempCellsPath)

                if self.matrix[i][j].haveValueComeFromDiag: # Check where the value came from diagonal
                    tempVAlign = self.vSeq[i] + vAlign
                    tempHAlign = self.hSeq[j] + hAlign
                    
                    tempCellsPath = cellsPath + [(i, j)]

                    backTrace(i - 1, j - 1, tempVAlign, tempHAlign, tempCellsPath)

        backTrace(i, j)

        return alignments

    def getAlignments(self) -> list[Alignment]: # Get the alignments
        alignments = []
        
        for i in self.findMaxIndexes(): # Find the alignments at the maximum value(s)
            alignments += self.findAlignmentsAt(i[0], i[1])

        return alignments
