Quraşdırma
===================================

Bu scripti mövcud bazanızda icra edin. Bu zaman bazada (schema) "convert_AzLat2Unicode" adlı prosedura (stored procedure) yaranacaq. 

İstifadə
===================================

Konvertordan istifadə etmək üçün 
<pre><code>
CALL convert_AzLat2Unicode(<cədvəlin_adı>) 
</code></pre>
yazıb icra etmək lazımdır. 
Nümunə:
<pre><code>
CALL convert_AzLat2Unicode('Table1')
</code></pre>
Bu zaman Table1 cədvəlinin bütün sütunlarında köhnə şriftlərlə yazılmış mətnlər unikod standartı ilə yazılmış mətnə çevriləcək. 

Çevirmə cədvəli
===================================

| From        | To           | 
| ------------- |:-------------:|
|  й	|	y	|
|	ц	|	ü	|
|	у	|	u	|
|	к	|	k	|
|	е	|	e	|
|	н	|	n	|
|	г	|	q	|
|	ш	|	ş	|
|	щ	|	h	|
|	з	|	z	|
|	х	|	x	|
|	ъ	|	c	|
|	ф	|	f	|
|	ы	|	ı	|
|	в	|	v	|
|	а	|	a	|
|	п	|	p	|
|	р	|	r	|
|	о	|	o	|
|	л	|	l	|
|	д	|	d	|
|	ж	|	j	|
|	э	|	g	|
|	я	|	ə	|
|	ч	|	ç	|
|	с	|	s	|
|	м	|	m	|
|	и	|	i	|
|	т	|	t	|
|	ь	|	ğ	|
|	б	|	b	|
|	ю	|	ö	|
|	Й	|	Y	|
|	Ц	|	Ü	|
|	У	|	U	|
|	К	|	K	|
|	Е	|	E	|
|	Н	|	N	|
|	Г	|	Q	|
|	Ш	|	Ş	|
|	Щ	|	H	|
|	З	|	Z	|
|	Х	|	X	|
|	Ъ	|	C	|
|	Ф	|	F	|
|	Ы	|	I	|
|	В	|	V	|
|	А	|	A	|
|	П	|	P	|
|	Р	|	R	|
|	О	|	O	|
|	Л	|	L	|
|	Д	|	D	|
|	Ж	|	J	|
|	Э	|	G	|
|	Я	|	Ə	|
|	Ч	|	Ç	|
|	С	|	S	|
|	М	|	M	|
|	И	|	İ	|
|	Т	|	T	|
|	Ь	|	Ğ	|
|	Б	|	B	|
|	Ю	|	Ö	|
