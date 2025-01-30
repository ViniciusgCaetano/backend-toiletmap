from pydantic import BaseModel, conint, Field
from datetime import datetime

class BanheiroBase(BaseModel):
    latitude: float = Field(..., example=40.7128)
    longitude: float = Field(..., example=-74.0060)
    name: str = Field(..., example="Central Park Restroom")
    rating: int= Field(..., example=2)
    review: str = Field(..., example="Clean and well-maintained")
    accessibility: bool = Field(..., example="True")

class BanheiroCreate(BanheiroBase):
    pass

class Banheiro(BanheiroBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class BanheiroPerto(Banheiro):
    distance: float = Field(..., description="Distance in kilometers")