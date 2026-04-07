from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str='devanshu'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,
                     lt=10,
                     default=5,
                     description='A decimal value representing the cgpa of student')

new_student={'age':'20','email':'abc@example.com','cgpa':'9.3'}

student=Student(**new_student)

student_dict=dict(student)
student_json=student.model_dump_json()

print(student_dict['email'])
print(student_json)