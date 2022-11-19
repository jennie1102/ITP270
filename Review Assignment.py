class Student:
	def __init__(self, name, year):
		self.name = name
		self.year = year
		self.grades = []
		self.attendance = {}
	def get_average(self):
		grade_sum = 0
		count = 0
		for i in self.grades:
			count += 1
			grade_sum += i
		return grade_sum / count
	def add_grade(self, grade):
		if type(grade) is int:
			self.grades.append(grade)
class Grade:
	minimum_passing = 65
	def __init__(self, score):
		self.score = score

	def is_passing(self, score):
		if score >= self.minimum_passing:
			return "is a passing Grade"
		else:
			return "is not a passing Grade"

roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

list_of_assignments1 = [100, 0, 50]
list_of_assignments2 = [90, 80, 55]
list_of_assignments3 = [65, 64, 65, 68]

student_score = Grade(0)
print(student_score.is_passing(89))
print(pieter.grades)
print(pieter.get_average())

pieter.attendance['01/01/22'] = 'Present'
pieter.attendance['01/02/22'] = 'Absent'
pieter.attendance['01/03/22'] = 'Present'

print(pieter.attendance)
