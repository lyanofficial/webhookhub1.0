import time
print("att 6s pour ce connecter")
time.sleep(6)
print("connect success!")
time.sleep(3)
print("met ton webhook")
import requests

webhook_url = input()

payload = {
    "content": f"rejoin le server https://discord.gg/Yg2r7ceJbW pour etre vérifié"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, json=payload, headers=headers)

print(response.status_code)

