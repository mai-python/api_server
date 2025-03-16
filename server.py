from flask import Flask, request, jsonify

app = Flask(__name__)

# 원격 조종 명령 저장
command = {"action": "none"}

@app.route("/send_command", methods=["POST"])
def send_command():
    global command
    data = request.json  # JSON 데이터 받기
    print(f"📥 서버에서 받은 데이터: {data}")  # 디버깅용 로그 추가

    if data and data.get("action") in ["start", "stop"]:
        command = data
        return jsonify({"status": "command received", "command": command})

    return jsonify({"status": "error", "message": "Invalid command"}), 400

@app.route("/get_command", methods=["GET"])
def get_command():
    return jsonify(command)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
