from app.services.banheiro_service import calcula_distancia

def test_calcula_distancia():
    ny_lat, ny_lon = 40.7128, -74.0060
    la_lat, la_lon = 34.0522, -118.2437
    
    distance = calcula_distancia(ny_lat, ny_lon, la_lat, la_lon)
    
    assert 3900 < distance < 4000