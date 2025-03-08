from flask import Flask, request
import requests
import os

# 初始化 Flask 应用实例
app = Flask(__name__)

# 从环境变量读取配置
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route('/api', methods=['POST'])
def handle_webhook():
    try:
        data = request.json
        message = data.get('message', '默认提醒：买入信号触发！')
        
        # 检查环境变量
        if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
            return "错误：Telegram Token 或 Chat ID 未设置！", 500
        
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        response = requests.post(
            telegram_url,
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message},
            timeout=10
        )
        response.raise_for_status()
        return "OK", 200
    except Exception as e:
        return f"服务器错误: {str(e)}", 500

@app.route('/', methods=['GET'])
def test():
    return "✅ 服务运行正常！", 200
