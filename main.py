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

    print('\nAluno: Ícaro Gabryel - MAT: 20209050584 - Número: 16\n')

    # Print alignments and score matrix
    print('Alignments found\n')
    for i in matrix.getBiggestAlignments():
        print('-' * 30, '\n')
        print(i[0], '\n')
        print(f'Score: {i[1]}\n')
        print(matrix.getMatrixInStr(i[2]), '\n')

    # Write output to file
    with open('output.txt', 'w') as file:
        file.write('Aluno: Icaro Gabryel - MAT: 20209050584 - Numero: 16\n\n')
        file.write(f'{'-' * 30}\n')
        file.write('Valores de score\n')
        file.write(f'{'-' * 30}\n')
        
        file.write(matrix.getMatrixInStrNoColor() + '\n')

        file.write(f'{'-' * 30}\n')
        file.write(f'Alinhamentos ( Match = {matchScore} | Missmatch = {missScore} | Gap = {gapScore})\n')
        file.write(f'{'-' * 30}\n')

        for i in matrix.getBiggestAlignments():
            file.write(f'Score do alinhamento: {i[1]}\n\n')
            file.write(i[0] + '\n\n')

    print('Output written to output.txt')

if __name__ == '__main__':
    main()
