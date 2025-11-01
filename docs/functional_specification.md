### Áttekintés

A **AI powered webshop** rendszer célja, hogy a vásárlók számára egy modern,
gyors és személyre szabott online értékesítési felületet biztosítson.
Az alkalmazás kulcseleme az AI-asszisztens, amely természetes nyelven segíti a felhasználókat.

A rendszer funkcionális felépítése az online értékesítési folyamat AI-alapú támogatására épül.
Az alkalmazás egyik fő modulja a bejelentkezés és jogosultságkezelés,
mivel a vásárlók és adminisztrátorok csak azonosítás után férhetnek hozzá személyre szabott funkcióikhoz.
A jogosultsági szintek határozzák meg, hogy ki milyen funkciókat érhet el (pl. adminisztrátor, vásárló).

A vásárló az AI által támogatott intelligens terméklista segítségével böngészhet a rendelkezésre álló termékek között,
amelyekhez a rendszer valós idejű készletinformációkat jelenít meg. 
Az AI figyelmeztet alacsony készletszint esetén, és javaslatot tesz alternatív termékekre vagy előrendelésre.

A felhasználók intelligens keresőmező és AI-alapú szűrés segítségével természetes nyelven is megtalálhatják a kívánt termékeket
(pl. „Mutass olcsó 5G-s telefonokat” vagy „Szeretnék egy jó kamerás modellt”).

A kiválasztott termékek kosárba helyezhetők, amelyet az AI dinamikusan kezel és
javaslatokat ad kiegészítő termékekre, csomagajánlatokra vagy akciókra.
A vásárló döntését követően az AI-asszisztens segíti a rendelés véglegesítését,
a fizetési folyamatot és a számlaadatok kitöltését.



### Jelenlegi helyzet

A digitális értékesítés rohamos fejlődése miatt a vásárlók ma már elvárják,
hogy az online vásárlási élmény gyors, intuitív és személyre szabott legyen.
A jelenleg használt webáruház-rendszerek azonban sok esetben nem képesek megfelelni ezeknek az igényeknek:
a felületek bonyolultak, az ajánlások nem relevánsak, és a keresés gyakran pontatlan.

A jelenlegi rendszer nem tartalmaz mesterséges intelligenciát,
ezért nem tudja értelmezni a felhasználók természetes nyelvű kéréseit
(pl. „Mutass nekem olcsó, jó kamerás telefont”), és nem képes személyre szabott termékajánlásokat nyújtani.
A hagyományos keresés és szűrés korlátozott, így a vásárlók nehezebben találják meg, amit keresnek,
ami csökkenti az értékesítési arányt és a felhasználói elégedettséget.

3-as
### Követelmény lista

| Modul            | Név                      | Kifejtés                                                                                                                            |
|------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Jogosultság      | Bejelentkezés            | A felhasználó (vásárló vagy admin) email-cím és jelszó segítségével léphet be; hibás adatok esetén az AI-asszisztens figyelmezteti. |
| Jogosultság      | Regisztráció             | Új vásárlók regisztrációja biztonságos (kódolt) jelszótárolással, email-validációval és AI-alapú űrlapsegítséggel.                  |
| Jogosultság      | Jogosultsági szintek     | Többszintű hozzáférés (admin, vásárló); az admin kezelhet, a vásárló böngészhet, vásárolhat és követhet rendeléseket.               |
| Vásárlói felület | Terméklista              | Az AI valós időben frissített terméklistát jelenít meg, személyre szabott sorrendben a felhasználói szokások alapján.               |
| Vásárlói felület | AI-asszisztens           | Az AI természetes nyelvű interakciót biztosít, ajánlásokat tesz, kérdésekre válaszol és segít a vásárlási folyamatban.              |
| Vásárlói felület | Keresés                  | Az AI értelmezi a természetes nyelvű lekérdezéseket (pl. „Mutass olcsó 5G-s telefonokat”) és releváns találatokat ad.               |
| Vásárlói felület | Szűrés                   | AI-támogatott szűrés kategória, ár, gyártó, teljesítmény vagy felhasználói értékelések alapján.                                     |
| Vásárlói felület | Termékajánlás            | Az AI a vásárlói előzmények és trendek alapján javaslatokat tesz kiegészítő vagy hasonló termékekre.                                |
| Vásárlói felület | Kosár funkció            | A vásárló kosárba helyezheti a termékeket, az AI ajánlhat hozzájuk kiegészítőket vagy kedvezményeket.                               |
| Vásárlói felület | Vásárlás támogatása      | Az AI végigkíséri a vásárlást, segít a fizetési mód kiválasztásában és a számlaadatok kitöltésében.                                 |
| Vásárlói felület | Rendeléskövetés          | A vásárló nyomon követheti rendelését az AI segítségével (pl. „Mikor érkezik meg a rendelésem?”).                                   |
| Vásárlói felület | Számlák kezelése         | Automatikus számlagenerálás PDF formátumban; AI-asszisztens segíti a reklamáció vagy sztornó folyamatát.                            |
| Riport           | Napi riport              | Az AI automatikusan összesíti a napi eladásokat és vásárlói aktivitást, admin számára egy kattintással elérhető.                    |
| Riport           | Heti/Havi riport         | Az AI automatikusan generál riportokat a forgalomról és vásárlói szokásokról, Excel vagy grafikus formában.                         |
| Riport           | Riport tartalom          | A riportok tartalmazzák az eladások, bevételek, készletmozgások és AI-interakciók statisztikáit.                                    |
| Adminisztráció   | Termékfeltöltés          | Az admin új termékeket tölthet fel, kategóriákat hozhat létre, képeket és specifikációkat adhat hozzá.                              |
| Adminisztráció   | Készletkezelés           | Az admin manuálisan vagy automatizáltan frissítheti a készletet, AI-értesítést kap alacsony szint esetén.                           |
| Adminisztráció   | Felhasználókezelés       | Az admin vásárlói fiókokat kezelhet, jogosultságokat módosíthat, aktivitást figyelhet.                                              |
| Adminisztráció   | Riportkészítés           | Az admin megtekintheti az AI által generált eladási, forgalmi és interakciós riportokat.                                            |
| Rendszer         | Stabil működés           | A rendszer reszponzív, skálázható és nagy forgalom mellett is gyors, felhőalapú architektúrával.                                    |
| Rendszer         | Biztonság                | Titkosított adatátvitel (SSL), biztonságos hitelesítés és GDPR-kompatibilis adatkezelés.                                            |
| Rendszer         | AI-etikai megfelelés     | Az AI működésének átláthatónak kell lennie, nem gyűjthet indokolatlan adatokat, és feleljen meg az EU AI-rendeletnek.               |
| Rendszer         | Szabványoknak megfelelés | A rendszer igazodjon az ISO/IEC 27001, ISO/IEC 25010 és ISO/IEC 42001 (AI-irányítás) szabványokhoz.                                 |

4-es
### Jelenlegi üzleti folyamatok modellje

1. Termékkezelés

- Az adminisztrátor a webáruház adminfelületén keresztül tölti fel a termékeket.
- Minden termékhez megadható a név, leírás, ár, kép, kategória és műszaki specifikáció.
- Az AI elemzi a termékadatokat, és javaslatot tehet kategorizálásra vagy leírás-optimalizálásra.
- A készlet valós időben frissül a rendelésekkel összhangban, az admin számára riasztás jelenik meg alacsony készletszint esetén.

2. Keresés és szűrés

- A vásárlók AI-asszisztens segítségével természetes nyelven is kereshetnek (pl. „Mutass olcsó 5G-s telefonokat 200 000 Ft alatt”).
- Az AI relevancia alapján rangsorolja a találatokat, és figyelembe veszi a felhasználó előzményeit és preferenciáit.
- A termékek továbbra is szűrhetők ár, gyártó, teljesítmény, kategória és értékelés alapján.

3. Kosár és rendelés

- A vásárló termékeket helyezhet a kosárba, a rendszer automatikusan kiszámítja az aktuális végösszeget.
- Az AI javaslatot tesz kapcsolódó termékekre („Szeretnéd ezt a tokot is hozzáadni?”).
- A rendelés leadása során az AI segít a fizetési mód kiválasztásában, és ellenőrzi az adatok helyességét.
- A rendszer automatikusan számlát generál és elküldi a vásárlónak e-mailben.

4. Felhasználók

- A vásárlók önállóan regisztrálhatnak és bejelentkezhetnek.
- A profiloldalukon megtekinthetik korábbi rendeléseiket, számláikat, és követhetik az aktuális szállítási állapotot.
- Az AI-asszisztens elérhető számukra bármikor – segíthet panasz, visszaküldés vagy termékinformáció esetén.

5. AI-folyamatok

- Az AI valós időben elemzi a vásárlói viselkedést, és személyre szabott ajánlásokat készít.
- Automatikus riportokat generál az adminisztráció számára az eladási trendekről és a felhasználói aktivitásról.
- Az AI ügyféltámogatási chatbotként is működik, megválaszolja a leggyakoribb kérdéseket, és továbbítja a problémákat az admin felé.

6. Adminisztráció

- Az adminisztrátor kezeli a terméklistát, a kategóriákat és a vásárlói fiókokat.
- Riportokat érhet el a bevételről, rendelések számáról és AI-interakciókról.
- Az AI értesíti az admint, ha a készlet alacsony, egy termék népszerűvé válik, vagy a felhasználók gyakori hibát tapasztalnak.
- A pénzügyi kimutatások és forgalmi riportok automatikusan, időzítetten készülnek.


5-os
### Igényelt üzleti folyamatok modellje

- **AI-támogatott termékfeltöltés** –
A rendszer lehetővé teszi új termékek gyors és strukturált feltöltését az adminfelületen. Az AI automatikusan javaslatot tesz 
kategóriákra, címkékre és kulcsszavakra a termékadatok alapján.

- **Termékadatok begyűjtése és elemzése (név, leírás, ár, kép, specifikációk)** –
A feltöltött információkat az AI értékeli, és segít optimalizálni a leírásokat a keresőoptimalizálás (SEO) 
és vásárlói megértés javítása érdekében.

- **Kategorizálás, módosítás, törlés** –
A termékek automatikusan kategorizálódnak az AI által, de az admin manuálisan is módosíthatja ezeket. Az AI javaslatot tehet új 
kategóriák vagy címkék létrehozására a felhasználói keresési minták alapján.

- **Intelligens készletkezelés integráció** –
A rendszer valós időben kapcsolódik a raktárkészlethez. Az AI előrejelzést készít a várható készlethiányokról, 
és javaslatot tesz utánrendelésre.

- **Természetes nyelvű keresés és AI-szűrés** –
A felhasználók természetes nyelven kereshetnek („Ajánlj nekem egy olcsó, de jó kamerás telefont”). Az AI személyre szabott 
találatokat jelenít meg az előzmények és preferenciák alapján.

- **Termékajánlás és kiegészítő javaslatok** –
Az AI vásárlási szokások és korábbi rendelések alapján személyre szabott ajánlásokat jelenít meg. Kosárhoz adáskor releváns 
kiegészítőket ajánl (pl. tok, kijelzővédő).

- **Kosárkezelés és dinamikus vásárlási folyamat** –
A vásárló termékeket adhat a kosárhoz vagy távolíthat el onnan, miközben az AI valós időben javaslatokat ad akciókra vagy 
olcsóbb alternatívákra.

- **Vásárlási folyamat támogatása AI-asszisztenssel** –
A vásárló a kosár tartalmát jóváhagyva indíthatja a fizetést, miközben az AI-asszisztens segít a szállítási és fizetési 
opciók kiválasztásában. Hibás adatok esetén az AI azonnali visszajelzést ad és javítási javaslatokat kínál.

- **Rendeléskövetés és visszajelzés** –
A sikeres tranzakció után a vásárló valós időben követheti rendelését, státuszváltozásról automatikus AI-értesítést kap.
Az AI képes megválaszolni kérdéseket, pl. „Mikor érkezik meg a rendelésem?”

- **Regisztráció, bejelentkezés és személyre szabás** –
A vásárlók saját profilt hozhatnak létre, ahol megtekinthetik rendeléseiket, kedvenceiket és ajánlásaikat. Az AI tanul a 
felhasználó viselkedéséből, hogy egyre pontosabb termékjavaslatokat adhasson.

- **Termékek, rendelések, vásárlók kezelése (Adminisztráció)** –
Az admin a felületen keresztül kezelheti a terméklistát, vásárlói fiókokat és rendeléseket. Az AI statisztikákat generál 
az eladási trendekről és figyelmeztet a rendellenes aktivitásra.

- **Készletfigyelés és előrejelzés** –
Az AI elemzi az értékesítési adatokat, és előrejelzést készít a készletmozgásokról. Hiány esetén automatikus riasztást 
küld az adminnak, és javaslatot tesz utánpótlási mennyiségre.

- **Bevétel-kiadás kimutatás és AI-riportálás** –
A rendszer automatikus pénzügyi kimutatásokat készít, vizualizált riportokkal. Az AI képes kiemelni a forgalmi trendeket, 
vásárlói szokásokat és kiugró adatokat (pl. legjobban teljesítő termék).

- **AI-ügyféltámogatás és visszaküldés kezelése** –
A vásárlók az AI-asszisztensen keresztül kezdeményezhetnek visszaküldést, panaszt vagy kérhetnek segítséget. Az AI automatikusan 
dokumentálja az esetet, és szükség esetén továbbítja az adminhoz.

### Használati esetek

1. Adminisztrátor

Az Adminisztrátor felelős a rendszer zavartalan működéséért, az adatok pontosságáért és a vásárlói élmény felügyeletéért.
Jogosultsága a teljes rendszerre kiterjed, beleértve az AI-funkciókat és a riportkészítést.

- Feladatai:
  - Bejelentkezés
  - Az adminisztrátor email-cím és jelszó megadásával lép be a rendszerbe.
  - Kétlépcsős hitelesítés és AI-alapú gyanús bejelentkezés-észlelés védi a fiókot.
  - Felhasználókezelés
  - Hozzáférés a vásárlói és admin fiókok listájához.
  - Felhasználók adatainak módosítása (név, email, státusz, jogosultság).
  - Fiókok zárolása, törlése vagy jogosultság-módosítása.
  - Termékkezelés és készletfelügyelet
  - Új termékek feltöltése, kategóriák létrehozása, módosítása, törlése.
  - Az AI-asszisztens javaslatokat tesz kategorizálásra, árazásra és készletbővítésre.
  - Riasztás alacsony készlet esetén, előrejelzés a fogyó termékekről.
  - Riportálás és statisztika
  - Az admin megtekintheti az AI által automatikusan generált napi, heti és havi riportokat.
  - A riportok tartalmazzák az eladásokat, vásárlói viselkedést és AI-interakciókat.
  - Az AI képes kiemelni trendeket és anomáliákat (pl. forgalomcsökkenés, népszerű termékek).
  - Globális rendszerfelügyelet
  - A rendszerbeállítások, jogosultságok és biztonsági modulok kezelése.
  - AI-logok és adatvédelmi beállítások ellenőrzése a GDPR-nak megfelelően.
  - Az AI működésének felügyelete és finomhangolása (pl. ajánlórendszer, chatbot-tanítás).

2. Vásárló

A Vásárló a rendszer elsődleges felhasználója, aki böngészi, keresheti és megvásárolhatja a termékeket.
Az AI-asszisztens személyre szabott élményt és támogatást biztosít számára minden lépésben.

- Lehetőségei:
  - Regisztráció és bejelentkezés
  - Saját fiók létrehozása email és jelszó segítségével.
  - Az AI segít az adatok ellenőrzésében és jelszó-erősség kiértékelésében.
  - Termékböngészés és keresés
  - Termékek megtekintése AI-alapú ajánlások és kategóriák szerint.
  - Természetes nyelvű keresés: pl. „Mutass nekem egy jó kamerás, de olcsó telefont.”
  - Az AI figyelembe veszi a vásárlási előzményeket, hogy releváns találatokat adjon.
  - Kosár és vásárlási folyamat
  - Termékek hozzáadása vagy eltávolítása a kosárból.
  - Az AI ajánl kiegészítőket („Ehhez a telefonhoz illik ez a tok és töltő”).
  - Vásárlási folyamat indítása, fizetési mód és szállítás kiválasztása az AI útmutatásával.
  - Rendeléskövetés és ügyféltámogatás
  - Saját profilban megtekintheti rendelései állapotát.
  - Az AI válaszol a státuszra vonatkozó kérdésekre („Mikor érkezik meg a csomagom?”).
  - A vásárló visszaküldést vagy reklamációt is indíthat az AI segítségével.
  - Személyre szabás és ajánlások
  - Az AI tanul a vásárlási szokásokból, és egyre pontosabb termékajánlásokat tesz.
  - A vásárló kedvenc termékeket menthet és akcióértesítéseket kaphat.

3. AI-asszisztens

Az AI-asszisztens az alkalmazás intelligens központi eleme, amely a vásárlók és az adminisztrátorok munkáját egyaránt támogatja.

- Feladatai:
  - Természetes nyelvű kommunikáció a vásárlókkal (chat vagy hangalapú formában).
  - Termékkeresés, ajánlás és vásárlási folyamat támogatása.
  - Ügyféltámogatás: panaszkezelés, rendeléskövetés, visszaküldés indítása.
  - Admin számára riport- és trendgenerálás.
  - Készletfigyelés és előrejelzés a forgalmi adatok alapján.
  - AI-tanulás: a rendszer folyamatosan fejleszti magát a felhasználói interakciók alapján.

### Képernyő terv

![Image of the front-page](./doc_img/img_of_homepage.png)
*A webalkalmazás főoldalának tervezete*

### Forgatókönyv

- Cél:  
  A vásárló az AI-asszisztens segítségével sikeresen kiválaszt és megvásárol egy terméket, majd nyomon követi rendelését.  
  Az adminisztrátor a háttérben automatikus AI-riportot kap az eladásról.

- Szereplők:
    - Vásárló
    - AI-asszisztens
    - Rendszer
    - Adminisztrátor

- Lépések:
    1. A vásárló megnyitja a webáruházat, ahol az AI-asszisztens köszönti („Üdv! Segíthetek megtalálni az ideális telefont?”).
    2. A vásárló természetes nyelven beírja: „Olyan telefont keresek, ami jó kamerás és 250 000 Ft alatt van.”
    3. Az AI feldolgozza a kérdést, és listázza a releváns termékeket, rövid ajánlásokkal.
    4. A vásárló rákattint az egyik ajánlott termékre, ahol részletes specifikációkat és vásárlói értékeléseket lát.
    5. Az AI felajánl kiegészítő termékeket (pl. tok, kijelzővédő).
    6. A vásárló a kívánt terméket a kosárba helyezi, majd az AI megerősíti a műveletet és megjeleníti a végösszeget.
    7. A vásárló elindítja a vásárlási folyamatot, az AI-asszisztens segít a fizetési és szállítási adatok kitöltésében.
    8. A rendszer biztonságosan feldolgozza a fizetést, majd automatikusan digitális számlát generál és elküldi a vásárlónak e-mailben.
    9. A vásárló később megkérdezi: „Mikor érkezik meg a rendelésem?”, az AI pedig lekéri a rendelés állapotát és tájékoztatja.
    10. Az adminisztrátor a nap végén megtekinti az AI által automatikusan generált riportot, amely tartalmazza az eladásokat, forgalmat és felhasználói aktivitást.  


### Funkció – követelmény megfeleltetés

| Funkció                    | Modul            | Kapcsolódó követelmény(ek)                                                                                                        |
|----------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Bejelentkezés              | Jogosultság      | A rendszernek biztosítania kell, hogy csak regisztrált vásárlók és adminisztrátorok férjenek hozzá a funkciókhoz.                 |
| Regisztráció               | Jogosultság      | A felhasználók biztonságos módon hozhatnak létre fiókot; az AI segít az űrlapkitöltésben és adatellenőrzésben.                    |
| AI-asszisztens             | AI modul         | Az AI természetes nyelvű interakciót biztosít, ajánlásokat ad, és támogatja a vásárlási folyamatot.                               |
| Terméklista                | Vásárlói felület | A rendszernek meg kell jelenítenie az elérhető termékeket, az AI-nak pedig személyre szabott sorrendben kell azokat ajánlania.    |
| Természetes nyelvű keresés | Vásárlói felület | Az AI-nak értelmeznie kell a felhasználói kéréseket (pl. „Mutass olcsó 5G-s telefont”) és releváns találatokat kell biztosítania. |
| Szűrés                     | Vásárlói felület | A rendszernek lehetőséget kell adnia AI-támogatott szűrésre kategória, ár, gyártó és értékelés alapján.                           |
| Termékajánlás              | AI modul         | Az AI vásárlói előzmények és viselkedés alapján releváns termékeket ajánl.                                                        |
| Kosár funkció              | Vásárlói felület | A vásárlónak lehetőséget kell biztosítani termékek kosárba helyezésére, módosítására és végösszeg megtekintésére.                 |
| Vásárlás támogatása        | Vásárlói felület | Az AI-asszisztens segíti a vásárlót a fizetési és szállítási folyamat során, ellenőrzi az adatok helyességét.                     |
| Rendeléskövetés            | Vásárlói felület | A vásárló valós időben követheti rendeléseit, az AI válaszol a státuszra vonatkozó kérdésekre.                                    |
| Számlák kezelése           | Vásárlói felület | A rendszer automatikusan számlát generál a vásárlásról; az AI-asszisztens segíthet a sztornózás vagy visszaküldés folyamatában.   |
| Készletfigyelés            | Adminisztráció   | Az admin valós időben figyelheti a készletmozgásokat; az AI előrejelzi a fogyó termékeket és javaslatot tesz utánrendelésre.      |
| Felhasználókezelés         | Adminisztráció   | Az admin kezelheti a vásárlói fiókokat, jogosultságokat, aktivitást; az AI automatikusan jelent a gyanús tevékenységekről.        |
| Riportkészítés             | Adminisztráció   | Az AI automatikusan generál riportokat az eladásokról, trendekről és felhasználói viselkedésről.                                  |
| Stabil működés             | Rendszer         | A rendszernek reszponzívnak, skálázhatónak és hibamentesnek kell maradnia magas terhelés esetén is.                               |
| Biztonság és adatvédelem   | Rendszer         | Az adatkezelésnek GDPR-kompatibilisnek kell lennie, titkosított adattárolással és AI-adatnaplózással.                             |
| AI-etikai megfelelés       | Rendszer         | Az AI működésének átláthatónak, adatvédelminek és az EU AI Act előírásainak megfelelőnek kell lennie.                             |

| Fogalomtár                 |                                                                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Vásárló                    | A rendszer felhasználója, aki termékeket keres, kosárba helyez és megvásárol, valamint követi rendeléseit az AI-asszisztens segítségével.   |
| Adminisztrátor             | Jogosult felhasználó, aki kezeli a termékeket, vásárlói fiókokat, riportokat, és felügyeli a rendszer és az AI működését.                   |
| AI-asszisztens             | Intelligens segéd, aki természetes nyelven kommunikál a vásárlóval, termékeket ajánl, kérdésekre válaszol és segít a vásárlási folyamatban. |
| Termékajánlás              | Az AI által generált javaslat hasonló vagy kiegészítő termékekre, a vásárló preferenciái és előzményei alapján.                             |
| Rendeléskövetés            | A vásárló lehetősége, hogy valós időben megtekintse rendelése státuszát, az AI-asszisztens pedig információt nyújt erről.                   |
| Sztornózás                 | Már kiállított számla érvénytelenítése vagy rendelés visszavonása, amelyet az AI-asszisztens is támogat.                                    |
| Riport                     | Az AI által automatikusan generált összesítő dokumentum az eladások, bevételek, vásárlói aktivitás és készletmozgások adataival.            |
| Szűrés                     | AI-támogatott funkció, amely lehetővé teszi a termékek szűrését ár, típus, gyártó vagy más tulajdonság alapján.                             |
| Keresési mező              | Olyan intelligens keresőfelület, amely természetes nyelvű lekérdezéseket is képes értelmezni és releváns találatokat adni.                  |
| Kosár                      | A vásárló által kezelt gyűjtőfunkció, amely tartalmazza a kiválasztott termékeket, azok árát és a javasolt kiegészítő ajánlatokat is.       |
| AI-riportálás              | Az AI által készített automatikus jelentés az eladási trendekről, forgalomról és felhasználói interakciókról az adminisztrátor számára.     |
| Készletfigyelés            | Az AI által támogatott funkció, amely figyeli a termékkészletet, előrejelzi a hiányt, és javaslatot tesz utánrendelésre.                    |
| Természetes nyelvű keresés | Keresési funkció, amely lehetővé teszi, hogy a vásárló hétköznapi nyelven tegye fel kérdéseit (pl. „Mutass nekem olcsó, 5G-s telefonokat”). |
