from pydantic import BaseModel, field_validator

from fastapi import HTTPException

class NewUser(BaseModel):
    user_id: str
    password: str
    name: str
    age: int
    gender: str
    job: str
    further_details: str=None

    @field_validator('user_id', 'password', 'name', 'age', 'gender', 'job')
    def check_empty(cls, input):
        if not input or input.isspace():
            raise HTTPException(status_code=422, detail="필수 항목을 모두 입력해주세요.")
        return input
    
    @field_validator('password')
    def validate_password(cls, input):
        if len(input) < 8:
            raise HTTPException(status_code=422, detail="8자리 이상의 영문 + 숫자 비밀번호를 입력해주세요.")
        if all(char.isdigit() for char in input):
            raise HTTPException(status_code=422, detail="영문을 포함해서 비밀번호를 입력해주세요.")
        if all(char.isalpha() for char in input):
            raise HTTPException(status_code=422, detail="숫자를 포함해서 비밀번호를 입력해주세요.")