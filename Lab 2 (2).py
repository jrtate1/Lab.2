#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Calculation of Grades using UAlbany grading scale
grade_calculate_letter_grade(score):
    if score >= 93.0:
        return "A (93-100)"
    elif score >= 90.0:
        return"A- (90-92)"
    elif score >= 87.0:
        return "B+ (87-89)"
    elif score >= 83.0:
        return "B(83-86)"
    elif score >= 80.0:
        return "B- (80-82)"
    elif score >= 77.0:
        return "C+(77-79)"
    elif score >= 73.0:
        return "C (73-76)"
    elif score >= 70.0:
        return "C- (70-72)"
    elif score >= 60.0:
        return "D(60-69)"
    else:
        return "E(0-59)"
    
#Getting students score as an input
    score = str(input("Enter the student's socre: "))
    
#Explain range in which the number falls
    if score < 0 or score > 100:
        print("Wrong input : Score between 0 and 100")
    else:
        letter_score = calculate_letter_score(score)
        print(f"The student's letter grade is:{letter_grade}")
#2. Even or Odd

num = int(input("Enter an integer:"))

#Make sure even/odd
if number % 4==0:
    print(f"{num}is an even number.")
else:
    print(f"{num}is an odd number.")
    
#3 Largest number
#Ask the user to input a number of 4 digits

def is_four_digit(num):
    return 100<= num <= 9999

num = []
for i in range(3):
    number = int(input(f"Enter the {i +1}4 digit number:"))
    
    # Check if the input number is 4 Digits
    if is_four_digit(num):
        numbers.append(num)
    else:
        print("Wrong input: Please enter 4 digit- number")
        
    if len(num) == 3
        highest_num = max(num)
        print(f"The highest number of all {nums}")
        
        
# 4. Triangle Type 
tri1 = float (input("Enter length of first side: "))
tri2 =  float (input("Enter length of second side: "))
tri3 = float (input ("Enter length of third side:  "))

    if tri1 == tri2==side3:
        print("This is an eqailateral trinagle.")
    elif tri1== tri2 or tri1 == tri3 or tri2 ==tri3:
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")
        
        
 #5. State capitals
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
    "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
    "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]
    for state in states:
        print(state + " State."end=" ")
capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee",
    "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge",
    "Augusta", "Annapolis", "Boston", "Lansing", "St. Paul", "Jackson", "Jefferson City", "Helena", "Lincoln",
    "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City",
    "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier",
    "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"
]     
  for capital in capitals:
        print(capital + " City.", end=" ")
        
        
        


# In[4]:


#Calculation of Grades using UAlbany grading scale
grade_calculate_letter_grade(score):
    if score >= 93.0:
        return "A (93-100)"
    elif score >= 90.0:
        return"A- (90-92)"
    elif score >= 87.0:
        return "B+ (87-89)"
    elif score >= 83.0:
        return "B(83-86)"
    elif score >= 80.0:
        return "B- (80-82)"
    elif score >= 77.0:
        return "C+(77-79)"
    elif score >= 73.0:
        return "C (73-76)"
    elif score >= 70.0:
        return "C- (70-72)"
    elif score >= 60.0:
        return "D(60-69)"
    else:
        return "E(0-59)"
    
#Getting students score as an input
    score = str(input("Enter the student's socre: "))
    
#Explain range in which the number falls
    if score < 0 or score > 100:
        print("Wrong input : Score between 0 and 100")
    else:
        letter_score = calculate_letter_score(score)
        print(f"The student's letter grade is:{letter_grade}")


# In[5]:


#Calculation of Grades using UAlbany grading scale
def calculate_letter_grade(score):
    if score >= 93.0:
        return "A (93-100)"
    elif score >= 90.0:
        return"A- (90-92)"
    elif score >= 87.0:
        return "B+ (87-89)"
    elif score >= 83.0:
        return "B(83-86)"
    elif score >= 80.0:
        return "B- (80-82)"
    elif score >= 77.0:
        return "C+(77-79)"
    elif score >= 73.0:
        return "C (73-76)"
    elif score >= 70.0:
        return "C- (70-72)"
    elif score >= 60.0:
        return "D(60-69)"
    else:
        return "E(0-59)"
    
#Getting students score as an input
    score = str(input("Enter the student's socre: "))
    
#Explain range in which the number falls
    if score < 0 or score > 100:
        print("Wrong input : Score between 0 and 100")
    else:
        letter_score = calculate_letter_score(score)
        print(f"The student's letter grade is:{letter_grade}")


# In[ ]:


#Calculation of Grades using UAlbany grading scale
def calculate_letter_grade(score):
    if score >= 93.0:
        return "A (93-100)"
    elif score >= 90.0:
        return"A- (90-92)"
    elif score >= 87.0:
        return "B+ (87-89)"
    elif score >= 83.0:
        return "B(83-86)"
    elif score >= 80.0:
        return "B- (80-82)"
    elif score >= 77.0:
        return "C+(77-79)"
    elif score >= 73.0:
        return "C (73-76)"
    elif score >= 70.0:
        return "C- (70-72)"
    elif score >= 60.0:
        return "D(60-69)"
    else:
        return "E(0-59)"
    
#Getting students score as an input
    score = str(input("Enter the student's socre: "))
    
#Explain range in which the number falls
    if score < 0 or score > 100:
        print("Wrong input : Score between 0 and 100")
    else:
        letter_score = calculate_letter_score(score)
        print(f"The student's letter grade is:{letter_grade}")


# In[ ]:





# In[ ]:





# In[ ]:




