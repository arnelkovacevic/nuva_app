📊 XLS Reader Web Aplikacija

XLS Reader je jednostavna web aplikacija napravljena pomoću Streamlit frameworka koja omogućava:

📥 Učitavanje Excel fajlova (.xls, .xlsx)
👀 Pregled podataka u tabelarnom prikazu
📤 Preuzimanje obrađenih podataka nazad u Excel formatu
🔗 Online verzija aplikacije: https://xls-reader.onrender.com

🚀 Glavne funkcionalnosti

✅ Učitavanje Excel fajlova direktno iz tvog računara
✅ Prikaz podataka u interaktivnoj tabeli
✅ Mogućnost preuzimanja podataka u Excel formatu
✅ Podržani formati: .xls i .xlsx
🧰 Potrebni alati i biblioteke

Da bi pokrenuo aplikaciju lokalno, potrebno je:

Instaliran Python 3.7 ili noviji
Instalirane sljedeće biblioteke:
pip install streamlit pandas openpyxl xlsxwriter
🛠️ Kako pokrenuti aplikaciju lokalno

Napravi fajl app.py i zalijepi kod aplikacije (ili kloniraj projekt ako koristiš GitHub)
U komandnoj liniji pokreni aplikaciju sa:
streamlit run app.py
Otvori web preglednik i idi na http://localhost:8501
📂 Kako koristiti aplikaciju

Klikni na "Browse files" i odaberi Excel fajl sa svog računara (.xls ili .xlsx)
Nakon učitavanja, tabela s podacima će se prikazati ispod
Ako postoji opcija za preuzimanje, klikni "Download" da bi preuzeo novi Excel fajl
⚠️ Napomene

Aplikacija trenutno podržava samo Excel fajlove (ne CSV ili druge formate)
Fajlovi ne smiju biti zaštićeni lozinkom
Ako želiš zadržati naprednu formatizaciju (boje, ćelije, fontovi), moguće je proširiti aplikaciju uz pomoć biblioteka poput openpyxl ili xlsxwriter
📧 Kontakt

Ako imaš pitanja, prijedloge ili želiš dodati nove funkcionalnosti — slobodno se javi!
Možeš me kontaktirati direktno ili predložiti izmjene ako koristiš verziju na GitHubu.
