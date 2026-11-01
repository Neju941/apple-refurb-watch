import os
import requests

url = "https://www.apple.com/jp/shop/refurbished/iphone"

html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
).text

if "iPhone 16e" in html:
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": "🎉 iPhone 16eを発見しました！\n\nhttps://www.apple.com/jp/shop/refurbished/iphone"
        }
    )

print("done")
