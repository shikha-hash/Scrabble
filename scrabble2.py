from sys import stdin
import math
import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
CELL_WIDTH = 3 # cell width of the scrabble board
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7 and TILES_USED < len(Tiles):
        myTiles.append(Tiles[TILES_USED])
        TILES_USED += 1


# prints tiles and their scores
def printTiles(myTiles):
    tiles = ""
    scores = ""
    for letter in myTiles:
        tiles += letter + "  "
        thisScore = getScore(letter)
        if thisScore > 9:
            scores += str(thisScore) + " "
        else:
            scores += str(thisScore) + "  "

    print("\nTiles : " + tiles)
    print("Scores: " + scores)


# gets the score of a letter
def getScore(letter):
    for item in Scores:
        if item[0] == letter:
            return item[1]

# initialize n x n Board with empty strings
def initializeBoard(n):
    Board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("")
        Board.append(row)

    return Board

# put character t before and after the string s such that the total length
# of the string s is CELL_WIDTH.
def getString(s,t):
    global CELL_WIDTH
    s = str(s)
    rem = CELL_WIDTH - len(s)
    rem = rem//2
    s = t*rem + s
    rem = CELL_WIDTH - len(s)
    s = s + t*rem
    return s

# print the Board on screen
def printBoard(Board):
    global CELL_WIDTH
    print("\nBoard:")
    spaces = CELL_WIDTH*" "
    board_str =  "  |" + "|".join(getString(item," ") for item in range(len(Board)))  +"|"
    line1 = "--|" + "|".join(getString("","-") for item in range(len(Board)))  +"|"

 
    print(board_str)
    print(line1)
    
    for i in range(len(Board)):
        row = str(i) + " "*(2-len(str(i))) +"|"
        for j in range(len(Board)):
            row += getString(Board[i][j]," ") + "|"
        print(row)
        print(line1)
        
    print()

scoresFile = open('scores.txt')
tilesFile = open('tiles.txt')

# read scores from scores.txt and insert in the list Scores
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line= line.strip()
    Tiles.append(line)
tilesFile.close()

# decide whether to return random tiles
rand = input("Do you want to use random tiles (enter Y or N): ")
if rand == "Y":
    SHUFFLE = True
else:
    if rand != "N":
        print("You did not enter Y or N. Therefore, I am taking it as a Yes :P.")
        SHUFFLE = True
if SHUFFLE:
    random.shuffle(Tiles)


validBoardSize = False
while not validBoardSize:
    BOARD_SIZE = input("Enter board size (a number between 5 to 15): ")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE >= 5 and BOARD_SIZE <= 15:
            validBoardSize = True
        else:
            print("Your number is not within the range.\n")
    else:
        print("Are you a little tipsy? I asked you to enter a number.\n")


Board = initializeBoard(BOARD_SIZE)
printBoard(Board)

myTiles = []
getTiles(myTiles)
printTiles(myTiles)

########################################################################
# Write your code below this
########################################################################

word=""
wordsFile = open('dictionary.txt')
Valid=[]
ATiles=[]
WL=[]
lcount=0
foundL=0
CLCount=0
spRow=0
spCol=0
direc=0
VAL_HWord="NO Valid Words"
VAL_hScore=0
BTU=0
FirstWord=1
EBoard=1
correct = 0
tscore=0
placed=0
UWL=[]
TileUsed=0
usedWord=0
DIRECTIONS=[]
DIRECTIONS.append("H")
DIRECTIONS.append("V")
TOB=[]
LastCorrect=1
EmptyR=[]
EmptyC=[]
FilledR=[]
FilledC=[]
score=0





for line in wordsFile:
    line= line.strip()
    Valid.append(line)
wordsFile.close()







for i in range(0,BOARD_SIZE):
    EmptyR.append(i)
for j in range(0,BOARD_SIZE):
    EmptyC.append(j)

while(word!="***"):
    BOARD_Tiles=[]
    usedWord=0
    TileUsed=0
    ATiles=myTiles.copy()
    VAL_HWord="NO Valid Words"
    VAL_hScore=0
    WL=[]
    placable=1
    overlap=0
    TotalTiles=[]
    AIUWL=[]
    AI_BOARD_Tiles=[]
    
    #print(Board[i])
    for i in range(0,BOARD_SIZE):
        if "" not in Board[i] and i not in FilledR:
            FilledR.append(i)
            
    for j in range(0,BOARD_SIZE):
        if "" not in Board[j] and j not in FilledC:
            FilledR.append(j)       



    
    for u in UWL:
        AIUWL.append(u)

    for i in range(0,BOARD_SIZE):
        for j in range(0,BOARD_SIZE):
            if Board[i][j]!="":
                ################print("Board Not Empty")
                EBoard=0
                break
            j=j+1
        i=i+1
    
    for t in myTiles:
        TotalTiles.append(t)
    for t in TOB:
        TotalTiles.append(t)
    #print(TotalTiles)
    
    #print(AIUWL)
    
    #TempTotalTiles=TotalTiles.copy()
    Valid_Words=[]




    #for letter in ask:
        #    lcount=lcount+1
        #    for k in ATiles:
        #        if k==letter:
        #            CLCount=CLCount+1
        #            ATiles.remove(k)
        #            break;
        #        
        #            
        #    if len(ask)==lcount:
        #        if CLCount==lcount:
        #           WL.append(ask)
        #        ATiles=myTiles.copy()
        #        lcount=0
        #        CLCount=0
        #        break;












    
    for VWord in Valid:
        TempTotalTiles=TotalTiles.copy()
        lcount=0
        for letter in VWord:
            
            for t in TempTotalTiles:
                
                if letter==t:
                    
                    TempTotalTiles.remove(t)
                    lcount=lcount+1
                    #print(lcount)
                    break
            #print(VWord+str(lcount))
            #print(lcount)
        if lcount==len(VWord):
            #print(VWord)
            Valid_Words.append(VWord)
        
                    
        
    #print(Valid_Words)

    if LastCorrect==1:
        for word in Valid_Words:
            TileUsed=0
            correct=1
            for used in AIUWL:
                    if word==used:
                        correct=0
                        #print("But it's already been used")
                        break
                
            

            if correct==1:
                #print("checking")
                words=[]
                #LastCorrect=0
                #spRow=input("Enter the row of the first letter: "+word[0])
                #spCol=input("Enter the column of the first letter: "+word[0])
                for spRow in range(0,BOARD_SIZE):
                    
                    #print("checking "+word)
                    for spCol in range(0,BOARD_SIZE):
                            for direc in DIRECTIONS:
                                
                                TileUsed=0


                                placable=1


                                BTU=0
                                
                                
                                #direc=input("Enter the corresponding input for desired direction\n1.Horizontal\n2.Vertical")
                                usableTiles=myTiles.copy()              #######################################################################ADD COMMENTS!!!!!!!!!!!!!!!!!!
                                if direc=="H":
                                    if (not spCol+len(word)<=BOARD_SIZE) or ((spRow in EmptyR) and (EBoard==0)) or (spRow in FilledR):
                                        #print("Error, Can't place it")
                                        placable=0
                                        break
                                if direc=="V":
                                    if (not spRow+len(word)<=BOARD_SIZE) or ((spCol in EmptyC) and (EBoard==0)) or (spCol in FilledC):
                                        #print("Error, Can't place it")
                                        placable=0
                                        break
                                if spRow in EmptyR:
                                    EmptyR.remove(spRow)
                                    #FilledR.append(spRow)
                                if spCol in EmptyC:
                                    EmptyC.remove(spCol)
                                    #FilledC.append(spCol)
                                if placable==1:
                                    i=spRow
                                    j=spCol
                                    AI_BOARD_Tiles=[]
                                    for w in word:
                                        overlap=0
                                        if Board[i][j]=="":
                                            ####print("free")
                                            TileUsed=1
                                        else:
                                            if Board[i][j]==w:
                                                ######print(w+" BoardTileUsed")
                                                usableTiles.append(w)
                                                AI_BOARD_Tiles.append(w)
                                                BTU=1
                                            else:
                                                #print("OVERLAPPED")
                                                overlap=1
                                                correct=0
                                                break
                                        if direc=="H":
                                            j=j+1
                                        if direc=="V":
                                            i=i+1

                                    #print(usableTiles)
                                    TILE = 0
                                    #usableTiles=TotalTiles.copy()
                                    for w in word:
                                        
                                        if w in usableTiles:
                                            TILE= TILE+1
                                            usableTiles.remove(w)
                                        else :
                                            TILE = 0
                                            
                                            #break
                                    if TILE != len(word) :
                                        #print("this word cannot be made using the tiles")
                                        correct=0
                                        #print(word)
                                        #print(overlap)
                                        #print(TileUsed)
                                        #print(EBoard)
                                        #print(BTU)
                                        placable=0
                                        break
                                    else:
                                        #########
                                        #print("Cool, this is a valid word")
                                        
                                        
                                        correct=1
                                    if ((EBoard==1 and BTU==0 and spRow==int(BOARD_SIZE/2) and spCol==int(BOARD_SIZE/2)) or (EBoard==0 and BTU==1)) and TileUsed==1 and correct==1 and overlap==0:
                                        #print(spRow)
                                        #print(spCol)
                                        i=spRow
                                        j=spCol
                                        placable=1
                                        WL.append([word,spRow,spCol,direc,AI_BOARD_Tiles])
                                        #print(words)
                                        AIUWL.append(word)
                                        #print("VALID")
                                        for w in word:
                                            #Board[i][j]=w
                                            #print(i)
                                            if direc=="H":
                                                i=i+1
                                            else:
                                                j=j+1
                                            #for x in Scores:
                                                #if x[0]==w and not w in BOARD_Tiles:
                                                    #tscore= tscore+x[1]
                                        
                                        #break
                                    else:
                                        placable=0
                                    
                            #if(placable==1):
                                #words=([word,spRow,spCol,direc])
                                #print("checking2"+word)
                                #break
                        
                    #if(placable==1):
                        #print("checking3"+word)
                        #words=([word,spRow,spCol,direc])
                        #break
                #if(placable==1):
                    #words=([word,spRow,spCol,direc])
                    #print("checking4"+word)
                    #break       
                            

            else:
                #print("Word is not valid")
                direc=""
        
        
        wScore=0
        if WL:
            HWord=WL[0]
        else:
            print("No words can be made!")
            HWord=[]
        hScore=0
        for words in WL:
            word=words[0]
            spR=words[1]
            spC=words[2]
            d=words[3]
            AI_BOARD_Tiles=words[4]
            ##########################print("checking"+word)
            wScore=0
            for w in word:
                
                for x in Scores:
                    if x[0]==w and w not in AI_BOARD_Tiles:
                        wScore=wScore+x[1]
                        ########################print(wScore)
            if wScore>hScore:
                HWord=word
                HspR=spR
                HspC=spC
                Hd=d
                hScore=wScore
            
            
            wScore=0
        
    #if word:
    #    HWord=words[0]
    #    HspR=words[1]
    #    HspC=words[2]
    #    Hd=words[3]
    #    hScore=WordScore(HWord)
    #    print("High word :         "+HWord+"      "+str(hScore)+"   POS: "+str(HspR)+","+str(HspC)+"     DIR: "+Hd)
    #else:
    #    print("NO Words can be made!")
        
    #print("High word :         "+HWord+"      "+str(hScore)+"   POS: "+str(HspR)+","+str(HspC)+"     DIR: "+Hd)
   

    

    overlap=0
    BTU=0


    word = input("Enter a word ")
    #WordScore(word)
    #UWL=[]
    #######if correct==1:
    for v in Valid:
        if v==word:
            print(" you got it!")
            correct = 1
            for used in UWL:
                if word==used:
                    #print("USED")
                    correct=0
                    print("But it's already been used")
                    break
            break
        else:
            correct = 0
       
    if correct==1:
        spRow=input("Enter the row of the first letter: "+word[0])
        spCol=input("Enter the column of the first letter: "+word[0])
        if not spRow.isdigit() or not spCol.isdigit() or int(spCol)>=int(BOARD_SIZE) or int(spRow)>=int(BOARD_SIZE):
            print("Wrong input")
        else:
            direc=input("Enter the corresponding input for desired direction\nH.Horizontal\nV.Vertical")
            spRow=int(spRow)
            spCol=int(spCol)
            #print(direc)
            if not(direc=='H' or direc=='V'):
                direc=0
            if direc=="H":
                direc=1
            if direc=="V":
                direc=2
            
            #print(direc)
    else:
        print("Word is not valid")
        direc=0




    usableTiles=myTiles.copy()              #######################################################################ADD COMMENTS!!!!!!!!!!!!!!!!!!
    TILE = 0
#    for i in word:
#        if i in usableTiles:
#            TILE= TILE+1
#            usableTiles.remove(i)
#        else :
#            TILE = 0
#    if TILE != len(word) :
#        print("this word cannot be made using the tiles")
#        correct=0
#    else:
#        #########print("Cool, this is a valid word")
#        correct=1
#    







    ol=0

    if direc==1:
        if not spCol+len(word)<=BOARD_SIZE:
            print("Error, Can't place it")
        else:
            i=spRow
            j=spCol
            for w in word:
                if Board[i][j]=="":
                    ####print("free")
                    TileUsed=1
                else:
                    if Board[i][j]==w:
                        ######print(w+" BoardTileUsed")
                        usableTiles.append(w)
                        BOARD_Tiles.append(w)
                        BTU=1
                    else:
                        ol=1
                        break
                j=j+1



            for w in word:
                if w in usableTiles:
                    TILE= TILE+1
                    usableTiles.remove(w)
                else :
                    TILE = 0
                    break
            if TILE != len(word) :
                print("this word cannot be made using the tiles")
                correct=0
            else:
                #########print("Cool, this is a valid word")
                correct=1





                
            if (EBoard==1 and BTU==0 and spRow==int(BOARD_SIZE/2) and spCol==int(BOARD_SIZE/2)) or (EBoard==0 and BTU==1) and TileUsed==1 and correct==1 and ol==0:
                j=spCol
                score=0
                for w in word:
                    Board[i][j]=w
                    if w not in BOARD_Tiles:
                        TOB.append(w)
                    #print(j)
                    j=j+1
                    
                    for x in Scores:
                        if x[0]==w and not w in BOARD_Tiles:
                            tscore= tscore+x[1]
                            score= score+x[1]
                placed=1
            else:
                if(spRow!=int(BOARD_SIZE/2) or spCol!=int(BOARD_SIZE/2)):
                    print("The first move should be in the center of the board")
                    
        if TileUsed==0:
            print("You have to use use atleast one of your tiles")
        if(BTU==0 and EBoard==0):
            print("You have to use atleast one tile from the board")
                
    if direc==2:
        if not spRow+len(word)<=BOARD_SIZE:
            print("Error, Can't place it")
        else:
            i=spRow
            j=spCol
            for w in word:
                if Board[i][j]=="":
                    #print(str(i)+","+str(j)+w+" free")
                    TileUsed=1
                else:
                    if Board[i][j]==w:
                        #print(w+"BoardTileUsed")
                        usableTiles.append(w)
                        BOARD_Tiles.append(w)
                        BTU=1
                    else:
                        ol=1
                        break
                i=i+1



            for w in word:
                if w in usableTiles:
                    TILE= TILE+1
                    usableTiles.remove(w)
                else :
                    TILE = 0
            if TILE != len(word) :
                print("this word cannot be made using the tiles")
                correct=0
            else:
            #########print("Cool, this is a valid word")
                correct=1



                
            if (EBoard==1 and BTU==0 and spRow==int(BOARD_SIZE/2) and spCol==int(BOARD_SIZE/2)) or (EBoard==0 and BTU==1) and TileUsed==1 and correct==1 and ol==0:
                i=spRow
                score=0
                for w in word:
                    Board[i][j]=w

                    if w not in BOARD_Tiles:
                        TOB.append(w)
                    #print(i)
                    i=i+1
                    
                    for x in Scores:
                        if x[0]==w and not w in BOARD_Tiles:
                            tscore= tscore+x[1]
                            score= score+x[1]
                            
                placed=1
            else:
                if(spRow!=int(BOARD_SIZE/2) or spCol!=int(BOARD_SIZE/2)):
                    print("The first move should be in the center of the board")
                
        if TileUsed==0:
            print("You have to use use atleast one of your tiles")
        if(BTU==0 and EBoard==0):
            print("You have to use atleast one tile from the board")


                    
    if(placed==1):
        LastCorrect=1
        myTiles=usableTiles.copy()
        AIUWL.append(word)
        UWL.append(word)
        placed=0
        print("Your Score in this move "+str(score))
        if (int(hScore)<=score):
            print("BEST MOVE! Well Done!")
            
        else:
            #print("s")
            print("The best move was placing "+HWord+" with score "+str(hScore)+" at  POS: "+str(HspR)+","+str(HspC)+"  and   DIR: "+Hd)
    else:
        LastCorrect=0
        


        
    if direc==0:
        print("ERROR!")
    printBoard(Board)
    print("Your score is: ")
    print(tscore)


    getTiles(myTiles)
    #word = input("Enter a word to exit")
    printTiles(myTiles)
    BTU=0
    TileUsed=0
