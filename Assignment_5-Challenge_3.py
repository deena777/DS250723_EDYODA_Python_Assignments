# Challenge 3: Implement the Complete Student Class

class Student:
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_rollnumber(self, rollnumber):
        self.__rollnumber = rollnumber

    def get_rollnumber(self):
        return self.__rollnumber

    def display_student_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Roll Number: {self.get_rollnumber()}")



student1 = Student()

name = input("Name of student : ")
rollnumber = input("Roll Number of student : ")
student1.set_name(name)
student1.set_rollnumber(rollnumber)

print("\nStudent Info")
student1.display_student_info()
