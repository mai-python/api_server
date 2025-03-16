import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask 서버가 정상적으로 실행 중입니다!"

# Render의 포트 환경 변수 사용
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render에서 할당된 포트 사용
    app.run(host="0.0.0.0", port=port)
