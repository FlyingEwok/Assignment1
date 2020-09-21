'''You will design a program that will ask the user to input an x number of elements. Then the program will give an average. Hint( You will want to ask the user to provide the number of elements initially. )'''

#Make a list of user inputed numbers
xnuminputs = []

#Ask user to enter numbers until they're done
while True:
  xnuminputs.append(int(input("Enter a number: ")))
  i = input("Type done if done otherwise press enter to continue: ")
  if i == "done":
    break
  else:
    continue

#Take the average of the lists numbers
Averagexnuminputs = sum(xnuminputs) / len(xnuminputs)

#Print the list and the average to console 
print("The entered numbers are: ", xnuminputs, "The Average of those numbers is: ", Averagexnuminputs)