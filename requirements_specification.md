









6-os
### Jelenlegi üzleti folyamatok modellje

1. **Termékkezelés**
    - Az adminisztrátor manuálisan tölti fel a termékeket a webáruház adminisztrációs felületén.
    - A termékekhez nevet, leírást, árat, képet és műszaki adatokat ad meg.
    - A termékek kategorizálása jelenleg kézi folyamat, amely nem mindig egységes.
    - A készletadatokat egy egyszerű adatbázisban tároljuk, automatikus frissítés és AI-támogatás nélkül.

2. **Keresés és szűrés**
    - A vásárlók alapvető keresési funkciót használhatnak, amely csak kulcsszavakat ismer fel.
    - A szűrés ár, kategória és gyártó alapján történik, de a találatok nem mindig pontosak.
    - A keresés nem személyre szabott, így minden felhasználó ugyanazokat az eredményeket látja.

3. **Kosár és rendelés**
    - A vásárlók a kiválasztott termékeket manuálisan adhatják a kosárhoz.
    - A kosárban módosítható a mennyiség, illetve eltávolíthatók a tételek.
    - A rendszer kiszámítja az összesített árat, de nem ad ajánlást kapcsolódó termékekre.
    - A rendelési folyamat alapvető, az ügyféladatokat minden vásárlásnál külön meg kell adni.

4. **Felhasználók**
    - A felhasználók regisztráció és bejelentkezés után férnek hozzá a vásárlási funkciókhoz.
    - A rendszer nem tartalmaz AI-alapú segítséget vagy támogatást a vásárlási folyamat során.
    - A rendelési előzmények megtekintése lehetséges, de nincsenek automatikus ajánlások vagy értesítések.

5. **Adminisztráció**
    - Az admin manuálisan kezeli a rendeléseket és a terméklistát.
    - A készletfrissítés és a raktáradatok karbantartása kézi művelet, gyakran késéssel történik.
    - Riportok és kimutatások nem automatikusan készülnek, az adatok exportálása és elemzése időigényes.
    - Nincs közvetlen AI-támogatás az eladási trendek vagy a készletproblémák előrejelzésére.

Összességében a jelenlegi rendszer alapvető e-kereskedelmi funkciókat kínál, de hiányzik belőle az automatizálás, 
a mesterséges intelligencia támogatása és a személyre szabott vásárlói élmény. A folyamatok többsége manuális, 
ami időigényes és növeli a hibalehetőségeket.


7-es
### Igényelt üzleti folyamatok modellje

- **Termékfeltöltés az adminfelületen** –
A rendszernek lehetővé kell tennie új termékek gyors és strukturált feltöltését az adminisztrációs felületen keresztül,
sablonalapú űrlappal és AI-támogatott adatkitöltéssel.

- **Termékadatok kezelése (név, leírás, ár, kép, specifikációk)** – 
Az adminisztrátor egyszerűen adhat meg részletes termékinformációkat, amelyek alapján a vásárló pontos képet kap a termékről.

- **Kategorizálás, módosítás, törlés** –
A termékek kategóriákba rendezhetők, amelyek szükség esetén módosíthatók vagy törölhetők. Az AI képes javaslatot tenni a 
kategóriák finomítására.

- **Készletkezelés integráció** –
A webáruház automatikusan szinkronizálja a készletadatokat a raktárkészlettel, és figyelmeztet, ha egy termék elérhetősége 
alacsony.

- **AI-alapú keresés és szűrés** –
A felhasználók kulcsszavak vagy természetes nyelvű lekérdezések alapján kereshetnek. A rendszer szűrési lehetőségeket kínál ár, 
típus, márka és kategória szerint.

- **Kosár funkció (hozzáadás, eltávolítás, mennyiség módosítása)** – A felhasználó a kiválasztott termékeket egy 
kattintással a kosárba helyezheti, módosíthatja a mennyiséget vagy eltávolíthat tételeket. A rendszer automatikusan 
frissíti a végösszeget.

- **Megrendelés leadása és visszaigazolása** – 
A vásárló a kosár tartalmát megerősítve elindíthatja a rendelési folyamatot. Sikeres tranzakció esetén a 
rendszer automatikus visszaigazolást küld e-mailben, és a rendelés státusza nyomon követhető.

- **Regisztráció, bejelentkezés, rendeléskövetés** –
A felhasználók saját fiókot hozhatnak létre, ahol kezelhetik adataikat, megtekinthetik rendeléseiket és korábbi vásárlásaikat.

- **Termékek, rendelések és felhasználók kezelése** –
Az adminisztrátor kezelheti a terméklistát, felhasználói fiókokat és rendeléseket. Az AI figyelmezteti a hibás 
adatbevitelekre és javaslatot tesz hiányzó információk pótlására.

- **Készletfigyelés és raktárriasztás** – 
A rendszer valós időben követi a készletmozgásokat, és automatikus értesítéseket küld az adminisztrátornak a 
várható hiányokról vagy rendellenes eladási mintákról.

- **Bevétel–kiadás kimutatás** – 
A rendszer automatikusan generál napi, heti és havi pénzügyi jelentéseket,
 amelyek tartalmazzák az eladásokat, bevételeket és kiadásokat. Az AI elemzései segítik az üzleti döntéshozatalt.

Az igényelt üzleti folyamatok célja, hogy a rendszer hatékony, átlátható és részben automatizált módon 
támogassa az értékesítést, az adminisztrációt és a pénzügyi kimutatásokat, miközben csökkenti a manuális 
beavatkozás szükségességét.