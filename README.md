Oluşturacağınız bir sqlite tablosunda 5 adet sütun bulunacaktır. Bu sütunlar sırasıyla; 
id, x1, y1, x2 ve y2 sütunları olacaktır. Id sütunu unique (benzersiz) olacak ve tüm 
satırlar için farklı olacaktır. 
1 ila 1000 arasında oluşturacağınız rastgele 4 adet sayıyı x1, y1, x2 ve y2 sütunlarına 
yerleştiriniz. Bu işlemi 100 defa yapınız (yani veritabanında 100 adet satır bulunacak). 
Bu sayılar iki boyutlu uzaydaki bir dikdörtgenin 2 köşe noktasının x ve y koordinatlarını 
temsil etmektedir. 
Bu sayılar iki köşe noktasının x ve y koordinatlarını temsil edeceği için x1 x2'den büyük 
olamaz aynı şekilde y1 de y2'den büyük olamaz. Ayrıca bir dikdörtgenin herhangi bir 
kenar uzunluğu 100'den büyük olamaz. Koordinatları veritabanına eklerken bunu göz 
önünde bulundurunuz.  
Daha sonra veritabanından bu değerleri okuyarak üç durum için kontroller yapmanız 
gerekmektedir. Bu üç durum; iki dikdörtgenin kesişmesi, bir dikdörtgenin diğerini 
kapsaması ve bir dikdörtgenin uzaydaki hiçbir dikdörtgen ile kesişmemesi. Hiçbir 
dikdörtgen ile temas etmeyen dikdörtgenleri, birbiriyle kesişen dikdörtgenleri ve bir 
dikdörtgen tarafından kapsanmış dikdörtgenleri açıklamalı bir şekilde ekrana 
yazdırınız. (Bu durumlara sahip dikdörtgenlerin id'sini ve noktalarının koordinatlarını 
ekrana yazdırınız). Örnek çıktılar;  
17 id'li (120, 180) - (200, 190) dikdörtgeni ile 26 id'li (110, 170) - (190, 220) dikdörtgeni 
kesişmektedir. 
24 id’li dikdörtgen hiçbir dikdörtgen ile temas etmemektedir. 
56 id’li (70, 80) - (80, 100) dikdörtgeni, 75 id’li (20, 50) - (120, 250) dikdörtgeni 
tarafından kapsanmaktadır. 
