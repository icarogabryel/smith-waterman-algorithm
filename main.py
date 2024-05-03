from ScoreMatrix import ScoreMatrix

def main():
    with open('input.txt', 'r') as file:
        vSeq = file.readline().strip()
        hSeq = file.readline().strip()

        gapScore = int(file.readline())
        missScore = int(file.readline())
        matchScore = int(file.readline())
    
    matrix = ScoreMatrix(matchScore, missScore, gapScore, vSeq, hSeq)
    
    matrix.printMatrix()

    for i in matrix.getBiggestAlignments():
        print(i)

if __name__ == '__main__':
    main()
