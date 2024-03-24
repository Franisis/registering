from pydantic import BaseModel
from datetime import date
class Service(BaseModel):
    name : str
    description:str
    dateAdded: date 
    lastcheck: str
    errorReport: list = []

    @classmethod
    def create_with_today_date(cls, **data):
        today_date = date.today()
        data['dateAdded'] = today_date
        return cls(**data)

    class Config:
        orm_mode = True