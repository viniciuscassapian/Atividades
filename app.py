from flask import Flask
from atividade_controller import atividade_bp
from database import init_db

app = Flask(__name__)
app.register_blueprint(atividade_bp)

if __name__ == "__main__":
    init_db()
    app.run(port=5002, debug=True)
    