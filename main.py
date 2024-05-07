from ScoreMatrix import ScoreMatrix

def main():
    with open('input.txt', 'r') as file:
        vSeq = file.readline().strip()
        hSeq = file.readline().strip()

        gapScore = int(file.readline())
        missScore = int(file.readline())
        matchScore = int(file.readline())
    
    matrix = ScoreMatrix(matchScore, missScore, gapScore, vSeq, hSeq)

    print('\nAlignments found\n')
    for i in matrix.getBiggestAlignments():
        print('-' * 30, '\n')
        print(i[0], '\n')
        print(matrix.getMatrixInStr(i[1]), '\n')

    with open('output.txt', 'w') as file:
        file.write('Score Matrix\n\n')
        file.write(matrix.getMatrixInStrNoColor() + '\n')

        file.write('Alignments found\n\n')
        for i in matrix.getBiggestAlignments():
            file.write(i[0] + '\n\n')

    print('Output written to output.txt')

if __name__ == '__main__':
    main()
