from flask import Blueprint, jsonify, request
from database import get_connection
from pessoa_service_client import professor_existe

atividade_bp = Blueprint("atividade_bp", __name__)

@atividade_bp.route("/atividades", methods=["GET"])
def get_atividades():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descricao, professor_id FROM atividades")
    rows = cursor.fetchall()
    conn.close()

    atividades = []
    for row in rows:
        atividades.append({
            "id": row[0],
            "titulo": row[1],
            "descricao": row[2],
            "professor_id": row[3]
        })

    return jsonify(atividades), 200

@atividade_bp.route("/atividades/professor/<int:professor_id>", methods=["GET"])
def get_atividades_by_professor(professor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM atividades WHERE professor_id = ?", (professor_id,))
    atividades = cursor.fetchall()
    conn.close()

    if not atividades:
        return jsonify({"mensagem": "Nenhuma atividade encontrada para este professor"}), 404

    atividades_formatadas = [
        {"id": a[0], "nome": a[1], "disciplina": a[2], "professor_id": a[3]} for a in atividades
    ]

    return jsonify(atividades_formatadas), 200

@atividade_bp.route("/atividades", methods=["POST"])
def create_atividade():
    data = request.get_json()
    titulo = data.get("titulo")
    descricao = data.get("descricao")
    professor_id = data.get("professor_id")

    if not titulo or not descricao or not professor_id:
        return jsonify({"erro": "Campos 'titulo', 'descricao' e 'professor_id' são obrigatórios."}), 400
    
    if not professor_existe(professor_id):
        return jsonify({"erro": "Professor não encontrado."}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO atividades (titulo, descricao, professor_id) VALUES (?, ?, ?)", 
                   (titulo, descricao, professor_id))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Atividade criada com sucesso"}), 201

@atividade_bp.route("/atividades/<int:atividade_id>", methods=["DELETE"])
def delete_atividade(atividade_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM atividades WHERE id = ?", (atividade_id,))
    atividade = cursor.fetchone()

    if not atividade:
        conn.close()
        return jsonify({"erro": "Atividade não encontrada"}), 404

    cursor.execute("DELETE FROM atividades WHERE id = ?", (atividade_id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": f"Atividade com ID {atividade_id} foi removida com sucesso"}), 200