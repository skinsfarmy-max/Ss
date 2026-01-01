import threading
from flask import Flask
from kivy.app import App
from kivy.uix.webview import WebView # Нужен спец-рецепт для p4a

# Твой Flask сервер
server = Flask(__name__)

@server.route('/')
def hello():
    return "<h1>Это Flask внутри APK!</h1>"

def run_server():
    server.run(host='127.0.0.1', port=5000)

# Запускаем Flask в отдельном потоке, чтобы он не вешал приложение
threading.Thread(target=run_server, daemon=True).start()

# Дальше должен идти код Kivy, который откроет браузер внутри себя...
