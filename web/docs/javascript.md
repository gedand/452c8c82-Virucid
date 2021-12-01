# Javascript Documentation

Beüzemelés:
A javascript kód teljeskör? m?ködéséhez néhány feltételnek teljesülnie kell a környezet szempontjából, sajnos a CORS policy miatt. Firefox-ban szükség van a CORS everywhere pluginra, amit aztán be is kell kapcsolni, (zöld ikon jelzi). Valamint a teljes web mappát localhoston kell futtatni egy webszerver segitségével.

Login: A login folyamatnál validáció csak a legyegyszer?bb módon fordul el? frontenden, ilyen a ki nem töltött mez?, vagy a nem engedett karakter, a biztonság szempontjából fontos dolgok mint az adatbázisban vannak implementálva. A login egy post kérésben van megvalósitva, sikeres login esetén elment?dik egy token, innent?l kezdve minden kérés ezen token felhasználásával történik, token nélkül a f?oldal sem látogatható.

Fájlfeltöltés:A fájlfeltöltés során egy POST kérés történik, ha a fájl helyes formátumú és a token is helyes, akkor a fájl feltöltésre kerül, ezután frissülnek a megjelenitend? képek is.

Kép törlés: Kép törlésnél a kép id-ját küldjük be az adatbázis szerverre, ami igy legközelebb már nem fog fetchel?dni, csak admin tud képet törölni. Kép törlés után visszairányitjuk a felhasználót a kezd?oldalra.

Komment: Komment esetén minden képhez saját kommentek tartoznak, viszont nincs név és id? megjelenités a komment mellett.

CAFF fájl letöltés: Caff fájl letöltésnél lekérjük az adatbázisból a caff fájlt, ami után egy letöltés ablak nyilik.

Kérések:A kéréseknél egy kivétellel formdata tipusban küldjük el a kérést, majd a status kód alapján végezzük a további m?veleteket.

Onload: Amikor már az oldalra lépésnél szükséges a tartalom betöltése, az onload függvényt használjuk, ilyen pl a single_image.html-en a kép nagyban megjelenitése, vagy a f?oldalon a képek fetchelése.

HTML elemek generálása: A megjelenitésnél el?fordul, hogy html elemeket generálunk és appendelünk egymásba, ilyen pl a komment, képek megjelenitése.
