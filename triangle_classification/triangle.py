'''
Created on Sep 1, 2018
@author: Oscar Tavara
'''
triangleTypes = ["Scalene","Isosceles", "Equilateral"]

    
def validTriangle(sides):
    return ((len(sides) == 3) and (all(isinstance(x, float))for x in sides))

def validSide(side):
    return (side >= 0) and (isinstance(side, float))
        
def classifyTriangle(sides):
    sides.sort()
    sidesWithEqualLength = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if sides[i] == sides[j]:
                sidesWithEqualLength += 1
    if sidesWithEqualLength > 2:
        sidesWithEqualLength = 2
    isRight = (sides[0]**2 + sides[1]**2 == round(sides[2]**2, 2))
    return (('Right ' if isRight else '') + triangleTypes[sidesWithEqualLength] + " Triangle")

# def parseInputText(string, sides):
#     """Was going to make a separate function to parse instead of having it 
#         in the main function, but decided not to."""
#     whileLoopFlow = "continue"
#     if string[0].isalpha():
#         if string[0].lower() == "done":
#             if validTriangle(sides):
#                 whileLoopFlow = "break"
#             else:
#                 print("The entered triangle side(s) is not valid, try again.")
#                 whileLoopFlow = "continue/restart"
#         elif string[0].lower() == "restart":
#             whileLoopFlow = "continue/restart"
#         else:
#             print("The entered triangle side(s) is not valid, try again.")
#             whileLoopFlow = "continue/restart"
#     return whileLoopFlow
    
if __name__ == '__main__':
    sides = []
    while True:
        print("\nCurrent sides of triangle: ", sides)
        string = input("Please enter the lengths of the three side of a triangle. Enter done when finished or restart to start over.\n").replace(",", " ").split()
        if string == []:
            continue
        elif string[0].isalpha():
            if string[0].lower() == "done":
                if validTriangle(sides):
                    break
                else:
                    print("The entered triangle is not valid, try again.")
                    sides = []
                    continue
            elif string[0].lower() == "restart":
                sides = []
            else:
                print("Sorry, enter a valid number")
        else:
            for item in string:
                try: 
                    x = float(item)
                except:
                    print(item, " is not a valid number. Triangle restarted.")
                    sides = []
                    continue
                if validSide(x):
                    sides.append(x)
                else:
                    print(x, " is not a valid side. It must be a number that is greater than 0. Triangle restarted.")
                    sides = []
                    continue

    print(classifyTriangle(sides))