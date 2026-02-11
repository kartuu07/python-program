grades = {"Kartvya":"A","Saad":"B"}
attendence = {"Kartvya":"90","Saad":"85"}

grades["Kartvya"] = "A"
attendence["kartvya"] = "60"

grades["Tathagat"] = "B"
attendence["Tathagat"] = "85"

grades.pop("Saad")
attendence.pop("Saad")

for student in grades:
    print(student,"-Grades",grades[student],"Attendence",attendence[student])
