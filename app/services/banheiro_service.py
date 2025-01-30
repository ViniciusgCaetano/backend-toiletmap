from math import radians, sin, cos, sqrt, atan2
from sqlalchemy.orm import Session
from typing import List
from ..model.banheiro_model import Banheiro

def calcula_distancia(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two points using Haversine formula"""
    R = 6371  # Earth's radius in kilometers
    
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    return R * c

def get_banheiros_perto(db: Session, latitude: float, longitude: float, radius: float = 5) -> List[dict]:
    """Get bathrooms within specified radius"""
    bathrooms = db.query(Banheiro).all()
    nearby = []
    
    for bathroom in bathrooms:
        distance = calcula_distancia(latitude, longitude, bathroom.latitude, bathroom.longitude)
        if distance <= radius:
            bathroom_dict = {
                "id": bathroom.id,
                "latitude": bathroom.latitude,
                "longitude": bathroom.longitude,
                "name": bathroom.name,
                "rating": bathroom.rating,
                "review": bathroom.review,
                "accessibility": bathroom.accessibility,
                "created_at": bathroom.created_at,
                "distance": round(distance, 2)
            }
            nearby.append(bathroom_dict)
    
    return sorted(nearby, key=lambda x: x["distance"])