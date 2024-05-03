from ScoreMatrix import ScoreMatrix

def main():
    with open('input.txt', 'r') as file:
        vSeq = file.readline().strip()
        hSeq = file.readline().strip()

        gapScore = int(file.readline())
        missScore = int(file.readline())
        matchScore = int(file.readline())
    
    matrix = ScoreMatrix(matchScore, missScore, gapScore, vSeq, hSeq)
    
    print(f'Score Matrix of of the sequences {vSeq} and {hSeq}\n')
    print(matrix.getMatrixInStr(), '\n')

    print('Biggest Alignments of the matrix\n')
    for i in matrix.getBiggestAlignments():
        print(i[0], '\n')
        print(matrix.getMatrixInStr(i[1]), '\n')

if __name__ == '__main__':
    main()
