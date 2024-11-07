############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Chauntel Smith

# main() FUNCTION
def main():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    

    def GradeOutcomes(GradeList,numericGrade):
        GradeList = []
        numericGrade = 0.0
    

        #Gather user inputs
        print("please enter your grades for each class in this order:\nPROG1700\nNETW1700\nOSYS1200\nWEBD1000\nCOMM1700\nDBAS1007")
        for i in range(6):
            letterGrade = input("Please enter a letter grade : ").upper()
            modifier = input("Please enter a modifier (+, - or nothing) : ")
        GradeList.count(numericGrade)

     # Determine base numeric value of the grade
        if letterGrade == "A":
            numericGrade = 4.0
        elif letterGrade == "B":
            numericGrade = 3.0
        elif letterGrade == "C":
            numericGrade = 2.0
        elif letterGrade == "D":
            numericGrade = 1.0
        elif letterGrade == "F":
            numericGrade = 0.0
        else:
            #If an invalid entry is made
            print("You entered an invalid letter grade.")
    
        # Determine whether to apply a modifier
        if modifier == "+":
            if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                numericGrade += 0.3
        elif modifier == "-":
            if letterGrade != "F":     # Minus is not valid on F
                numericGrade -= 0.3

    print("The numeric value is for PROG1700 is: {0}\nThe numeric value is for NETW1700 is: {1}\nThe numeric value is for OSYS1200 is: {2}\nThe numeric value is for WEBD1000 is: {3}\nThe numeric value is for COMM1700 is: {4}\nThe numeric value is for DBAS1007 is: {5}".format(Gradelist[0,1,2,3,4,5],))
    return GradeOutcomes
  
        # Output final message and result, with formatting

    #PROGRAM EXECUTION STARTS HERE


main()