def test_create_banheiro(client):
    banheiro_data = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "name": "Test banheiro",
        "rating": 5,
        "review": "Limpo e bacana",
        "accessibility":True
    }
    
    response = client.post("/api/v1/banheiros/create", json=banheiro_data)
    assert response.status_code == 200

def test_get_all_banheiros_vazio(client):
    response = client.get("/api/v1/banheiros")
    assert response.status_code == 200

def test_get_all_banheiros(client):
    banheiro_data = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "name": "Test banheiro",
        "rating": 2,
        "review": "Meio vagabundo",
        "accessibility":True
    }
    client.post("/api/v1/banheiros/create", json=banheiro_data)
    
    response = client.get("/api/v1/banheiros")
    assert response.status_code == 200
    banheiros = response.json()
    assert len(banheiros) == 1
    assert banheiros[0]["name"] == "Test banheiro"

def test_get_nearby_banheiros(client):
    banheiros = [
        {
            "latitude": 40.7128,
            "longitude": -74.0060,
            "name": "NYC banheiro",
            "rating": 5,
            "review": "Clean",
            "accessibility":True
        },
        {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "name": "LA banheiro",
            "rating": 3,
            "review": "OK",
            "accessibility":False
        }
    ]
    
    for banheiro in banheiros:
        client.post("/api/v1/banheiros/create", json=banheiro)
    
    response = client.get("/api/v1/banheiros/perto", params={
        "latitude": 40.7128,
        "longitude": -74.0060,
        "radius": 10
    })
    
    assert response.status_code == 200
    nearby = response.json()
    assert len(nearby) == 1
    assert nearby[0]["name"] == "NYC banheiro"

def test_get_nearby_banheiros_parametros_invalidos(client):
    response = client.get("/api/v1/banheiros/perto", params={
        "latitude": "invalid",
        "longitude": -74.0060,
        "radius": 10
    })
    assert response.status_code == 422
