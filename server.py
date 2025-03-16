from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

# Flask 서버 주소 (Render에서 배포한 서버 URL 입력)
SERVER_URL = "https://api-server-huax.onrender.com/send_command"

class ControlApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # 상태 표시 레이블
        self.status_label = Label(text="state: standby", font_size=20)
        self.add_widget(self.status_label)

        # "operate" 버튼
        start_button = Button(text="operate", font_size=24, size_hint=(1, 0.3))
        start_button.bind(on_press=lambda x: self.send_command("start"))
        self.add_widget(start_button)

        # "stop" 버튼
        stop_button = Button(text="stop", font_size=24, size_hint=(1, 0.3))
        stop_button.bind(on_press=lambda x: self.send_command("stop"))
        self.add_widget(stop_button)

    def send_command(self, action):
        """Flask 서버로 명령을 전송하는 함수"""
        try:
            data = {"action": action}
            headers = {"Content-Type": "application/json"}
            response = requests.post(SERVER_URL, json=data, headers=headers)

            # HTTP 응답 코드에 따른 처리
            if response.status_code == 200:
                result = response.json()
                self.status_label.text = f"state : {result.get('command', {}).get('action', 'error')}"
            elif response.status_code == 404:
                self.status_label.text = "Error: API endpoint not found (404)"
            elif response.status_code == 500:
                self.status_label.text = "Error: Server error (500)"
            else:
                self.status_label.text = f"Unexpected Error: {response.status_code}"
        
        except requests.exceptions.ConnectionError:
            self.status_label.text = "Connection Error: Server unreachable"
        except requests.exceptions.Timeout:
            self.status_label.text = "Error: Request Timed Out"
        except requests.exceptions.RequestException as e:
            self.status_label.text = f"Request Error: {str(e)}"

class RemoteControlApp(App):
    def build(self):
        return ControlApp()

if __name__ == "__main__":
    RemoteControlApp().run()
