from fastapi import HTTPException
from models.student_model import Student


students = []


def create_student(student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")

    students.append(student)
    return student


def get_all_students():
    return students


def get_student(student_id):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


def update_student(student_id, updated_student):
    for i in range(len(students)):
        if students[i].id == student_id:
            updated_student.id = student_id
            students[i] = updated_student
            return updated_student

    raise HTTPException(status_code=404, detail="Student not found")


def delete_student(student_id):
    for i in range(len(students)):
        if students[i].id == student_id:
            students.pop(i)
            return

    raise HTTPException(status_code=404, detail="Student not found")