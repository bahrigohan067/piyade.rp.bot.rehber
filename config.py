import os

# Eğer .env dosyası varsa otomatik oku (lokal testler için kolaylık sağlar)
env_file = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip("'\""))

# =====================================================================
# BOT TOKEN & SUNUCU (GUILD) AYARLARI
# =====================================================================
TOKEN = os.getenv("TOKEN_REHBER")
GUILD_ID = int(os.getenv("GUILD_ID", "1529545898294509589"))
ERLC_API_KEY = os.getenv("ERLC_API_KEY", "").strip()

# =====================================================================
# SUNUCU & ROBLOX BİLGİLERİ
# =====================================================================
SUNUCU_ADI = "Piyade RP | Los Angeles"
ERLC_SUNUCU_KODU = "piyade"
ROBLOX_GRUP_ID = 860635623
ROBLOX_GRUP_LINK = "https://www.roblox.com/share/g/860635623"
ANA_BOT_ID = 1544144846875267253  # Sunucunun ana botu (piyade.rp.bot)

# =====================================================================
# KANAL ID'LERİ (Kullanıcının Belirttiği Resmi Liste)
# =====================================================================
REHBER_PANEL_KANAL_ID = 1556687054526611486   # Kalıcı Ana Rehber Panelinin kurulacağı kanal
GENEL_KURALLAR_KANAL_ID = 1532828330380890452 # Genel kurallar kanalı
RP_TERIMLERI_KANAL_ID = 1554940447452037192   # RP terimleri kanalı
DC_DUYURU_KANAL_ID = 1541355760829726760      # DC Sunucu Duyuru kanalı
ETKINLIK_DUYURU_KANAL_ID = 1551312682924253204# Etkinlik duyuru kanalı
RP_DUYURU_KANAL_ID = 1554103929451581460      # RP Duyuru kanalı
UYARILAR_KANAL_ID = 1532828434739368149       # Uyarılar kanalı
ERLC_GLOBAL_DUYURU_ID = 1541354459408629830   # ER:LC Global duyuru kanalı
SOSYAL_MEDYA_KANAL_ID = 1532828546865696889   # Sosyal medya kanalı
RP_OYLAMA_KANAL_ID = 1554037075563651182      # RP oylama kanalı
ROBLOX_GRUP_KANAL_ID = 1554038042157654016    # Roblox grup & karakter onay kanalı
ISTEK_ONERI_KANAL_ID = 1545562405076209714    # İstek Öneri kanalı
KAYIT_KANAL_ID = 1532831582753128530          # Kayıt kanalı
SOHBET_KANAL_ID = 1554924057189941258         # Sohbet kanalı
MEDYA_KANAL_ID = 1554924097723699270          # Medya kanalı
PERM_AL_KANAL_ID = 1554924155927924776        # Perm al kanalı
MUZIK_KANAL_ID = 1554924186684629175          # Müzik oynatma kanalı
BOT_KOMUT_KANAL_ID = 1554924232897732789      # Bot komut kanalı
TICKET_KANAL_ID = 1534770099179884564         # Yazılı ticket kanalı
DESTEK_BEKLEME_SES_ID = 1532829788824404274   # Sesli destek bekleme kanalı
VS_TALEP_KANAL_ID = 1537136926287593503       # VS talep kanalı
VS_SONUC_KANAL_ID = 1537142672953708685       # VS sonuç kanalı
HOSGELDINIZ_KANAL_ID = 1532829955409449081    # Hoşgeldiniz kanalı

# Destek Talebi Direkt Linki
TICKET_KANAL_LINK = f"https://discord.com/channels/{GUILD_ID}/{TICKET_KANAL_ID}"

# =====================================================================
# ROL ID'LERİ
# =====================================================================
KURUCU_ROL_ID = 1529546007635824680
UST_YONETIM_ROL_ID = 1539167256246747186
YONETICI_ROL_ID = 1534798061845483694
YONETIM_EKIBI_ROL_ID = 1537934087166369812

YONETIM_ROLLER = [
    KURUCU_ROL_ID,
    UST_YONETIM_ROL_ID,
    YONETICI_ROL_ID,
    YONETIM_EKIBI_ROL_ID
]

# Görsel Yolları
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BANNER_PATH = os.path.join(BASE_DIR, "assets", "rehber_banner.jpg")

# Renk Temaları
RENK_ANA = 0x2B8CFF       # Canlı Piyade Mavisi
RENK_ALTIN = 0xF1C40F     # Altın Sarısı
RENK_YESIL = 0x2ECC71     # Yeşil (Başarı/Onay)
RENK_KIRMIZI = 0xE74C3C   # Kırmızı (Ceza/Yasak)
RENK_MOR = 0x9B59B6       # Mor (Çete/İllegal)
RENK_TURUNCU = 0xE67E22   # Turuncu (Dikkat/Uyarı)
RENK_KOYU = 0x2F3136      # Koyu Gri (Arkaplan)
