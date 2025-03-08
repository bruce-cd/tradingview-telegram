@app.route('/api', methods=['POST'])
def handle_webhook():
    try:
        data = request.json
        message = data.get('message', '默认提醒：买入信号触发！')
        
        # 检查环境变量是否加载
        if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
            return "错误：Telegram Token 或 Chat ID 未设置！", 500
        
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        response = requests.post(
            telegram_url,
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message}
        )
        
        # 检查 Telegram API 响应
        if response.status_code != 200:
            return f"Telegram API 错误: {response.text}", 500
            
        return "OK", 200
    except Exception as e:
        print(f"服务器内部错误: {str(e)}")  # 此日志可在 Vercel Logs 中查看
        return f"服务器内部错误: {str(e)}", 500
