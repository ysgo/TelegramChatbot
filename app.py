from decouple import config
from flask import Flask, request

token = config('TELEGRAM_TOKEN')
app = Flask(__name__)

@app.route('/')
def index():
    return 'chatbot!'

@app.route(f'/{token}', methods=['POST'])
def telegram():
    print(request.get_json())
    return '', 200

# python app.py로 서버 실행, Debug 모드로
if __name__ == '__main__':
    app.run(debug=True)