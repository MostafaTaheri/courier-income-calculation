from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    email: str


class CourierResponse(BaseModel):
    id: int
    user: UserResponse
