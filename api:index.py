from flask import Flask, request
import requests

app = Flask(__name__)

# 填写你的 Telegram 机器人的 Token 和 Chat ID
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"  # 替换成你的 Token
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"       # 替换成你的 Chat ID

@app.route('/api', methods=['POST'])
def handle_webhook():
    try:
        # 从 TradingView 接收警报数据
        data = request.json
        message = data.get('message', '默认提醒：买入信号触发！')
        
        # 发送到 Telegram
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            }
        )
        
        # 检查是否发送成功
        if response.status_code == 200:
            return "OK", 200
        else:
            return f"Telegram 发送失败: {response.text}", 500
            
    except Exception as e:
        return f"服务器错误: {str(e)}", 500

if __name__ == '__main__':
    app.run()
