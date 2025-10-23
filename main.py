import requests, os

CLOUDFLARE_TOKEN = "你的API Token"
ACCOUNT_ID = "你的Account ID"
TELEGRAM_TOKEN = "你的Bot Token"
CHAT_ID = "你的个人ID"

def get_usage():
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/workers/scripts"
    headers = {"Authorization": f"Bearer {CLOUDFLARE_TOKEN}"}
    r = requests.get(url, headers=headers).json()
    return len(r["result"])

def send_msg(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

usage = get_usage()
send_msg(f"☁️ Cloudflare Workers 当前使用 {usage} 次")
