# -*- coding: utf-8 -*-
"""
Piyade RP | Los Angeles — Kapsamlı Sunucu Rehberi Bilgi Veritabanı
Tüm kategoriler, kanal rehberleri, kurallar ve sistem detayları burada tanımlıdır.
"""

from config import (
    SUNUCU_ADI, ERLC_SUNUCU_KODU, ROBLOX_GRUP_LINK, ROBLOX_GRUP_ID,
    TICKET_KANAL_LINK,
    GENEL_KURALLAR_KANAL_ID, RP_TERIMLERI_KANAL_ID, DC_DUYURU_KANAL_ID,
    ETKINLIK_DUYURU_KANAL_ID, RP_DUYURU_KANAL_ID, UYARILAR_KANAL_ID,
    ERLC_GLOBAL_DUYURU_ID, SOSYAL_MEDYA_KANAL_ID, RP_OYLAMA_KANAL_ID,
    ROBLOX_GRUP_KANAL_ID, ISTEK_ONERI_KANAL_ID, KAYIT_KANAL_ID,
    SOHBET_KANAL_ID, MEDYA_KANAL_ID, PERM_AL_KANAL_ID, MUZIK_KANAL_ID,
    BOT_KOMUT_KANAL_ID, TICKET_KANAL_ID, DESTEK_BEKLEME_SES_ID,
    VS_TALEP_KANAL_ID, VS_SONUC_KANAL_ID, HOSGELDINIZ_KANAL_ID
)

# Discord'un ince uzun yatay ayracı
DIVIDER = "────────────────────────────────────────"

# =====================================================================
# 1. ANASAYFA VERİLERİ (Sunucu Tanıtımı & "Tüm Kanalları Göster" Vurgusu)
# =====================================================================
ANASAYFA_METIN = f"""
# 🏙️ {SUNUCU_ADI} • HOŞ GELDİNİZ!

{DIVIDER}

### 🌟 Biz Kimiz ve Vizyonumuz Nedir?
**{SUNUCU_ADI}**, Roblox ER:LC (Emergency Response: Liberty County) platformunda en gerçekçi, kurallı ve adil Los Angeles roleplay deneyimini sunmak amacıyla kurulmuş seçkin bir topluluktur.

Sunucumuzda adaleti, yüksek rol kalitesini, saygıyı ve kesintisiz aksiyonu bir araya getiriyoruz. İster kanunlara bağlı bir polis memuru, ister Los Angeles sokaklarında nam salmış bir çete lideri, isterseniz de sakin bir sivil olarak şehrin ritmini belirleyebilirsiniz.

{DIVIDER}

### ⚠️ EN KRİTİK ADIM: "TÜM KANALLARI GÖSTER" SEÇENEĞİ
> 🚨 **HER KATILIMCININ MUTLAKA YAPMASI GEREKEN AYAR:**
> Discord'un yeni kanal filtreleme sistemi sebebiyle bazı üyelerimiz önemli kanalları görememektedir.
> 
> 1️⃣ Sol üst köşede bulunan **`{SUNUCU_ADI}`** sunucu ismine tıklayınız.
> 2️⃣ Açılan menüden **`Tüm Kanalları Göster (Show All Channels)`** seçeneğini bulun ve **işaretleyiniz (aktif edin)**.
> 
> *Bu işlem yapılmadığı takdirde kayıt, duyuru, kurallar ve etkileşim kanallarımızın bir kısmı gizli kalabilir!*

{DIVIDER}

### 🧭 Rehber Menüsü Nasıl Kullanılır?
Aşağıdaki **Açılır Seçim Menüsünü (Select Menu)** kullanarak dilediğiniz kategoriye tek tıkla geçiş yapabilir, sunucumuz hakkındaki tüm bilgilere bu özel mesaj üzerinden anında ulaşabilirsiniz.
"""

# =====================================================================
# 2. GENEL SUNUCU REHBERİ (Tüm 23 Kanalın Detaylı Açıklaması)
# =====================================================================
KANALLAR_METIN = f"""
# 🗺️ GENEL SUNUCU REHBERİ VE KANAL DÜZENİ

{DIVIDER}

Sunucumuzdaki tüm metin ve ses kanalları düzen ve kolaylık sağlamak amacıyla kategorize edilmiştir:

### 📢 DUYURU VE BİLGİLENDİRME
• <#{DC_DUYURU_KANAL_ID}> ➡️ **DC Duyuru:** Discord sunucusu güncellemeleri, bot yenilikleri ve idari kararlar.
• <#{ETKINLIK_DUYURU_KANAL_ID}> ➡️ **Etkinlik Duyuru:** Ödüllü turnuvalar, konvoylar ve özel kapışma duyuruları.
• <#{RP_DUYURU_KANAL_ID}> ➡️ **RP Duyuru:** Rolün başlangıç/bitiş saatleri, sunucu durumu ve aktiflik detayları.
• <#{ERLC_GLOBAL_DUYURU_ID}> ➡️ **ER:LC Global Duyuru:** ER:LC oyun yapımcılarından gelen küresel güncellemeler.
• <#{SOSYAL_MEDYA_KANAL_ID}> ➡️ **Sosyal Medya:** Resmi YouTube, Instagram ve TikTok hesaplarımızın linkleri.
• <#{HOSGELDINIZ_KANAL_ID}> ➡️ **Hoş Geldiniz:** Sunucumuza yeni katılan tüm üyelerimizin karşılandığı kanal.

{DIVIDER}

### 📝 KAYIT VE TOPLULUK BAŞLANGIÇ
• <#{KAYIT_KANAL_ID}> ➡️ **Kayıt:** Whitelist başvurusu yapabileceğiniz ilk başlangıç noktası.
• <#{ROBLOX_GRUP_KANAL_ID}> ➡️ **Roblox Grup:** Resmi Roblox grup linki ve hesap doğrulama paneli.
• <#{PERM_AL_KANAL_ID}> ➡️ **Perm Al:** İlgi alanınıza göre roller: *(Driver, PVP, Builder, Legal, İllegal, Sıcak Kanlı, Müzik)*.
  ⚠️ **Kural:** *Legal ve İllegal rolleri aynı anda kesinlikle alınamaz!*

{DIVIDER}

### 💬 SOHBET, ETKİLEŞİM VE MEDYA
• <#{SOHBET_KANAL_ID}> ➡️ **Sohbet:** Üyelerimizle seviyeli sohbet edebileceğiniz ana kanal.
• <#{MEDYA_KANAL_ID}> ➡️ **Medya:** Oyun içi araç fotoğrafları ve en iyi roleplay anlarınızı paylaşabileceğiniz galeri.
• <#{MUZIK_KANAL_ID}> ➡️ **Müzik Oynatma:** Ses kanallarında müzik botu komutlarını kullanabileceğiniz alan.
• <#{BOT_KOMUT_KANAL_ID}> ➡️ **Bot Komut:** Sistem sorguları ve bot etkileşimlerinin gerçekleştiği kanal.
• <#{ISTEK_ONERI_KANAL_ID}> ➡️ **İstek & Öneri:** Sunucumuz için sistem tavsiyeleri ve fikirlerinizi ileteceğiniz kanal.

{DIVIDER}

### ⚖️ KURAL VE DİSİPLİN KANALLARI
• <#{GENEL_KURALLAR_KANAL_ID}> ➡️ **Genel Kurallar:** Sunucumuzda geçerli temel yazılı kurallar.
• <#{RP_TERIMLERI_KANAL_ID}> ➡️ **RP Terimleri:** Rol içi terimler ve kural tanımları sözlüğü.
• <#{UYARILAR_KANAL_ID}> ➡️ **Uyarılar:** Ceza alan üyelerin sicil kayıtları, ceza puanları ve yetkili bilgisi.

{DIVIDER}

### 🎮 ROL OYLAMA VE VS KANALLARI
• <#{RP_OYLAMA_KANAL_ID}> ➡️ **RP Oylama:** Günlük rol oturumu için katılım oylamasının yapıldığı kanal.
• <#{VS_TALEP_KANAL_ID}> ➡️ **VS Talep:** 1v1 PvP veya Drive kapışma talebi açma. *(RP'yi etkilemez, sadece rank up içindir)*.
• <#{VS_SONUC_KANAL_ID}> ➡️ **VS Sonuç:** Yapılan kapışmaların kazananları ve kademe terfileri.

{DIVIDER}

### 🚨 DESTEK VE YARDIM KANALLARI
• <#{TICKET_KANAL_ID}> ➡️ **Ticket (Destek):** Yazılı destek talebi ve şikayetlerin incelendiği kanal.
• <#{DESTEK_BEKLEME_SES_ID}> ➡️ **Destek Bekleme (Ses):** Yetkililerimizle sesli canlı destek odası.
"""

# =====================================================================
# 3. TÜM KURALLAR (M1 - M13, D1 - D3, Y1 - Y5 & Ceza Puan Sistemi)
# =====================================================================
TUM_KURALLAR_METIN = f"""
# ⚖️ PİYADE RP • TÜM KURAL MADDELERİ VE DİSİPLİN SİSTEMİ

{DIVIDER}

Sunucumuzda huzur, adalet ve kaliteli bir ortamı korumak adına tüm kurallar madde madde ve cezalarıyla birlikte aşağıda belirtilmiştir:

### 🔴 KATEGORİ 1: GENEL SUNUCU KURALLARI (M)
• **M1 ---** Sunucumuzda küfür veya hakarete başvurmak. ➡️ **[2 Ceza Puanı]**
• **M2 ---** Reklam yapmak, hesap/oyun satışı gibi ticari faaliyetlerde bulunmak *(Özel mesajlar / DM dahil)*. ➡️ **[🚨 Kalıcı BAN]**
• **M3 ---** Etkinliklerde veya kapışmalarda karşı taraf rahatsız olduğu halde kendini abartı şekilde övmek, ego kasmak. ➡️ **[1 Ceza Puanı]**
• **M4 ---** Cinsiyet fark etmeksizin üyelere taciz içeren davranışlarda bulunmak. ➡️ **[⏳ 2 Gün Timeout]**
• **M5 ---** Kanalları amacı dışında kullanmak *(Örn: #bot-komut kanalında sohbet etmek)*. ➡️ **[3 Ceza Puanı]**
• **M6 ---** Cinsel içerikli herhangi bir paylaşım *(görsel, yazı, link, video)* yapmak. ➡️ **[8 Ceza Puanı]**
• **M7 ---** Bir kişiye muhatap olmak istemediği sürece sataşmak veya kasten kavga ortamı yaratmak. ➡️ **[4 Ceza Puanı]**
• **M8 ---** Zorbalık yapmak, başka bir üyeyi hedef alarak sunucudan soğutacak tavırlar sergilemek. ➡️ **[5 Ceza Puanı]**
• **M9 ---** Kurucu ve Üst Yönetim bilgisi dışında sunucu üyelerini başka sunucuya veya gruba davet etmek. ➡️ **[🚫 Yasaklı Rolü Verilir]**
• **M10 ---** +18, cinsel taciz, ırkçılık, cinsiyet/yaş ayrımcılığı içeren söylem veya içerik paylaşmak. ➡️ **[⏳ 1 Gün Timeout]**
• **M11 ---** Irkçılık ve her türlü ayrımcılık yapmak. ➡️ **[⏳ 1 Gün Timeout]**
• **M12 ---** Sunucuda bulunan kişilerin psikolojisini etkileyecek argo, küçümseme ve dalga geçme gibi faaliyetlerde bulunmak. ➡️ **[2 Ceza Puanı]**
• **M13 ---** Sunucuda yapılan etkinliklerde ve kapışmalarda 3. Taraf yazılım *(hile, exploit, macro vb.)* kullanmak. ➡️ **[⏳ 1 Gün Timeout + Etkinlikten Men]**

{DIVIDER}

### ⚠️ KATEGORİ 2: SUNUCU DÜZENİ KURALLARI (D)
• **D1 ---** Önemli kanallara *(Duyuru vb.)* anlamsız, boş mesajlar veya flood atmak. ➡️ **[3 Ceza Puanı]**
• **D2 ---** Ses kanallarında ses panelini veya sohbet kanallarında sohbeti gereksiz yere çağırmak *(spawnlamak)*. ➡️ **[3 Ceza Puanı]**
• **D3 ---** Önemli ses kanallarında sürekli hızlıca oda yolculuğu yaparak bildirim kirliliğine yol açmak. ➡️ **[3 Ceza Puanı]**

{DIVIDER}

### 👮 KATEGORİ 3: YETKİLİ KURALLARI VE DİSİPLİN (Y)
• **Y1 ---** Yetkisini kendi lehine veya arkadaşı lehine kullanmak. ➡️ **[🚨 Doğrudan Yetki Alımı / İhraç]**
• **Y2 ---** Sunucudaki katılımcıyı bilerek veya ihmalle yanlış yönlendirmek. ➡️ **[1 Yetkili Uyarısı]**
• **Y3 ---** Hatalı veya kanıtsız işlem yapmak *(Örn: Hatalı uyarı vermek)*. ➡️ **[1 Yetkili Uyarısı]**
• **Y4 ---** Sunucuda kendini üyelerden üstün görmek, kibirli ve saygısız davranmak. ➡️ **[1 Yetkili Uyarısı]**
• **Y5 ---** Kendinden üst kademeli yöneticilerin verdiği talimatları dinlememek/ihmal etmek. ➡️ **[1 Yetkili Uyarısı]**

{DIVIDER}

### 📊 CEZA PUAN SİSTEMİ VE KADEMELER
Aldığınız her ceza puanı sicilinize işlenir ve toplam puana göre kademeniz belirlenir:
• **3 - 5 Puan:** 📍 1. Kademe Uyarı (Uyarı 1 rolü)
• **6 - 8 Puan:** 📍 2. Kademe Uyarı (Uyarı 2 rolü)
• **9 - 11 Puan:** 📍 3. Kademe Uyarı (Uyarı 3 rolü)
• **12 - 14 Puan:** 📍 4. Kademe Uyarı (Uyarı 4 rolü — Kritik Eşik)
• **15+ Puan:** 🚨 **5. Kademe Uyarı (Jail Rolü):** Üye sunucunun tüm genel kanallarından tecrit edilir!
"""

# =====================================================================
# 4. RP TERİMLERİ (RM1 - RM17 Açıklamalar ve Hatalı Rol Örnekleri)
# =====================================================================
RP_TERIMLERI_METIN = f"""
# 🎭 ROLEPLAY (RP) TERİMLERİ SÖZLÜĞÜ VE KURALLAR

{DIVIDER}

Kaliteli bir roleplay deneyimi için tüm terimlerin anlamlarını ve hatalı rol örneklerini aşağıda inceleyebilirsiniz:

• **RM1 — Fail RP (FRP):** Gerçek hayatta mantıken yapılamayacak eylemleri sergilemek.
  🚫 *Hatalı Örnek:* Ağır yaralı haldeyken koşup zıplamak, takla atan arabadan inip hemen kaçmak. ➡️ **[3 Puan]**

• **RM2 — Fear Roleplay:** Karakterinizin can güvenliği tehlikedeyken korku rolü yapmaması.
  🚫 *Hatalı Örnek:* Kafanıza 3 kişi silah doğrultmuşken onlara küfür etmek veya kaçmaya kalkışmak. ➡️ **[3 Puan]**

• **RM3 — Cop Trigger (Cop-Bait):** Kolluk kuvvetlerini rol çıkarmak amacıyla bilerek kışkırtmak.
  🚫 *Hatalı Örnek:* Polis karakolunun önünde bilerek drift atıp polise korna çalmak. ➡️ **[2 Puan]**

• **RM4 — New Life Rule (NLR):** Öldükten sonra hastanede doğunca önceki olayları ve katilinizi unutmama kuralı.
  🚫 *Hatalı Örnek:* Vurulduktan hemen sonra olay yerine silahlanıp katilin peşine dönmek. ➡️ **[4 Puan]**

• **RM5 — Non-RP Driving:** Araçların fiziksel sınırlarını aşarak gerçek dışı sürüş yapmak.
  🚫 *Hatalı Örnek:* Lüks spor araçla dağ yamaçlarından ve uçurumlardan uçarak basıp gitmek. ➡️ **[2 Puan]**

• **RM6 — Combat LOG (CL):** Çatışma, tutuklanma veya rol esnasında cezadan kaçmak için oyundan çıkmak.
  🚫 *Hatalı Örnek:* Polis kelepçe takarken oyunu kapatıp 'Leave' atmak. ➡️ **[3 Puan]**

• **RM7 — Meta Gaming (MG):** Oyun dışından (Discord, ses, yayın vb.) edinilen bilgiyi oyun içine aktarmak.
  🚫 *Hatalı Örnek:* Arkadaşınızın Discord'da 'beni şuraya kaçırdılar' demesiyle konum bilmeden oraya gitmek. ➡️ **[4 Puan]**

• **RM8 — Power Gaming (PG):** Karşı tarafa savunma veya tepki fırsatı vermeden mutlak eylemler yazmak.
  🚫 *Hatalı Örnek:* Tek yumrukla karşısındakini bayıltıp cebindeki tüm parayı almak. ➡️ **[3 Puan]**

• **RM9 — Erotik RP (ERP):** Cinsel ve erotik eylemler sergilemek veya dayatmak.
  🚫 *Hatalı Örnek:* Cinsel imalar veya eylemler içeren roller. ➡️ **[⏳ 4 Gün Timeout]**

• **RM10 — Random Shooting:** Geçerli bir rol veya çatışma gerekçesi olmadan etrafa rastgele ateş açmak.
  🚫 *Hatalı Örnek:* Şehir merkezinde canı sıkıldığı için havaya ve araçlara kurşun sıkmak. ➡️ **[4 Puan]**

• **RM11 — Vehicle Death Match (VDM):** Aracı bir silah gibi kullanarak oyuncuları ezmek.
  🚫 *Hatalı Örnek:* Yolda yürüyen veya kaldırımdaki insanları araçla kasten ezerek öldürmek. ➡️ **[3 Puan]**

• **RM12 — GOOA (Silah Çıkarma Kuralı):** Büyük silahları mantıklı bir kaynak olmadan aniden havadan çıkarmak.
  🚫 *Hatalı Örnek:* Cebinden birdenbire uzun namlulu tüfek çıkartıp taramaya başlamak. ➡️ **[2 Puan]**

• **RM13 — Trash Talk (TT):** Rol dışı kışkırtıcı, alaycı ve toksik söylemlerde bulunmak.
  🚫 *Hatalı Örnek:* Vurulan kişinin başında bekleyip 'bot gibi öldün ezik' demek. ➡️ **[4 Puan]**

• **RM14 — Random Death Match (RDM):** Sebepsizce, diyalogsuz ve rolsüz insan öldürmek.
  🚫 *Hatalı Örnek:* Sokakta yürüyen birini sebepsiz yere arkasından kurşun yağmuruna tutmak. ➡️ **[3 Puan]**

• **RM15 — Kaza RP Yapmama:** Ağır kazalardan sonra hasar/yaralanma rolü yapmadan yola devam etmek.
  🚫 *Hatalı Örnek:* 180 km/h hızla duvara çarptıktan sonra hiçbir şey olmamış gibi gaza basmak. ➡️ **[1 Puan]**

• **RM16 — Refuse RP:** Başlayan rolü mazeretsiz reddetmek, cevap vermemek veya AFK taklidi yapmak.
  🚫 *Hatalı Örnek:* Polis durdurduğunda 'ben oynamıyorum' diyerek hareketsiz beklemek. ➡️ **[2 Puan]**

• **RM17 — Abuse (Açık Suistimali):** Oyun açıklarını veya Safezone sınırlarını kendi lehine suistimal etmek.
  🚫 *Hatalı Örnek:* Safezone çizgisine gir-çık yaparak çatışmada hasar almamaya çalışmak. ➡️ **[5 Puan]**
"""

# =====================================================================
# 5. KAYIT SİSTEMİ (Aşama Aşama Rehber)
# =====================================================================
KAYIT_SISTEMI_METIN = f"""
# 📋 ADIM ADIM KAYIT VE WHITELIST REHBERİ

{DIVIDER}

{SUNUCU_ADI} sunucumuzda rol yapabilmek için 2 aşamalı kayıt sistemimizi tamamlamanız gerekmektedir. Adımları sırasıyla takip ediniz:

### 1️⃣ AŞAMA 1: İLK BAŞVURU FORMU
• <#{KAYIT_KANAL_ID}> kanalına gidiniz.
• Kanalda yer alan **`Kayıt Ol`** butonuna tıklayınız.
• Açılan formda sizden **Gerçek Adınız**, **Roblox Kullanıcı Adınız** ve **Cinsiyetiniz** istenecektir. Eksiksiz doldurup gönderiniz.

{DIVIDER}

### 2️⃣ AŞAMA 2: GİZLİ BAŞVURU KONUSU & İNCELEME
• Form gönderildikten sonra kayıt kanalında yalnızca sizin ve yetkililerin görebileceği **Özel Gizli Bir Konu (Thread)** açılır.
• Başvuru kartınız onay kanalına düşer. Whitelist yetkilimiz başvurunuzu inceler ve onayladığında size **`Grup Onayı Bekliyor`** ara rolü tanımlanır.

{DIVIDER}

### 3️⃣ AŞAMA 3: ROBLOX GRUBU ONAYI (OTOMATİK KABUL)
• <#{ROBLOX_GRUP_KANAL_ID}> kanalına gidiniz.
• [Piyade RP | Los Angeles Roblox Grubumuza]({ROBLOX_GRUP_LINK}) katılma isteği gönderiniz.
• İstek attıktan sonra kanaldaki **`Hesabımı Onayla`** butonuna basınız.
• Sistemimiz Roblox API üzerinden isteğinizi algılar ve **otomatik olarak gruba kabul eder!**

{DIVIDER}

### 4️⃣ AŞAMA 4: KARAKTER FORMU DOLDURMA
• Grup onaylandıktan sonra size özel gizli konunuzda (thread) **`Karakter Oluştur`** butonu belirir.
• Bu butona tıklayarak rol yapacağınız **Karakter Adı** ve **Karakter Yaşını** giriniz.

{DIVIDER}

### 5️⃣ AŞAMA 5: SON ONAY VE WHITELIST
• Karakteriniz onaylandığında **Kayıtsız** ve ara rolleriniz alınır; **Üye**, **Whitelist** ve **Cinsiyet** rolleriniz otomatik tanımlanır.
• Sunucu takma adınız `{{Karakter Adı}} | {{Roblox Adı}}` olarak ayarlanır.
• Başvuru konunuz silinir ve <#1552306929571733635> kayıt log kanalında hoş geldiniz duyurunuz yayınlanır!
"""

# =====================================================================
# 6. ÇETE SİSTEMİ (Parseller, Savaşlar, Cooldown & Meth Üretimi)
# =====================================================================
CETE_SISTEMI_METIN = f"""
# 🏴‍☠️ İLLEGAL DÜNYASI, ÇETE SİSTEMİ VE METH ÜRETİMİ

{DIVIDER}

Los Angeles sokaklarındaki illegal düzen belirli hiyerarşik kurallara bağlıdır. Çete kurmak veya bir çeteye katılmak isteyenlerin bilmesi gerekenler:

### 👑 ÇETE HİYERARŞİSİ VE ROLLER
• **Boss (Lider):** Çetenin mutlak yöneticisidir. Parsel alımı, kasa yönetimi ve savaş kararları Boss'a aittir.
• **Underboss (Sağ Kol):** Çete liderinin yardımcısıdır, lider yokken çete yönetiminden sorumludur.
• **İllegal Üyeler:** Çetenin silahlı gücü ve bölge savunucularıdır.

{DIVIDER}

### 📍 PARSEL VE BÖLGE SİSTEMİ
Çeteler harita üzerinde kendilerine tahsis edilen parsel numaralarına göre konuşlanır.
• **Geçerli Parseller:** `700, 701, 702, 703, 1104, 1108, 1101, 601, 602, 600, 805, 807, 809, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 403, 404, 405, 406, 407, 409, 410, 411`

{DIVIDER}

### ⏳ 7 GÜN ÇETE DEĞİŞTİRME COOLDOWN'I
> ⚠️ **DİKKAT — ÇETE DEĞİŞTİRME KURALI:**
> Bir çeteden kendi isteğiyle ayrılan veya lider tarafından çıkarılan herhangi bir üye, **7 gün boyunca başka hiçbir çeteye katılamaz veya yeni çete kuramaz**. Bu süre sistem tarafından otomatik takip edilir.

{DIVIDER}

### 💰 ÇETE KASASI, DEPOSU VE UYARILAR
• Çeteler etkinlik ve operasyonlarla seviye atladıkça kasa limitleri ve depo kapasiteleri artar.
• Disiplinsizlik yapan çeteler resmi çete uyarısı alır. **3 çete uyarısına ulaşan oluşum feshedilir** ve parseli boşa düşer.

{DIVIDER}

### 🧪 METH LABORATUVARI VE KİMYASAL ÜRETİM
• İllegal üyeler laboratuvar kurarak kimyasal üretim mini oyununa katılabilir.
• Reaksiyon sorularına doğru cevap vererek üretim tamamlanır ve gelir elde edilir.
• **Büyük Tehlikeler:**
  💥 **Patlama Riski:** Hatalı adımlarda laboratuvar patlayabilir ve karakteriniz ölür (**İnfaz / Ölü** rolü alır).
  🚨 **Polis İhbarı:** Duman sızıntısı sonucu polis merkezine anında otomatik ihbar düşer ve **Aranan** statüsü alırsınız!
"""

# =====================================================================
# 7. VS TALEP SİSTEMİ (PvP / Drive & Kademe Sistemi)
# =====================================================================
VS_TALEP_METIN = f"""
# ⚔️ 1v1 VS (KAPIŞMA) VE KADEME (RANK UP) SİSTEMİ

{DIVIDER}

Bireysel refleks ve sürüş kabiliyetinizi kanıtlamak için VS talep sistemimizi kullanabilirsiniz:

### ⚠️ ÖNEMLİ KURAL: RP'DEN BAĞIMSIZDIR
> 📌 **BİLİNMESİ GEREKEN EN TEMEL HUSUS:**
> <#{VS_TALEP_KANAL_ID}> kanalından açılan VS talepleri **Roleplay sunucusunun gidişatını kesinlikle etkilemez**. 
> Bu kapışmalar yalnızca katılımcıların bireysel rütbelerini yükseltmek (**Rank Up**) amacıyla düzenlenir.

{DIVIDER}

### 🎯 KAPIŞMA TÜRLERİ
• **PvP Düellosu:** Silahlı 1v1 çatışma yeteneği kapışmasıdır.
• **Drive Düellosu:** Araç kontrolü, takip ve kaçış yeteneği kapışmasıdır.

{DIVIDER}

### 🏆 KADEME SIRALAMASI
Her galibiyet sizi bir üst kademeye terfi ettirir:
• **Temel Kademe** ➡️ Başlangıç
• **Kademe 1 ➡️ Kademe 2 ➡️ Kademe 3**
• **Kademe 4 ➡️ Kademe 5 ➡️ Kademe 6**
• 👑 **Kademe 7 (Zirve):** Sunucunun en üst düzey kapışmacı unvanıdır!

{DIVIDER}

### ⚖️ YÖNETİM VE KURALLAR
• Kapışmalar **PvP Manager**, **Drive Manager** ve **Kapışma Talep Yetkilisi** denetiminde özel odalarda gerçekleşir.
• Hile, makro veya 3. parti yazılım kullanımı doğrudan diskalifiye ve M13 gereği **1 Gün Timeout** ile sonuçlanır.
• Maç sonuçları ve terfiler <#{VS_SONUC_KANAL_ID}> kanalında ilan edilir.
"""

# =====================================================================
# 8. ER:LC BİLGİ (Oyun Durumu, Safezonelar ve Katılım)
# =====================================================================
ERLC_BILGI_METIN = f"""
# 🎮 ER:LC OYUN SUNUCUSU, CANLI BİLGİ VE SAFEZONE

{DIVIDER}

Roblox Emergency Response: Liberty County sunucumuza dair tüm teknik bilgiler aşağıdadır:

### 🔑 SUNUCU KATILIM KODU
> Sunucu Katılım Kodu: **`{ERLC_SUNUCU_KODU}`**
• Roblox ER:LC oyununa giriniz ➡️ **Servers (Sunucular)** sekmesini açınız ➡️ **Join by Code (Kod ile Katıl)** alanına **`{ERLC_SUNUCU_KODU}`** yazarak doğrudan bağlanınız!

{DIVIDER}

### 🛡️ SAFEZONE (GÜVENLİ BÖLGE) KURALLARI
Aşağıdaki koordinat ve bölgelerde herhangi bir şekilde çatışmaya girmek, adam vurmak, rehin almak veya soygun yapmak kesinlikle **YASAKTIR**:
• **Silah Mağazası (Gun Shop):** İçinde ve kapı önünde silah çekmek yasaktır.
• **Polis Departmanı (PD):** Kolluk kuvvetleri ana karargahı güvenli bölgedir.
• **Hastane ve Acil Servis:** Tedavi ve yeniden doğma alanları dokunulmazdır.
• **Araç Modifiye ve Tamir İstasyonları:** Tamir sırasındaki araçlara saldırı yapılamaz.

{DIVIDER}

### 👥 CANLI OYUNCU VE AKTİFLİK DURUMU
• Sunucumuzun anlık aktif oyuncu ve sıra sayısını Discord ana botumuz olan **<#1544144846875267253>** durumu üzerinden anlık takip edebilirsiniz.
• Rol başlangıç ve aktiflik durumları <#{RP_DUYURU_KANAL_ID}> kanalında @| Whitelist rolü etiketlenerek ilan edilir.
• Rol öncesi katılım sayımı için <#{RP_OYLAMA_KANAL_ID}> kanalındaki oylamalara katılabilirsiniz.
"""

# =====================================================================
# 9. DİĞER BİLGİLER VE DESTEK MERKEZİ
# =====================================================================
DIGER_METIN = f"""
# ❓ DİĞER BİLGİLER VE DESTEK MERKEZİ

{DIVIDER}

Aradığınız bilgiye bu rehberde ulaşamadıysanız veya özel bir yardıma ihtiyacınız varsa aşağıdaki kanallardan destek alabilirsiniz:

### 🎫 YAZILI DESTEK TALEBİ (TICKET)
• Bir kural ihlali şikayeti, hesap sorunu veya teknik bir aksaklık durumunda <#{TICKET_KANAL_ID}> kanalına giderek destek talebi açınız.
• Destek biletinize olayla ilgili ekran görüntüsü veya video kanıtı eklemeniz işlemlerinizi hızlandıracaktır.
• [Buraya Tıklayarak Destek Kanalına Ulaşabilirsiniz]({TICKET_KANAL_LINK})

{DIVIDER}

### 🔊 SESLİ CANLI YARDIM
• Sorununuzu sesli olarak aktarmak isterseniz <#{DESTEK_BEKLEME_SES_ID}> kanalına geçerek yetkili ekibimizin odaya gelmesini bekleyebilirsiniz.

{DIVIDER}

### 💡 FİKİR VE ÖNERİ BİLDİRİMİ
• Sunucumuza katkı sağlayacak yenilikçi fikirleriniz varsa <#{ISTEK_ONERI_KANAL_ID}> kanalından önerinizi paylaşabilirsiniz.
"""
