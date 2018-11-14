#nathan broadbent
#11/18
#questions
upperQ="this function turns all letters in a string into capital letters"
titleQ="this function capitalizes the first letter of every word"
flowChartQ="used to show how a program flows"
intQ="a whole number data type"
stringQ="a list of characters surrounded by quotations"
indexQ="a specific position in a string"
functionQ=" a block of code that you can call whenever"
variableQ="a defined value that can be called"
commentQ="a line of code that the computer doesn't read"
loopQ="a block of code that repeats itself"

#defining the puzzle
puzzle1="fqvindexkoclyaxepnffugohriludgvlbwninttxgkrtccaniognretheblttziipmaolpewormporsesnbotpugtzlscwsswjfe"
#score variable
score=0
# the trivia part of the game
def askQuestion(tQuestion,word,puzzle):
    attempts=10
    global score
    fullQuestion=tQuestion,"what is the term"
    while True:
        answer=input(fullQuestion)
        if answer.lower()==word:
            print("correct")
            score+=attempts*5
            puzzleSolve(word,attempts,puzzle)
            break
        else:
            attempts-=1
            print(attempts,"attempts left")
# the puzzle part of the game        
def puzzleSolve(word,attempts,puzzle):
    global score
    display="where is",word,"at in the puzzle put a comma between the index's"
    while True:
        displaypuzzle(puzzle)
        answer=input(display)
        input_number=""
        new_word=""
        for i in answer:
            
            if i ==",":
                print(input_number)
                input_number=int(input_number)
                new_word+=puzzle[input_number]
                input_number=""
            else:    
                input_number+=i  
        if new_word==word:
            print("correct")
            score+=attempts*10
            break
        else:
            attempts-=1
            print(attempts,"attempts left")

#displaying  the puzzle
def displaypuzzle(puzzle):
    print(" 0123456789")
    print("0",puzzle[0:10])
    print("1",puzzle[10:20])
    print("2",puzzle[20:30])
    print("3",puzzle[30:40])
    print("4",puzzle[40:50])
    print("5",puzzle[50:60])
    print("6",puzzle[60:70])
    print("7",puzzle[70:80])
    print("8",puzzle[80:90])
    print("9",puzzle[90:])
    print()
    
def main():
    askQuestion(upperQ,"upper",puzzle1)
    print("your Score is ",score)
    askQuestion(titleQ,"title",puzzle1)
    print("your Score is ",score)
    askQuestion(flowChartQ,"flowChart",puzzle1)
    print("your Score is ",score)
    askQuestion(intQ,"int",puzzle1)
    print("your Score is ",score)
    askQuestion(stringQ,"string",puzzle1)
    print("your Score is ",score)
    askQuestion(indexQ,"index",puzzle1)
    print("your Score is ",score)
    askQuestion(functionQ,"function",puzzle1)
    print("your Score is ",score)
    askQuestion(variableQ,"variable",puzzle1)
    print("your Score is ",score)
    askQuestion(commentQ,"comment",puzzle1)
    print("your Score is ",score)
    askQuestion(loopQ,"loop",puzzle1)
    print("your Final Score is ",score)
    
    
main()
