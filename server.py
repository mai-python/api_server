import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# 명령 상태 저장
command = {"action": "stop"}  # 기본 상태는 "정지"

@app.route("/")
def home():
    return "Flask 서버가 정상적으로 실행 중입니다!"

# Kivy 앱에서 명령 전송
@app.route("/send_command", methods=["POST"])
def send_command():
    global command
    data = request.json  # {"action": "start"} 또는 {"action": "stop"}
    
    if data and data.get("action") in ["start", "stop"]:
        command = data
        return jsonify({"status": "command received", "command": command})
    
    return jsonify({"status": "error", "message": "Invalid command"}), 400

# 현재 명령 상태 조회 (앱에서 사용)
@app.route("/get_command", methods=["GET"])
def get_command():
    return jsonify(command)

# Render의 포트 환경 변수 사용
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render에서 할당된 포트 사용
    app.run(host="0.0.0.0", port=port)
