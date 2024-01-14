class student:
    def __init__(self,x,y,z):
        self.name = x
        self.grade = y
        self.major = z
        self.courses = []

    def enroll_courses(self, course):
        if len(self.courses) < 5 :
            self.courses.append(course)
        else:
            print("수업 과목이 너무 많습니다")

    def cancel_course(self):
        if len(self.courses) ==0:
            print('과목이 없습니다.')
        else:
            for index, item in enumerate(self.courses):
                print(f"{index}.{item}")

            removetarget = int(input("빼고 싶은 과목의 번호를 선택:"))
            del self.courses[removetarget]

    def informate(self):
        print(f"학생 이름 : {self.name} 학년 : {self.grade}, 학생전공 : {self.major}")
        print("학생의 수업리스트:")
        for i in self.courses:
            print(f"{i}")


kim = student('김주영', '3', '철학과')
kim.enroll_courses('철학의이해')
kim.enroll_courses('철학의쓸모')

kim.informate()

class Circle:
    def __init__(self,x):
        self.area = x**2 * 3.14
        self.round = x*2*3.14

    def information(self):
        print(f"윈의 넓이는 {self.area}, 원의 둘레는 {self.round} 입니다.")

radius = Circle(10)

radius.information()



