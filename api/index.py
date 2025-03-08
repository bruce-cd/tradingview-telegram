from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/api', methods=['POST'])
def handle_webhook():
    try:
        data = request.json
        message = data.get('message', '默认提醒：买入信号触发！')
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        response = requests.post(telegram_url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})
        return "OK", 200
    except Exception as e:
        return f"错误: {str(e)}", 500

@app.route('/', methods=['GET'])
def test():
    return "✅ 服务运行正常！", 200
