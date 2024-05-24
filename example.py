from score_matrix import ScoreMatrix, ScoreCell, Alignment


BLUE = '\033[36m' # Colors for print the matrix
GREEN = '\033[32m'
RED = '\033[31m'
END_COLOR = '\033[0m'


def printAlign(vSeq: str, hSeq: str, matrix: list[list[ScoreCell]], cellsPath: Alignment = []) -> None:
    def addLength(string, length):
        return ' ' * (length - len(string)) + string

    vSeq = '-' + vSeq
    hSeq = '-' + hSeq
    matrixInStr = ''
    maxCellLen = 0

    for i in matrix:
        for j in i:
            if (length := len(str(j.getValue()))) > maxCellLen:
                maxCellLen = length

    matrixInStr += BLUE + '  ' + ''.join([f' {addLength(i, maxCellLen)}' for i in hSeq]) + END_COLOR + '\n'

    for i in range(len(matrix)):
        scoreLine = ''

        for j in range(len(matrix[i])):
            if (i, j) in cellsPath:
                scoreLine += RED + f' {addLength(str(matrix[i][j].getValue()), maxCellLen)}' + END_COLOR
            else:
                scoreLine += GREEN + f' {addLength(str(matrix[i][j].getValue()), maxCellLen)}' + END_COLOR

        matrixInStr += BLUE + f' {vSeq[i]}' + END_COLOR + scoreLine + '\n'

    print(matrixInStr)


def main():
    matchScore = 1
    missScore = -2
    gapScore = -2
    vSeq = 'AGGTTG'
    hSeq = 'TCAGTTGCC'
    
    # Create score matrix
    matrix = ScoreMatrix(matchScore, missScore, gapScore, vSeq, hSeq)

    alignments = matrix.getAlignments()

    for i in alignments:
        printAlign(vSeq, hSeq, matrix.matrix, i.path)


if __name__ == '__main__': main()
