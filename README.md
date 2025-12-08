# 🤖 AI-powered Webshop – Django Web Application

Ez a projekt egy **Django keretrendszerre épülő webalkalmazás**, amely egy webshop alapfunkcióit valósítja meg,  
és **AI-alapú továbbfejlesztési lehetőségekre** van felkészítve.  
A rendszer célja egy jól strukturált, bővíthető backend kialakítása modern webes és mesterséges intelligencia megoldásokhoz.

---

## 📌 Fő funkciók

- Felhasználói regisztráció és autentikáció  
- Termékek és specifikációk adatbázis-alapú kezelése  
- Kosár- és rendelési logika  
- Django admin felület használata  
- Strukturált backend logika Django modellekre építve  

---

## 🧠 AI-orientált megközelítés

A projekt architektúrája fel van készítve mesterséges intelligencia alapú funkciók integrálására:

- Intelligens termékajánló rendszer alapjai  
- Automatizált termékadat-feldolgozás lehetősége  
- AI-alapú elemzések beillesztése a backendbe  
- Skálázható adatmodell AI tanulási célokra  

---

## 🏗️ Alkalmazott architektúra

- Django **MVT (Model–View–Template)** minta  
- Elkülönített alkalmazás (`application` modul)  
- Központi konfiguráció (`settings`, `urls`)  
- Relációs adatbázis-kezelés (pl. PostgreSQL)  
- Környezeti változók támogatása (`.env`)  

---

## ⚙️ Technológiai stack

- **Backend:** Python, Django  
- **Adatbázis:** SQLite / PostgreSQL  
- **Frontend:** Django Templates, HTML, CSS  
- **Egyéb:** Django Admin, ORM  

---

## 🚀 Telepítés és futtatás

```bash
# Virtuális környezet létrehozása
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Függőségek telepítése
pip install -r requirements.txt

# Migrációk futtatása
python manage.py migrate

# Szerver indítása
python manage.py runserver
