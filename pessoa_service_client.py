import requests

def professor_existe(professor_id):
    try:
        response = requests.get(f"http://localhost:5000/professores/{professor_id}")
        return response.status_code == 200
    except:
        return False
    
def get_professor_nome_por_id(professor_id):
    try:
        response = requests.get(f"http://localhost:5000/professores/{professor_id}")
        if response.status_code == 200:
            return response.json().get("nome")
        return None
    except requests.exceptions.RequestException:
        return None