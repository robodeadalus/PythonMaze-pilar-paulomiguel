# Paulo Miguel A. Pilar
# 225008
# October 6, 2022

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.
maze = [ 
    [ 
    [1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,1,0,0,0,1],
    [1,1,1,1,1,1,1]
    ],
    [
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,1,1],
    [1,0,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1]
    ],
    [ 
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    ]
]

# --------------------
# Function Definitions
# --------------------
def PointLocations():
    initializingpoints=int(input("Starting point: "))
    userpositionX = (((initializingpoints//(UserLevelInput+2))*2)+1)
    userpostitionY = (((initializingpoints%(UserLevelInput+2))*2)+1)
    initializingpoints=int(input("Exit location: "))
    exitPositionX = (((initializingpoints//(UserLevelInput+2))*2)+1)
    exitPositionY = (((initializingpoints%(UserLevelInput+2))*2)+1)
    return userpositionX, userpostitionY,exitPositionX,exitPositionY

def printingmaze():
    outputMaze=[]
    for i in range (gridSize):
        tempList=[]
        for j in range(gridSize):
            if maze[UserLevelInput-1][i][j] == 0:
                tempList.append(" ")
            elif maze[UserLevelInput-1][i][j] ==1:
                tempList.append("■")
        outputMaze.append(tempList)
    return outputMaze

def objectLocation(x,y,character):
    realOutputMaze[x][y] = character

def directionChecker():
    availableDirections = "Available directions: "
    if realOutputMaze[userpositionX-1][userpostitionY] != "■":
        availableDirections+="North "
       
    if realOutputMaze[userpositionX+1][userpostitionY] != "■":
        availableDirections+="South "
    
    if realOutputMaze[userpositionX][userpostitionY+1] != "■":
        availableDirections+="East "
    
    if realOutputMaze[userpositionX][userpostitionY-1] != "■":
        availableDirections+="West"
    return availableDirections
# -----------------
# Program Execution
# -----------------
print("Welcome to the Maze!")
print("Select a level: 1, 2, or 3")
while True:
    UserLevelInput = int(input())
    if (UserLevelInput>= 1 and UserLevelInput <=3):
     break
gridSize = ((2*UserLevelInput)+5)
realOutputMaze = printingmaze()
positions = PointLocations() 
userpositionX = positions[0]
userpostitionY =positions[1]
exitPositionX = positions[2]
exitPositionY = positions[3]
objectLocation(userpositionX,userpostitionY, "O")
objectLocation(exitPositionX,exitPositionY,"X")

while True:
    if userpositionX == exitPositionX and userpostitionY == exitPositionY:
        for i in range(gridSize):
            print(*realOutputMaze[i])  
        print("Found the exit!")
        print("Goodbye.")
        break

    availableDirections = directionChecker()
    directionChecker()

    objectLocation(userpositionX,userpostitionY,"O")
    objectLocation(exitPositionX,exitPositionY,"X")
    for i in range(gridSize):
        print(*realOutputMaze[i])  
    print(availableDirections)
    print("Which direction will you take?")
  
    availableDirections.split()
    UserDirectionInput = input()
    if UserDirectionInput.lower() == "Quit".lower():
        print("\nTry again next time.")
        print ("Goodbye.")
        break
        
#Source CholoBoyCholoBoy(2017, September 17). How do I make a list comparison be case insensitive? Stack Overflow. Retrieved October 9, 2022, from https://stackoverflow.com/questions/46249507/how-do-i-make-a-list-comparison-be-case-insensitive CholoBoyCholoBoy(2017, September 17). How do I make a list comparison be case insensitive? Stack Overflow. 
# Retrieved October 9, 2022, from https://stackoverflow.com/questions/46249507/how-do-i-make-a-list-comparison-be-case-insensitive  

#Source: bitbuoybitbuoy. (2012, May 2). Check if something is (not) in a list in Python. Stack Overflow. 
# Retrieved October 9, 2022, from https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
    if UserDirectionInput.lower() not in availableDirections.lower():
        print("\nPlease choose an available direction.")
        continue

#Source: Hadzhiev, B. (2022, August 26). Make user input case-insensitive in python. bobbyhadz. 
# Retrieved October 9, 2022, from https://bobbyhadz.com/blog/python-make-user-input-case-insensitive#:~:text=Use%20the%20str.,do%20a%20case%2Dinsensitive%20comparison. 
    if UserDirectionInput.lower() == "North".lower():
        realOutputMaze[userpositionX][userpostitionY] =" "
        userpositionX-=2
      
    elif UserDirectionInput.lower() == "South".lower():
        realOutputMaze[userpositionX][userpostitionY] =" "
        userpositionX+=2

    elif UserDirectionInput.lower() == "East".lower(): 
        realOutputMaze[userpositionX][userpostitionY] =" "
        userpostitionY+=2
       
    elif UserDirectionInput.lower() == "West".lower():
        realOutputMaze[userpositionX][userpostitionY] =" "
        userpostitionY-=2
    print("\n")

        
    


        


