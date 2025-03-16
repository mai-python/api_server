from flask import Flask, request, jsonify

app = Flask(__name__)

# 원격 조종 명령 저장
command = {"action": "none"}

# 원격 조종 명령을 서버에 저장하는 API
@app.route("/send_command", methods=["POST"])
def send_command():
    global command
    data = request.json  # {"action": "start"} 또는 {"action": "stop"}
    if data.get("action") in ["start", "stop"]:
        command = data
        return jsonify({"status": "command received", "command": command})
    return jsonify({"status": "error", "message": "Invalid command"}), 400

# 현재 저장된 명령을 반환하는 API
@app.route("/get_command", methods=["GET"])
def get_command():
    return jsonify(command)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
