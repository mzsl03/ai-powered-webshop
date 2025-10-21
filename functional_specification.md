



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