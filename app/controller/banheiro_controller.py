from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..model.banheiro_model import Banheiro
from ..schemas.schemas import BanheiroCreate, Banheiro as BathroomSchema, BanheiroPerto
from ..services.banheiro_service import get_banheiros_perto

router = APIRouter()

@router.post("/banheiros/create", 
    summary="Criar um banheiro",
    response_model=dict)
def create_bathroom(bathroom: BanheiroCreate, db: Session = Depends(get_db)):
    db_bathroom = Banheiro(**bathroom.model_dump())
    db.add(db_bathroom)
    db.commit()
    db.refresh(db_bathroom)
    return {"message": "Banheiro criado com sucesso"}

@router.get("/banheiros/perto", 
    summary="Achar banheiros perto",
    response_model=List[BanheiroPerto])
def achar_banheiros_perto(
    latitude: float = Query(..., description="Your current latitude"),
    longitude: float = Query(..., description="Your current longitude"),
    radius: float = Query(5, description="Search radius in kilometers"),
    db: Session = Depends(get_db)
):
    return get_banheiros_perto(db, latitude, longitude, radius)

@router.get("/banheiros", 
    summary="Pegar todos os banheiros",
    response_model=List[BathroomSchema])
def get_todos_banheiros(db: Session = Depends(get_db)):
    return db.query(Banheiro).all()