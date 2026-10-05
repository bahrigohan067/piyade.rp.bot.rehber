# 📖 Piyade RP | Los Angeles — Resmi Sunucu Rehber Botu

**Piyade RP | Los Angeles** Roblox (ER:LC) ve Discord sunucusu için geliştirilmiş interaktif, modern ve tek merkezden yönetilen rehber botu.

Bu bot, sunucu kanallarındaki görsel düzeni ve akışı bozmamak adına **Direkt Mesaj (DM)** üzerinden kişiye özel olarak çalışır. Sunucu kanalında sabit duran şık bir panelden butona tıklayan her üyeye özel olarak DM iletilir ve kullanıcı tüm kategorileri açılır menü ve butonlarla gezebilir.

---

## 🚀 Temel Özellikler

1. **Kanala Sabit Kalıcı Panel (`/rehber-paneli-kur`):**
   - Hedef kanal: `#1556687054526611486`
   - Büyük yüksek çözünürlüklü banner görseli (`assets/rehber_banner.jpg`).
   - Kalıcı buton: `📖 Rehberi Başlat (DM Kutunuza Gönderir)`
   - Butona basıldığında sunucuda kalabalık yapmaz; ephemeral (yalnızca tıklayana özel) bildirim gösterir ve DM'den rehberi açar.
   - Kullanıcının DM'i kapalıysa uyarıp nasıl açacağını adım adım anlatır.

2. **DM Üzerinde 9 Farklı Zengin Kategori (Birleşik Sistem):**
   - ℹ️ **Anasayfa:** Sunucu tanıtımı, vizyon ve **"Tüm Kanalları Göster"** ayarının kritik önemi.
   - ℹ️ **Genel Sunucu Rehberi:** Sunucudaki 23 kanalın tamamının işlevleri, rolleri ve doğrudan etiket linkleri.
   - ℹ️ **Tüm Kurallar:** M1-M13 Genel Kurallar, D1-D3 Sunucu Düzeni, Y1-Y5 Yetkili Kuralları ve Ceza Puanı Kademeleri.
   - ℹ️ **RP Terimleri:** RM1-RM17 kuralları, terim tanımları ve hatalı rol örnekleri.
   - ℹ️ **Kayıt Sistemi:** Aşama aşama Roblox grubu (ID: `860635623`), otomatik kabul, gizli thread ve Whitelist süreci.
   - ℹ️ **Çete Sistemi:** Boss/Underboss, parsel listesi, 7 gün cooldown, bölge savaşları ve meth üretimi riskleri.
   - ℹ️ **Vs Talep Sistemi:** 1v1 PvP ve Drive kapışmaları, Temel Kademe'den Kademe 7'ye terfi, rank up mantığı.
   - ℹ️ **ER:LC Bilgi:** Oyun katılım kodu (`piyade`), Safezonelar, canlı oyuncu sayısı (Ana Bot durumu veya API) ve RP aktiflik takibi.
   - ℹ️ **Diğer...:** Ticket açma ve canlı sesli destek yönlendirmesi.

3. **Görsel Standartlar:**
   - Her kategoride büyük banner görseli yer alır (`rehber_banner.jpg`).
   - Başlık ve paragrafların arasında Discord'un ince uzun çizgisi (`────────────────────────────────────────`) bulunur.
   - Renkli temalar ve bol emojili düzen.

4. **Sohbet Dinleyicisi (Auto-Help):**
   - Yeni üyeler sohbette "nasıl kayıt olunur", "kod nedir", "grup linki", "bilet nasıl açılır" gibi sorular sorduğunda bot nazikçe ve cooldown korumalı olarak rehbere ve ilgili kanallara yönlendirir.

---

## ⚙️ Kurulum & Railway Dağıtımı

### Ortam Değişkenleri (Variables)

| Değişken Adı | Açıklama |
|---|---|
| `TOKEN_REHBER` | Botun Discord Token'ı (**Zorunlu**) |
| `GUILD_ID` | Hedef Sunucu ID'si (`1529545898294509589`) |
| `ERLC_API_KEY` | *(Opsiyonel)* ER:LC sunucu API anahtarı |

> [!IMPORTANT]
> Railway panelinde botun servis değişkenlerine **`TOKEN_REHBER`** adıyla token tanımlanmalıdır.

---

## 📜 Komutlar

| Komut | Yetki | Açıklama |
|---|---|---|
| `/rehber-paneli-kur [kanal]` | Yönetim | Belirtilen kanala sabit ve kalıcı Ana Rehber Panelini kurar |
| `/rehber` | Herkes | Rehber panelini doğrudan kullanıcının DM kutusuna gönderir |