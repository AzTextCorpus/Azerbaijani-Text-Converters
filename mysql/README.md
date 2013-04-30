Quraşdırma
===================================

Bu scripti mövcud bazanızda icra edin. Bu zaman bazada (schema) "convert_AzLat2Unicode" adlı prosedura (stored procedure) yaranacaq. 

İstifadə
===================================

Konvertordan istifadə etmək üçün 

CALL convert_AzLat2Unicode(<cədvəlin_adı>) yazıb icra etmək lazımdır. 
Nümunə:
CALL convert_AzLat2Unicode('Table1')

Bu zaman Table1 cədvəlinin bütün sütunlarında köhnə şriftlərlə yazılmış mətnlər unikod standartı ilə yazılmış mətnə çevriləcək. 

Çevirmə cədvəli
===================================

{й,ц,у,к,е,н,г,ш,щ,з,х,ъ,ф,ы,в,а,п,р,о,л,д,ж,э,я,ч,с,м,и,т,ь,б,ю,Й,Ц,У,К,Е,Н,Г,Ш,Щ,З,Х,Ъ,Ф,Ы,В,А,П,Р,О,Л,Д,Ж,Э,Я,Ч,С,М,И,Т,Ь,Б,Ю}
{y,ü,u,k,e,n,q,ş,h,z,x,c,f,ı,v,a,p,r,o,l,d,j,g,ə,ç,s,m,i,t,ğ,b,ö,Y,Ü,U,K,E,N,Q,Ş,H,Z,X,C,F,I,V,A,P,R,O,L,D,J,G,Ə,Ç,S,M,İ,T,Ğ,B,Ö}

