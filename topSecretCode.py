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
