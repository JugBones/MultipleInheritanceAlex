#class person - parent class
class Person:
    
    def __init__(self, name, address):
        self._name = name
        self._address = address
        
    def getName(self):
        return self.__name
    
    def getAdress(self):
        return self.__address
    
    def setName(self, name):
        self.__name = name
    
    def setAdress(self, address):
        self.__address = address
        
    def __str__(self):
        return "Name : {} , Address: {} ".format(self._name(), self._address())
    

class Student(Person):
    
    def __init__ (self, name, address, numCourses = 0, courses = [], grades = []):
        super().__init__(name,address)
        self.__courses = []
        self.__grades = []
        
    def getAverageGrade(self,grades):
        return sum(grades)/len(grades)
    
    def addCourseGrade(self,courses,grades):
        self.__courses = courses
        self.__grades = grades
    
    def printGrades(self):
        print("Course: {}, Grade: {}".format(self.__courses, self.__grades))
        
    def __str__(self):
        return "Student name: {} , Address: {}".format(self.getName(), self.getAddress())


class Teacher(Person):
    
    def __init__ (self, name, address,numCourses=0,courses=[]):
        super().__init__(name,address)
        self.__numCourses = numCourses
        self.__courses = courses
      
    def addCourses(self, courses):
        self.__courses = courses
        if courses in self.__courses:
            print("your course already exist mam/mister!")
            return False
        self.__courses.append(courses)
        self.__numCourses +=1
        
    def removeCourse(self,course):
        if course not in self.__courses:
            print("The course does not exist")
            return False
        self.__courses.remove(course)
        self.__numCourses -= 1
        
    def __str__(self):
        return "Teacher name: {} , Address: {}".format(self.getName(),self.getAddress())
