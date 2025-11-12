#Andrew Blanchard
#Project 1

#The creates the class student
class Student:
    #This is the init function for the class student that allows me to easily create multiple instances of students in this said class.
    def __init__(self, id, first, last):
        self.id = id
        self.first = first
        self.last = last

    def set_GPA(self, new_Set_GPA):
        self.GPA = float(new_Set_GPA)
        #If the student's gpa is less than 2, they go on probation, if the student's gpa is greater than 2, they don't need to be on probation.
        if(self.GPA < float(2)):
            self.probation = True
            print("\nThis student is in bad standing, they are now On Probation")
        else:
            self.probation = False
            print("\nThis student is in good standing, they are now Not On Probation")
        return self.probation

#This function outside the class is supposed to display all students, it infact does this fairly well.
def display_all(studentList):
    for person in studentList:
        print(f"Student: {person.first} {person.last} has the ID of {person.id}")

#This is a list containing all student IDs as they get created. If the name wasn't clear enough, it should contain only the IDs of the students.
listID = []

def enter_GPA(studentList,ProbationDic):
    answer = int(input("\nWhat student ID would you like to choose? Please enter their ID: "))
    for peer in studentList:
        listID.append(peer.id)
        #This section is grabbing the ID you asked for, checking if valid in the list...
    if(answer in listID):
        print("This student does exist, yay!")
        secondAnswer = float(input("\nWhat would you like to set their GPA to? Enter a valid number: "))
        #Then asks for a float value between 0.0 and 5.0 for this school's gpa system, then sets it as that student's gpa.
        if(secondAnswer <= 5.0 and secondAnswer >= 0.0):
            for person in studentList:
                if(person.id == answer):
                    probationVariable = person.set_GPA(secondAnswer)
                    ProbationDic[answer] = probationVariable
        else:
            print("Invalid GPA, try again.")
    else:
        print("This student does not exist, try again.")

#This dictionatary takes the answerthree as the student ID to get the value of the key.
ProbationDic = {}

#This function displays the probation, oh wait, that was in the name... Anywho this function works when the set_gpa function isn't being awful.
def display_probation():
    answerthree = int(input("What student would you like to view the probation status of? Please enter their ID: "))
    #Checks if student is in the ID list, then prints whether or not they are in good standing.
    if(answerthree in listID):
        ProbationVar = ProbationDic[answerthree]
        if(ProbationVar == True):
            print("This student is under acadmic probation.")
        else:
            print("This student is in good acadmic standing.")
    else:
        print("This student does not exist or has not been assigned a GPA.")

#This is where all of my code runs
def main():
    #I created 4 instances of Student
    student_1 = Student(1, "Timmy", "Turnaround")
    student_2 = Student(2, "Ben", "Dover")
    student_3 = Student(3, "Mike", "Raphone")
    student_4 = Student(4, "Eileen", "Dover")
    #They are all very funny.

    studentList = [student_1,student_2,student_3,student_4]

    #The most main portion of the code, the code loop of asking for students.
    name = input("\nWelcome to the College Student Tracker, please enter your user name to continue, anything works for us: ")
    while(True):
        print(f"\nHi {name}, welcome to the system. Would you like to: \n 1. See the list of all enrolled students? \n 2. Edit a student's GPA \n 3. Do a quick lookup to see if a student is under acadmic probation.")
        numberChosen = int(input("\nEnter HERE: "))
        #Uses the number selected to call on specific functions in my code.
        if(numberChosen <= 3 and numberChosen >= 1):
            if(numberChosen == 1):
                display_all(studentList)
            if(numberChosen == 2):
                enter_GPA(studentList,ProbationDic)
            if(numberChosen == 3):
                display_probation()
        else:
            print("ERROR, Try Again, invalid selection")

#This starts my code and actually makes it function.
main()