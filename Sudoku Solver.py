sudoku = [
    [0,0,5, 3,0,0, 0,0,0],
    [8,0,0, 0,0,0, 0,2,0],
    [0,7,0, 0,1,0, 5,0,0],
    
    [4,0,0, 0,0,5, 3,0,0],
    [0,1,0, 0,7,0, 0,0,6],
    [0,0,3, 2,0,0, 0,8,0],
    
    [0,6,0, 5,0,0, 0,0,9],
    [0,0,4, 0,0,0, 0,3,0],
    [0,0,0, 0,0,9, 7,0,0]]

steps = 0
tries = 0
def afficherSudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0: #chaque 3 colones sauf la première
            print('- - - - - - - - - - - - - - - - -')
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0: #chaque 3 lignes sauf la première
                print(' | ', end='') #end empeche le retour a la ligne

            if j == len(sudoku[0]) - 1: #si derniere position, retour a la ligne
                print(' ' + str(sudoku[i][j]))
            else: #sinon end empeche le retour a la ligne
                print(' ' + str(sudoku[i][j]) + ' ', end='')


def caseVide(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0: #si case vide
                return (i, j) #retourne le couple (ligne, colone)
    return None #retourne None si aucune case vide


def reponseValide(sudoku, reponse, position):
    #vérifie ligne
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == reponse and position[1]!= i: #vérifie que ce n'est pas notre propre case
            return False #si une case est la meme que notre reponse, retourne False

    #vérifie colone
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == reponse and position[0] != i:
            return False

    #vérifie carre
    carre_x = position[1] // 3 #partie entière de la division, regroupe 3 colones
    carre_y = position[0] // 3 #regroupe 3 lignes dans un carre 0, 1 ou 2

    for i in range(carre_y * 3, carre_y * 3 + 3): #pour commencer a la colone 0, 3 ou 6 jusqu'à 3, 6 ou 9
        for j in range(carre_x * 3, carre_x * 3 + 3):
            if sudoku[i][j] == reponse and (i, j) != position:
                return False

    #si n'a pas revoyé False, alors la reponse est valide
    return True


def resoudre(sudoku):
    global steps
    global tries
    steps = steps +1
    
    case = caseVide(sudoku)
    if not case: #si aucune case vide, si caseVide retourne None
        return True #alors le sudoku est fini
    else:
        ligne, colone = case
        
    for i in range(1, 10): #teste les réponses de 1 à 9 inclu
        tries = tries + 1
        if reponseValide(sudoku, i, (ligne, colone)):
            sudoku[ligne][colone] = i

            #on rappele cette meme fonction pour tester les case suivantes
            #si une case est fausse, alors la fonction retourne False
            #la case est alors remplacer par 0
            #la boucle continue alors avec une autre valeur
            if resoudre(sudoku):
                return True
            sudoku[ligne][colone] = 0
            
    #si il n'y a plus de valeur à tester, la fonction retourne False
    #le meme processus se fait pour la fonction precedement appele
    return False

afficherSudoku(sudoku)
resoudre(sudoku)
print('\n')
afficherSudoku(sudoku)
print('\nsolved in ', tries, 'tries')
print('solved in ', steps, 'steps')
