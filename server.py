from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS를 import

app = Flask(__name__)
CORS(app)  # CORS 설정 추가

@app.route('/get_command', methods=['POST'])
def get_command():
    data = request.get_json()  # 클라이언트에서 보낸 JSON 데이터
    action = data.get('action', 'stop')  # 기본값은 'stop'
    print(f"Received action: {action}")
    
    # action에 따라서 처리 (여기서는 예시로 'start'와 'stop'을 처리합니다)
    if action == "start":
        response = {"action": "start", "status": "operating"}
    elif action == "stop":
        response = {"action": "stop", "status": "paused"}
    else:
        response = {"action": "error", "status": "invalid action"}
    
    # 상태를 JSON 형식으로 반환
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # 포트 5000에서 실행
