# AI-powered-Webshop Rendszerterv

1. Zsolti
### A rendszer célja

Az AI-powered Webshop célja, hogy modern,
könnyen kezelhető és megbízható online vásárlási felületet biztosítson a felhasználók számára.
A rendszer célja, hogy egyszerűvé tegye a termékek böngészését, összehasonlítását és megvásárlását,
miközben átlátható információkat nyújt a készletekről és az árakról.

A webshop központi eleme a felhasználóbarát felület,
amely lehetővé teszi, hogy a vásárlók gyorsan megtalálják a keresett termékeket,
szűrjenek kategória vagy ár alapján, és néhány kattintással rendelést adjanak le.
A kosárfunkció segítségével több termék is egyszerre kezelhető, így a vásárlási folyamat gyors és kényelmes.

A rendszer beépített AI-asszisztense segíti a felhasználókat a döntéshozatalban:
válaszol a kérdéseikre, ajánl releváns termékeket és támogatja a keresést természetes nyelvű kérdések alapján. 
z növeli a felhasználói élményt és csökkenti a keresési időt.

A cél egy stabil, biztonságos és rugalmas online platform megvalósítása,
amely hosszú távon is képes alkalmazkodni a változó igényekhez,
és hatékonyan támogatja a vásárlók mindennapi online vásárlási szokásait.

2. Zsolti
### Projektterv

A projektet négytagú fejlesztőcsapat valósítja meg, 
amelyben minden tag részt vesz a backend, frontend, tesztelési és dokumentációs feladatokban. 
A feladatmegosztás rugalmas, így a csapat gyorsan tud alkalmazkodni a fejlesztés során felmerülő igényekhez. 
A közös munka során kiemelt szerepet kap a tudásmegosztás, a folyamatos kommunikáció és az átlátható feladatkövetés.

**Fő feladatkörök:**
- **Backend fejlesztés:** Django alapú logika és adatbázis kapcsolat kialakítása.
- **Frontend fejlesztés:** Django Template használatával reszponzív webes felület megvalósítása.
- **Tesztelés:** egység- és funkcionális tesztek készítése, hibák javítása.
- **Dokumentáció:** követelmény-, rendszer- és teszttervek kidolgozása.

A fejlesztés iteratív megközelítéssel történik, 
kisebb modulokra bontva (pl. bejelentkezés, keresés, kosár, AI-asszisztens). 
Minden fejlesztési szakaszt rövid tesztelési és visszajelzési ciklus követ,
így a csapat gyorsan reagálhat az esetleges hibákra vagy változtatásokra.

| Modul / Funkció         | Feladat                              | Állapot        |
|-------------------------|--------------------------------------|----------------|
| Felhasználói azonosítás | Regisztráció, bejelentkezés          | Kész           |
| Termékkezelés           | Keresés, szűrés, megjelenítés        | Folyamatban    |
| Kosárkezelés            | Termékek hozzáadása, eltávolítása    | Folyamatban    |
| AI-asszisztens          | Termékajánlások, keresési javaslatok | Tervezés alatt |
| Tesztelés               | Egység- és integrációs tesztek       | Folyamatban    |

*Az eredeti becslések, aktuális értékek és eltelt idő órában értendők.*  

A táblázat a fejlesztés során folyamatosan frissül, 
így mindig naprakész képet ad a projekt állapotáról. 
Segíti a csapat kommunikációját és az időgazdálkodást, 
mivel egyértelműen látható, mely feladatok igényelnek azonnali figyelmet, 
és hol szükséges erőforrásokat átcsoportosítani.

3. Zoli
4. Geri
5. Geri


6. Zsolti
### Fizikai környezet

Az alkalmazás webes platformra készül, reszponzív kialakítással, így asztali számítógépeken és laptopokon is használható.
A rendszer nem igényel telepítést a felhasználó eszközére, mivel modern böngészőből érhető el (Chrome, Firefox, Edge, Safari).

A szerveroldali környezet a tervek szerint helyi (lokális) szerveren kerül kialakításra,
mivel ennek üzemeltetése jelentősen alacsonyabb költséggel jár,
így partnereink számára gazdaságosabb megoldást biztosít a rendszer hosszú távú fenntartására.

Biztonsági lépéseket teszünk az adatok megfelelő kezelése érdekében is, azáltal, hogy az adatbázishoz való hozzáférést csak
a megfelelő jogosultsággal rendelkezők számára ösztjuk meg. Az adatbázis szerver állandó üzemeltetésével és karbantartásával
próbáljuk elérni, hogy a felhasználók számára gördülékeny adathozzáférés jöjjön létre.

A rendszer teljes mértékben open source komponensekre épül, nem használ megvásárolt, zárt forráskódú szoftvert.

**Fejlesztésre használt eszközök:**

- Pycharm Professional - backend fejlesztése (Python Django keretrendszere)
- Visual Studio Code - fronted fejlesztése (HTML/CSS)
- Figma - felhasználói felület tervezése, képernyő tervezés
- Git és Github - verziókezelés és csapatmunka támogatása

7. Geri

8. Marci

9. Zoli

10. Zoli

11. Zsolti
### Tesztterv

A tesztelés célja annak biztosítása, hogy a rendszer minden komponense hibamentesen, a követelményeknek megfelelően működjön. A folyamat során ellenőrzésre kerül a funkcionalitás, a teljesítmény, a biztonság és a böngésző-kompatibilitás. Cél, hogy a rendszer stabil és megbízható legyen az éles használat során.

**1. Egységtesztelés (Unit Test)**
A fejlesztés során minden fontos funkcióhoz egységteszteket készítünk.  
Célja, hogy a backend logika, az adatbázis-kezelés és az űrlapfeldolgozás hibamentesen működjön.  
A kódlefedettség elvárt aránya 80% körüli.  
Tesztelendő fő modulok:
- Felhasználói autentikáció és jogosultságkezelés
- Termékek CRUD műveletei
- Kosár funkció (hozzáadás, törlés, árkalkuláció)
- Rendelés leadása és érvényesítése

**2. Alfa tesztelés**
A fejlesztői környezetben zajlik, a teljes rendszer működésének belső ellenőrzése.  
Fő cél: a hibák feltárása még az élesítés előtt.  
Tesztelt szempontok:
- Böngészők közötti kompatibilitás  
- Alapfunkciók (regisztráció, rendelés, kosár) helyes működése  
- Adatkezelés és hibaüzenetek megjelenítése  

**3. Béta tesztelés**
A rendszer valós felhasználói környezetben, tesztfelhasználók által kerül kipróbálásra.  
Célja az esetleges rejtett hibák feltárása és a felhasználói élmény vizsgálata.  
A visszajelzéseket a fejlesztői csapat kiértékeli, és szükség esetén módosításokat hajt végre.


### Tesztelendő funkciók

**Backend funkciók**
- **Adatbázis-kezelés:**  
  Az adatok rögzítése, módosítása és törlése hibamentesen működjön.  
- **Készletkezelés:**  
  A készletváltozások pontosan jelenjenek meg a vásárlások és visszavonások után.  
- **Felhasználókezelés:**  
  A regisztráció, bejelentkezés és jogosultságkezelés biztonságosan működjön.  
- **Rendeléskezelés:**  
  A rendelések helyesen rögzüljenek, a státuszok megfelelően frissüljenek.  

**Frontend funkciók**
- **Bejelentkezés:**  
  - Helyes adatok esetén a felhasználó sikeresen belép.  
  - Hibás adatoknál megfelelő hibaüzenet jelenik meg.  
- **Keresés és szűrés:**  
  - Termékek keresése név vagy kategória alapján.  
  - Szűrés ár, elérhetőség és márka szerint.  
- **Kosárkezelés:**  
  - Termékek hozzáadása és eltávolítása működjön hibamentesen.  
  - Kosárérték automatikusan frissüljön.  
  - Kosár tartalma maradjon meg kijelentkezés után is.  
- **Reszponzivitás:**  
  A weboldal helyesen jelenjen meg minden modern böngészőben és kijelzőméreten.  
- **AI-asszisztens:**  
  A felhasználói kérdésekre pontos és releváns válaszokat adjon.

12. Marci