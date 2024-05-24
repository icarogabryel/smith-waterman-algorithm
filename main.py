from score_matrix import ScoreMatrix, ScoreCell

BLUE = '\033[36m'
GREEN = '\033[32m'
RED = '\033[31m'
END_COLOR = '\033[0m'

def addLength(string, length): # todo change to all len
    return ' ' * (length - len(string)) + string


def getMatrixInStr(self, cellsPath = []):
    matrixInStr = ''
    maxCellLen = 0

    for i in self.matrix:
        for j in i:
            if len(str(j.getCellValue())) > maxCellLen:
                maxCellLen = len(str(j.getCellValue()))

    for i in range(len(self.matrix)-1, -1, -1):
        scoreLine = ''

        for j in range(len(self.matrix[i])):
            if (i, j) in cellsPath:
                scoreLine += RED + f' {addLength(str(self.matrix[i][j].getCellValue()), maxCellLen)}' + END_COLOR
            else:
                scoreLine += GREEN + f' {addLength(str(self.matrix[i][j].getCellValue()), maxCellLen)}' + END_COLOR

        matrixInStr += BLUE + f' {self.vSeq[i]}' + END_COLOR + scoreLine + '\n'

    matrixInStr += BLUE + '  ' + ''.join([f' {addLength(i, maxCellLen)}' for i in self.hSeq]) + END_COLOR

    return matrixInStr

def matrixToString(matrix: list[list[ScoreCell]]):
    matrixInStr = ''
    maxCellLen = 0

    for i in matrix:
        for j in i:
            if len(str(j.getValue())) > maxCellLen:
                maxCellLen = len(str(j.getValue()))

    for i in range(len(matrix)):
        scoreLine = ''

        for j in range(len(matrix[i])):
            scoreLine += f' {addLength(str(matrix[i][j].getValue()), maxCellLen)}'

        matrixInStr += scoreLine + '\n'

    # matrixInStr += '  ' + ''.join([f' {addLength(i, maxCellLen)}' for i in self.hSeq])

    return matrixInStr
    

def main():
    # Read input from file
    with open('input.txt', 'r') as file:
        vSeq = file.readline().strip()
        hSeq = file.readline().strip()

        gapScore = int(file.readline())
        missScore = int(file.readline())
        matchScore = int(file.readline())
    
    # Create score matrix
    matrix = ScoreMatrix(matchScore, missScore, gapScore, vSeq, hSeq)

    print(matrixToString(matrix.matrix))


    # # Print alignments and score matrix
    # print('Alignments found\n')
    # for i in matrix.getBiggestAlignments():
    #     print('-' * 30, '\n')
    #     print(i[0], '\n')
    #     print(f'Score: {i[1]}\n')
    #     print(matrix.getMatrixInStr(i[2]), '\n')

    # # Write output to file
    # with open('output.txt', 'w') as file:
    #     file.write('Aluno: Icaro Gabryel - MAT: 20209050584 - Numero: 16\n\n')
    #     file.write(f'{'-' * 30}\n')
    #     file.write('Valores de score\n')
    #     file.write(f'{'-' * 30}\n')
        
    #     file.write(matrix.getMatrixInStrNoColor() + '\n')

    #     file.write(f'{'-' * 30}\n')
    #     file.write(f'Alinhamentos ( Match = {matchScore} | Missmatch = {missScore} | Gap = {gapScore})\n')
    #     file.write(f'{'-' * 30}\n')

    #     for i in matrix.getBiggestAlignments():
    #         file.write(f'Score do alinhamento: {i[1]}\n\n')
    #         file.write(i[0] + '\n\n')

    # print('Output written to output.txt')

if __name__ == '__main__':
    main()
