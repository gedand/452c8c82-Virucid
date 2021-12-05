# Javascript Documentation

Be�zemel�s:
A javascript k�d teljesk�r? m?k�d�s�hez n�h�ny felt�telnek teljes�lnie kell a k�rnyezet szempontj�b�l, sajnos a CORS policy miatt. Firefox-ban sz�ks�g van a CORS everywhere pluginra, amit azt�n be is kell kapcsolni, (z�ld ikon jelzi). Valamint a teljes web mapp�t localhoston kell futtatni egy webszerver segits�g�vel.

Login: A login folyamatn�l valid�ci� csak a legyegyszer?bb m�don fordul el? frontenden, ilyen a ki nem t�lt�tt mez?, vagy a nem engedett karakter, a biztons�g szempontj�b�l fontos dolgok mint az adatb�zisban vannak implement�lva. A login egy post k�r�sben van megval�sitva, sikeres login eset�n elment?dik egy token, innent?l kezdve minden k�r�s ezen token felhaszn�l�s�val t�rt�nik, token n�lk�l a f?oldal sem l�togathat�.

F�jlfelt�lt�s:A f�jlfelt�lt�s sor�n egy POST k�r�s t�rt�nik, ha a f�jl helyes form�tum� �s a token is helyes, akkor a f�jl felt�lt�sre ker�l, ezut�n friss�lnek a megjelenitend? k�pek is.

K�p t�rl�s: K�p t�rl�sn�l a k�p id-j�t k�ldj�k be az adatb�zis szerverre, ami igy legk�zelebb m�r nem fog fetchel?dni, csak admin tud k�pet t�r�lni. K�p t�rl�s ut�n visszair�nyitjuk a felhaszn�l�t a kezd?oldalra.

Komment: Komment eset�n minden k�phez saj�t kommentek tartoznak, viszont nincs n�v �s id? megjelenit�s a komment mellett.

CAFF f�jl let�lt�s: Caff f�jl let�lt�sn�l lek�rj�k az adatb�zisb�l a caff f�jlt, ami ut�n egy let�lt�s ablak nyilik.

K�r�sek:A k�r�sekn�l egy kiv�tellel formdata tipusban k�ldj�k el a k�r�st, majd a status k�d alapj�n v�gezz�k a tov�bbi m?veleteket.

Onload: Amikor m�r az oldalra l�p�sn�l sz�ks�ges a tartalom bet�lt�se, az onload f�ggv�nyt haszn�ljuk, ilyen pl a single_image.html-en a k�p nagyban megjelenit�se, vagy a f?oldalon a k�pek fetchel�se.

HTML elemek gener�l�sa: A megjelenit�sn�l el?fordul, hogy html elemeket gener�lunk �s appendel�nk egym�sba, ilyen pl a komment, k�pek megjelenit�se.
