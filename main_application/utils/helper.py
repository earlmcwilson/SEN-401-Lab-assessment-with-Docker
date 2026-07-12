import os
import requests

# In Docker Compose, the backend is reachable via its service name ("backend"),
# not localhost. Locally (running outside Docker) it defaults to 127.0.0.1:8000.
BASE_URL = os.environ.get("API_BASE_URL", "http://127.0.0.1:8000")

def _to_display(student: dict) -> dict:
    return {
        "id": student["id"],
        "name": student["full_name"],
        "matric_no": student["matric_no"],
        "gender": (student.get("gender") or "").replace("_", " ").title(),
        "score": student["score"],
        "department": student.get("department"),
        "profile_image": student.get("profile_image"),
    }

def get_students() -> list[dict]:
    response = requests.get(url=f"{BASE_URL}/students/")
    return [_to_display(s) for s in response.json()]

def get_student(id: str) -> dict:
    response = requests.get(url=f"{BASE_URL}/students/{id}")
    if response.status_code != 200:
        return None
    return _to_display(response.json())

def highest_score(students: list[dict]):
    if not students:
        return None
    return max(students, key=lambda s: s["score"])

def lowest_score(students: list[dict]):
    if not students:
        return None
    return min(students, key=lambda s: s["score"])

def get_average_score(students: list[dict]) -> float:
    if not students:
        return 0.0
    return sum(s["score"] for s in students) / len(students)

def get_departments(students: list[dict]) -> list[str]:
    return sorted({s.get("department") for s in students if s.get("department")})

def filter_by_department(students: list[dict], department: str) -> list[dict]:
    return [s for s in students if (s.get("department") or "").lower() == department.lower()]
        

def get_validated_student(student_id):
    student = get_student(student_id)
    if not student:
        return None, "Student not found."
    return student, None
