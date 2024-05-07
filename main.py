from ScoreMatrix import ScoreMatrix

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

    # Print alignments and score matrix
    print('\nAlignments found\n')
    for i in matrix.getBiggestAlignments():
        print('-' * 30, '\n')
        print(i[0], '\n')
        print(matrix.getMatrixInStr(i[1]), '\n')

    # Write output to file
    with open('output.txt', 'w') as file:
        file.write(f'{'-' * 30}\n')
        file.write('Valores de score\n')
        file.write(f'{'-' * 30}\n')
        
        file.write(matrix.getMatrixInStrNoColor() + '\n')

        file.write(f'{'-' * 30}\n')
        file.write(f'Alinhamentos ( Match = {matchScore} | Missmatch = {missScore} | Gap = {gapScore})\n')
        file.write(f'{'-' * 30}\n')

        for i in matrix.getBiggestAlignments():
            file.write(i[0] + '\n\n')

    print('Output written to output.txt')

if __name__ == '__main__':
    main()
