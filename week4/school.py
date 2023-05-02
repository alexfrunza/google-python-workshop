from typing import List


def check_number(x) -> bool:
    try:
        x = float(x)
        return True
    except ValueError:
        return False


def calculate_avg(arr: List[float]) -> float:
    return sum(arr) / len(arr)


class CatalogEntry:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

        self.courses = {}
        self.absences = 0

    def __str__(self):
        # Return message with singular form of the word absence
        if self.absences == 1:
            return f'{self.first_name} {self.last_name} - {self.absences} absence'

        return f'{self.first_name} {self.last_name} - {self.absences} absences'

    def increment_absences(self):
        self.absences += 1

    def motivate_absences(self, number: int):
        try:
            number = int(number)
            if number > self.absences:
                self.absences = 0
            else:
                self.absences -= number
        except ValueError:
            print("The argument must be an integer!")


class CatalogEntryExtension(CatalogEntry):
    def add_grades(self, course: str, grades: List[float]):
        self.courses[course] = grades

    def show_courses(self):
        print(f"Student, {self.first_name} {self.last_name} has the following courses:")
        for course in self.courses:
            print(course)

    def show_avg_grades(self):
        print(f"Student, {self.first_name} {self.last_name} has the following "
              f"grades averages:")
        for name, grades in self.courses.items():
            grades = list(filter(check_number, grades))

            # Error message for 0 division
            if len(grades) == 0:
                print(f"No grades for course {name}")
                continue

            grades = list(map(lambda x: float(x), grades))

            print(f"Avg grade at {name} is {calculate_avg(grades):.2f}")


# Verifications
student1 = CatalogEntryExtension("Ion", "Roata")
for _ in range(3):
    student1.increment_absences()

student1.motivate_absences(2)

student2 = CatalogEntryExtension("George", "Cerc")
for _ in range(4):
    student2.increment_absences()

student2.motivate_absences(2)

# Show absences
print(student1)
print(student2)
print()

student1.add_grades("Python", [9.9, 7, 8.5])
student2.add_grades("Python", [8, 10, 7.3])

student1.add_grades("Romana", [5, 8, 8])
student2.add_grades("Matematica", [10, 7, 9])

student1.show_courses()
print()
student2.show_courses()
print()

student1.show_avg_grades()
print()
student2.show_avg_grades()

