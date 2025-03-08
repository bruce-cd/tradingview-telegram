@app.route('/api', methods=['POST'])
def handle_webhook():
    try:
        data = request.json
        message = data.get('message', '默认提醒')
        
        # 调试日志：输出环境变量状态
        print(f"[DEBUG] TELEGRAM_TOKEN exists: {bool(TELEGRAM_TOKEN)}")
        print(f"[DEBUG] TELEGRAM_CHAT_ID exists: {bool(TELEGRAM_CHAT_ID)}")
        
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        response = requests.post(
            telegram_url,
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message}
        )
        
        # 调试日志：输出 Telegram API 响应
        print(f"[DEBUG] Telegram API 响应状态码: {response.status_code}")
        print(f"[DEBUG] Telegram API 响应内容: {response.text}")
        
        response.raise_for_status()  # 主动触发异常（如果状态码非 200）
        return "OK", 200
    except Exception as e:
        print(f"[ERROR] 服务器崩溃: {str(e)}")
        return f"错误: {str(e)}", 500
