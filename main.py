class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, teacher, course, grade): # Оценка лекций от студентов
        if isinstance(teacher, Lecturer) and course in self.courses_attached and course in teacher.courses_in_progress:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg(self):
        self.numbers = []
        for key, value in self.grades.items():
            for number in value:
                self.numbers.append(number)
        res = sum(self.numbers) / len(self.numbers)
        return res

    def __str__(self): # Крутая "ПАСТА"
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_avg()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.get_avg() < other.get_avg()
 

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def get_avg(self):
        self.numbers = []
        for key, value in self.grades.items():
            for number in value:
                self.numbers.append(number)
        res = sum(self.numbers) / len(self.numbers)
        return res
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.get_avg() < other.get_avg()


class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade): # Оценка домашки Ревьюером
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



# best_student = Student('Хлеб', 'Булкович', 'Мужской')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Олег', 'Булыгин')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
student_1 = Student('Алексей', 'Чебуреков', 'Мужской')
student_2 = Student('Доминик', 'Торрента', 'Бензин')
reviewer_1 = Reviewer('Доктор', 'Дре')
reviewer_2 = Reviewer('Асап', 'Роки')
lecturer_1 = Lecturer('Джон', 'Сина')
lecturer_2 = Lecturer('Хабиб', 'Нурмагомедов')

students_list = [student_1, student_2]
reviewer_list = [reviewer_1, reviewer_2]
lecturer_list = [lecturer_1, lecturer_2]

def drake(students_list, course):
    








# class HomeWork:
#     grades = {'Python': [10, 18, 18, 10], 'Java': [8, 2, 4, 5]}

#     def get_avg(self, student_1, selected):
#         self.numbers = []
#         for key, value in self.grades.items():
#             if key == selected:
#                 for number in value:
#                     self.numbers.append(number)
#         res = sum(self.numbers) / len(self.numbers)
#         return res
