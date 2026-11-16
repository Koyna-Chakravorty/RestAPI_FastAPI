from pydantic import BaseModel, Field, model_validator

class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str | None = None 
    completed: bool = False 


class Task(TaskCreate):
    id: int


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    description: str | None = None
    completed: bool | None = None

    @model_validator(mode="after")
    def validate_updates(self):
        if "title" in self.model_fields_set and self.title is None:
            raise ValueError("Title cannot be null")

        if "completed" in self.model_fields_set and self.completed is None:
            raise ValueError("Completed cannot be null")

        return self