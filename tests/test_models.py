from sqlalchemy import create_engine
from app.model.banheiro_model import Banheiro
from sqlalchemy.orm import sessionmaker

def test_create_bathroom(test_db):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = local_session()
    bathroom = Banheiro(
        latitude=40.7128,
        longitude=-74.0060,
        name="Teste",
        rating=5,
        review="Limpo",
        accessibility=True

    )
    db.add(bathroom)
    db.commit()
    
    saved_bathroom = db.query(Banheiro).first()
    assert saved_bathroom.name == "Teste"
    assert saved_bathroom.rating == 5
    db.close()