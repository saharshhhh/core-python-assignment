class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

average_marks = {name: Student(name, marks).average_marks() for name, marks in students.items()}
top_performer = max(average_marks, key=average_marks.get)

print(f"Average Marks: {average_marks}")
print(f"Top Performer: {top_performer}")