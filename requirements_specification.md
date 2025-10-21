







### Vágyálom rendszer

A projekt célja, hogy egy megbízható, könnyen kezelhető és átlátható webáruház jöjjön létre,
amely a mesterséges intelligencia segítségével segíti a vásárlókat és az adminisztrátorokat a mindennapi működésben.
A rendszernek egyszerűen használhatónak kell lennie, hogy a vásárlási folyamat gyorsan és problémamentesen végbemenjen.

A vásárlók számára a legfontosabb, hogy könnyen megtalálják a keresett termékeket.
Ezt az **AI-asszisztens** támogatja, aki természetes nyelven is képes értelmezni a kérdéseket,
és segít a termékek közötti eligazodásban. A felületnek biztosítania kell a szűrési és keresési lehetőségeket mint például ár,
típus vagy márka alapján —, hogy a felhasználó rövid idő alatt megtalálhassa, amit keres.

A rendszernek valós idejű információt kell nyújtania a termékekről, a készletekről és a rendelési folyamat állapotáról.
Az AI képes jelezni az alacsony készletszintet, így az adminisztrátor időben intézkedhet a feltöltésről.
A készletbővítésnek és termékkezelésnek egyszerűen, néhány kattintással kell történnie.

Az adminisztrátor feladata a rendszer felügyelete, az új termékek feltöltése, valamint a felhasználók és rendelési adatok kezelése.
A felületnek áttekinthető módon kell megjelenítenie az eladásokat, bevételeket és forgalmi adatokat,
hogy az admin könnyen értékelhesse a teljesítményt.

A cél egy olyan rendszer kialakítása, amely nem túl bonyolult, de kellően okos ahhoz,
hogy megkönnyítse a vásárlók döntéseit és az adminisztrátor napi munkáját.
Az **AI-powered Phoneshop** így egy stabil, praktikus és korszerű alapot biztosít a mindennapi online értékesítéshez.


4-es
### Funkcionális követelmények

| Kategória       | Funkció                            | Leírás                                                                                                  |
|-----------------|------------------------------------|---------------------------------------------------------------------------------------------------------|
| Felhasználói    | Regisztráció és bejelentkezés      | A vásárlók saját fiókot hozhatnak létre, bejelentkezés után személyre szabott tartalom jelenik meg.     |
| Felhasználói    | Termékkeresés és szűrés            | A felhasználók ár, típus, márka vagy tulajdonság alapján kereshetnek, az AI pedig segíti a találatokat. |
| Felhasználói    | AI-asszisztens támogatás           | A beépített AI-asszisztens természetes nyelven segít a termékkeresésben és a vásárlási folyamatban.     |
| Felhasználói    | Kosár funkció                      | A kiválasztott termékek kosárban kezelhetők, a rendszer automatikusan számolja a végösszeget.           |
| Felhasználói    | Vásárlási folyamat és fizetés      | A rendszer több fizetési módot támogat, az AI-asszisztens segít a hibák elkerülésében.                  |
| Felhasználói    | Rendeléskövetés                    | A vásárló a saját fiókjában nyomon követheti rendeléseinek státuszát és számláit.                       |
| Felhasználói    | Termékajánlások                    | Az AI személyre szabott ajánlásokat jelenít meg a felhasználói viselkedés alapján.                      |
| Adminisztrációs | Termék- és készletkezelés          | Az admin termékeket tölthet fel, módosíthat, törölhet, és figyelheti a készletmozgásokat.               |
| Adminisztrációs | Felhasználó- és jogosultságkezelés | Az admin felügyeli a vásárlók és adminisztrátorok fiókjait, jogosultságokat oszt ki.                    |
| Adminisztrációs | Riportok és kimutatások            | Az AI automatikus napi, heti és havi riportokat generál az eladásokról és a bevételekről.               |
| Egyéb           | AI-támogatott naplózás             | A rendszer automatikusan rögzíti a műveleteket és az interakciókat az átláthatóság érdekében.           |
| Egyéb           | Rendszerstabilitás és biztonság    | A felület gyors, megbízható és megfelel a GDPR-előírásoknak.                                            |
| Egyéb           | Vásárlói élmény és támogatás       | Az AI gördülékennyé teszi a vásárlási folyamatot, segít az ügyfélszolgálat tehermentesítésében.         |

5-os
### A rendszerre vonatkozó törvények, rendeletek, szabványok

A rendszernek meg kell felelnie a személyes adatok kezelésére és információbiztonságra vonatkozó jogszabályoknak,
különös tekintettel a **GDPR** (General Data Protection Regulation) előírásaira.
A vásárlók személyes adatait kizárólag a szükséges mértékben, biztonságosan és átlátható módon szabad kezelni.

Az **AI-powered Phoneshop** köteles betartani az **elektronikus kereskedelemről szóló hazai és uniós előírásokat**,
beleértve a fogyasztóvédelmi, számlázási és online fizetési szabályokat.
A rendszernek biztosítania kell a vásárlói jogok érvényesítését, a visszaküldés és reklamáció folyamatának jogszerű lebonyolítását, 
valamint a biztonságos online tranzakciókat.

Az adatok tárolását és továbbítását **kódolt formában** kell megvalósítani, az **ISO/IEC 27001**
információbiztonsági szabvány követelményeinek megfelelően. 
A mesterséges intelligencia működésének átláthatósága és elszámoltathatósága érdekében a rendszernek összhangban kell állnia az **EU AI Act**
alapelveivel is.

A szoftver minőségbiztosítását az **ISO/IEC 25010** szabvány irányelvei alapján kell megvalósítani, 
különös figyelmet fordítva a megbízhatóságra, a teljesítményre, a használhatóságra és a biztonságra.

A pénzügyi és riportálási funkcióknak támogatniuk kell a **számviteli és adózási előírások** betartását,
a naplózott adatoknak pedig visszakövethetőnek és hitelesnek kell lenniük.

Összességében a rendszernek biztonságosnak, jogszerűnek, átláthatónak és hosszú távon fenntarthatónak kell működnie,
garantálva a vásárlók adatainak védelmét és a rendszer megbízható üzemeltetését.

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

8-as
### Követelmény lista

| Modul          | Név                        | Kifejtés                                                                                                                             |
|----------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Jogosultság    | Regisztráció és belépés    | A felhasználó e-mail-cím és jelszó segítségével regisztrálhat és léphet be a rendszerbe; hibás adatok esetén hibaüzenet jelenik meg. |
| Jogosultság    | Jogosultsági szintek       | Az adminisztrátor és a vásárlók eltérő hozzáférési jogokkal rendelkeznek; az admin teljes rendszerfelügyeletet kap.                  |
| Felhasználói   | Terméklista                | A rendszer bejelentkezés után megjeleníti az aktuálisan elérhető termékeket, az árakkal és készletinformációkkal együtt.             |
| Felhasználói   | AI-alapú keresés és szűrés | A felhasználók természetes nyelven vagy kulcsszavakkal kereshetnek, szűrhetnek ár, típus vagy márka alapján.                         |
| Felhasználói   | Kosár funkció              | A kiválasztott termékek kosárba helyezhetők, a mennyiségek módosíthatók, és a végösszeg automatikusan frissül.                       |
| Felhasználói   | Rendelés és visszaigazolás | A vásárló a kosár tartalmát megerősítve megrendelést adhat le, amelyről automatikus visszaigazolást kap.                             |
| Felhasználói   | Rendeléskövetés            | A felhasználó a fiókjában nyomon követheti korábbi és aktuális rendeléseit, azok státuszát és számláit.                              |
| Adminisztráció | Termék- és készletkezelés  | Az admin új termékeket tölthet fel, módosíthatja az adatokat, és követheti a készletmozgásokat valós időben.                         |
| Adminisztráció | Felhasználókezelés         | Az adminisztrátor kezelheti a felhasználókat, hozzáadhat új fiókokat, és módosíthatja jogosultságaikat.                              |
| Adminisztráció | Riportkészítés             | Az admin napi, heti és havi riportokat generálhat, amelyek az eladásokat, készleteket és bevételeket tartalmazzák.                   |
| Rendszer       | Stabil működés             | A rendszernek gyorsan és megbízhatóan kell működnie, még nagy terhelés alatt is.                                                     |
| Rendszer       | Biztonság és adatvédelem   | Az adatok kezelése a GDPR és az ISO/IEC 27001 szabvány szerint történik, kódolt adatbázis-tárolással.                                |
| Rendszer       | Naplózás és átláthatóság   | A rendszer minden műveletet naplóz, ezzel segítve az adminisztrációt és a hibák visszakövetését.                                     |
| Rendszer       | AI-támogatás               | A mesterséges intelligencia elemzi a felhasználói viselkedést, támogatja a keresést, az ajánlásokat és a riportokat.                 |

| Fogalomtár      |                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Vásárló         | A rendszer felhasználója, aki termékeket keres, kosárba helyez, megrendel és nyomon követi rendeléseit.                             |
| Adminisztrátor  | Jogosult felhasználó, aki kezeli a termékeket, felhasználókat, riportokat és a rendszer általános működését.                        |
| AI-asszisztens  | Beépített intelligens funkció, amely segíti a vásárlót a keresésben, ajánlásokat ad, valamint támogatja a riportok értelmezését.    |
| Riport          | Összesítő dokumentum, amely tartalmazza az adott időszakban (nap, hét, hónap) eladott termékek adatait, bevételt és statisztikákat. |
| Szűrés          | A termékek listájának leszűkítése ár, típus, kategória vagy más jellemző alapján a gyorsabb keresés érdekében.                      |
| Keresési mező   | Olyan felület, ahol a vásárló kulcsszavakat vagy természetes nyelvű kérdéseket adhat meg az AI által támogatott kereséshez.         |
| Kosár           | A vásárló által kezelt funkció, amely tartalmazza a kiválasztott termékeket, mennyiségeket és azok végösszegét.                     |
| Rendelés        | A vásárló által véglegesített tranzakció, amely tartalmazza a megrendelt termékeket és a fizetési adatokat.                         |
| Készletfigyelés | Az adminisztrátor által használt funkció, amely valós időben mutatja a termékek elérhetőségét és raktárkészletét.                   |
| Sztornózás      | Hibás vagy visszavont rendelés érvénytelenítése a rendszerben, amely frissíti a készletadatokat is.                                 |