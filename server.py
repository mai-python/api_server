from flask import Flask, request, jsonify

app = Flask(__name__)

# 명령 상태 저장
command = {"action": "stop"}  # 기본 상태는 "정지"

@app.route("/send_command", methods=["POST"])  # POST 메서드로 명령 처리
def send_command():
    global command
    data = request.json  # {"action": "start"} 또는 {"action": "stop"}
    
    if data and data.get("action") in ["start", "stop"]:
        command = data
        return jsonify({"status": "command received", "command": command})
    
    return jsonify({"status": "error", "message": "Invalid command"}), 400

@app.route("/get_command", methods=["GET"])  # GET 메서드로 명령 상태 조회
def get_command():
    return jsonify(command)

if __name__ == "__main__":
    app.run(debug=True)
