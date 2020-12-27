# Student Management System
import sys
student = input("Please enter your name and surname: ").title()
i=0
while i<3:
      Check = input("Enter again your name and surname: ").title()
      if (Check == student ):
          print("Welcome {}! ".format(student))
          break
      else:
         print("Please try again.")
         i+=1
         if(i==3):
            print("Invalid login!!!")
            sys.exit()

b = int(input("How many lessons do you have? : "))

while 5 >=b>=3:

    break

while b<3:
   print("You failed in class!")
   sys.exit()

while b>5:
   print("You can't take more than 5 lessons")
   b = int(input("Enter less than 5 lessons: "))
   break

lessonList = []

for i in range(b):
        lesson = input(f"Enter the {i + 1}. lesson: ")
        lessonList.append(lesson)
print(lessonList)


Lesson = input(f"Enter the lesson: ")
grades = {'midterm exam': 0, 'final': 0, 'project': 0}

midterm = int(input('Enter your midterm exam grade: '))
grades['midterm exam'] = midterm

final = int(input('Enter your final grade: '))
grades['final'] = final

project = int(input('Enter your project grade: '))
grades['project'] = project

your_grade = grades['midterm exam'] * 0.3 + grades['final'] * 0.2 + grades['project'] * 0.5
grades = {'midterm exam': midterm, 'final': final, 'project': project}
print(grades)

if your_grade >= 90:
    print(f'You got AA from {Lesson} lesson')
elif 90 > your_grade and your_grade >= 70:
    print(f'You got BB from {Lesson} lesson')
elif 70 > your_grade and your_grade >= 50:
    print(f'You got CC from {Lesson} lesson')
elif 50 > your_grade and your_grade >= 30:
    print(f'You got DD from {Lesson} lesson')
elif 30 > your_grade:
    print(f'You got FF from {Lesson} lesson.You failed!!')