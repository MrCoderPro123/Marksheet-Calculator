def createFile(percentage, grade,eachmarks ,marksgained ,ttlmarks, marks):
    with open(f"{year}report.txt", "w") as f:
        f.write(f'''This is the Report of {name} from class {thisgrade}
                


{examname} Exams {year}-{int(year) + 1}

You got {marks[0]}/{eachmarks} in English
You got {marks[1]}/{eachmarks} in Maths
You got {marks[2]}/{eachmarks} in Urdu
You got {marks[3]}/{eachmarks} in Science
You got {marks[4]}/{eachmarks} in Sst
You got {marks[5]}/{eachmarks} in Computer
You got {marks[6]}/{eachmarks} in Sindi
You got {marks[7]}/{eachmarks} in Islamiat

You Scored {marksgained}/{ttlmarks}
Your Grade is {grade}
Your Percentage is {percentage}%
        ''')

def read_report(year):
    filename = f"{year}report.txt"
    try:
        with open(filename, "r") as f:
            content = f.read()
            
        # Extract score
        score_line = [line for line in content.split('\n') if "You Scored" in line][0]
        score = score_line.split()[-1]
        
        # Extract grade
        grade_line = [line for line in content.split('\n') if "Your Grade is" in line][0]
        grade = grade_line.split()[-1]
        
        # Extract percentage
        percentage_line = [line for line in content.split('\n') if "Your Percentage is" in line][0]
        percentage = percentage_line.split()[-1].rstrip('%')
        
        return float(percentage), grade, score
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None, None, None

# Usage example:
# year = input("Enter the year of the report you want to read: ")
# percentage, grade, score = read_report(year)
# if percentage is not None:
#     print(f"Percentage: {percentage}%")
#     print(f"Grade: {grade}")
#     print(f"Score: {score}")


def calcGrade(percentage):
    if (percentage > 80 and percentage <= 100):
        print("Your Grade is A+! Exellent!")
        grade = "A+"
    elif (percentage > 60 and percentage <= 80):
        print("Your Grade is B. Good Work!")
        grade = "B"
    elif (percentage > 40 and percentage <= 60):
        print("Your Grade is C. Average.")
        grade = "C"
    elif (percentage > 30 and percentage <= 40):
        print("Your Grade is D. You Need to improve.")
        grade = "D"
    elif (percentage > 10 and percentage <= 30):
        print("Your Grade is F. You Failed!")
        grade = "F"
    elif (percentage <= 10):
        print("You are staying in this grade for another year! You need serios Improvement. Your Grade is F-")
        grade = "F-"
    else:
        print("Invalid Percentage")
    
    return grade

work = input("What do you wanna do? [Add Report (c), Get Report (g)]")

if work == 'g':
    year = input("Enter the year of the report you want to read: ")
    percentage, grade, score = read_report(year)
    if percentage is not None:
        print(f"Percentage: {percentage}%")
        print(f"Grade: {grade}")
        print(f"Score: {score}")
else:
    name = input("Enter Your Full Name: ")
    thisgrade = input("Enter Your Class: ")
    year = input("Enter the Year of Exams: ")
    examname = input("Which Exams marks are you giving: ")



    eachTotalMarks = int(input("Enter Total Marks of each Subject: "))
    totalMarks = eachTotalMarks * 8

    engMarks = int(input("Enter your Marks in English: "))
    totalMarksGained = engMarks
    mathMarks = int(input("Enter your Marks in Maths: "))
    totalMarksGained += mathMarks
    urdmarks = int(input("Enter your Marks in Urdu: "))
    totalMarksGained += urdmarks
    sciMarks = int(input("Enter your Marks in Science: "))
    totalMarksGained += sciMarks
    sstMarks = int(input("Enter your Marks in Sst: "))
    totalMarksGained += sstMarks
    compMarks = int(input("Enter your Marks in Computer: "))
    totalMarksGained += compMarks
    sinMarks = int(input("Enter your Marks in Sindhi: "))
    totalMarksGained += sinMarks
    islMarks = int(input("Enter your Marks in Islamiat: "))
    totalMarksGained += islMarks

    print(f"You got {totalMarksGained}/{totalMarks}")
    percentage = (totalMarksGained*100) / totalMarks
    print(f"Your Percentage is {percentage}")
    grade = calcGrade(percentage)

    wantFile = input("Do you want a seperate .txt file with all your percentage? [Y/N]: ")
    if (wantFile == "Y"):
        createFile(percentage, grade,eachTotalMarks ,totalMarksGained ,totalMarks ,[engMarks,mathMarks,urdmarks,sciMarks,sstMarks,compMarks,sinMarks,islMarks])
        print("Your File has been created as report.txt")





