# 1. Create a class of cohort 4
#Class name starts with a capital letter is ever in singular 
# class  Cohort:
    #name
    #decription 
    #start_date
    #end-date

# Within the cohort class, add a constructor for the cohort class
#Add a method to the class that prints the cohort name and the total number of students
#create a new instance of the cohort class
#No 1
class Cohort:
    def __init__(self,name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

p1 = Cohort("Daniela", "Love python", "20th/August/2024", "20th/August/2026")

print(p1.name)
print(p1.description)
print(p1.start_date)
print(p1.end_date)

#No.2

class Cohort4:
    def __init__(self,name, student_total_number):#the method to print the class name and total number of students
        
        self.name = name
        self.student_total_number = student_total_number

p1 = Cohort4("Computer science", 55)#The instance created 

print(f"Cohort Name: {p1.name}")
print(f"Total number of students: {p1.student_total_number}")
