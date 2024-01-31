from .api import post_request
from .mail import send_email
from .util import load_stations, format_date
import config
import datetime

stations = load_stations()
binis_istasyon_id = stations.get(config.binis_istasyon_adi)
inis_istasyon_id = stations.get(config.inis_istasyon_adi)
formatted_date = format_date(config.date)

sefer_url = "https://api-yebsp.tcddtasimacilik.gov.tr/sefer/seferSorgula"
vagon_url = "https://api-yebsp.tcddtasimacilik.gov.tr/vagon/vagonHaritasindanYerSecimi"

# Function to fetch and filter journeys
def fetch_and_filter_journeys():
    formatted_date = format_date(config.date)
    body = {
        "kanalKodu": 3,
        "dil": 0,
        "seferSorgulamaKriterWSDVO": {
            "satisKanali": 3,
            "binisIstasyonu": config.binis_istasyon_adi,
            "inisIstasyonu": config.inis_istasyon_adi,
            "binisIstasyonId": binis_istasyon_id,
            "inisIstasyonId": inis_istasyon_id,
            "binisIstasyonu_isHaritaGosterimi": False,
            "inisIstasyonu_isHaritaGosterimi": False,
            "seyahatTuru": 1,
            "gidisTarih": f"{formatted_date} 00:00:00 AM",
            "bolgeselGelsin": False,
            "islemTipi": 0,
            "yolcuSayisi": 1,
            "aktarmalarGelsin": True,
        }
    }

    print(f"Checking for date: {formatted_date}")
    response = post_request(sefer_url, body)
    data = response.json()

    if data['cevapBilgileri']['cevapKodu'] == '000':
        for sefer in data['seferSorgulamaSonucList']:
            sefer_time = datetime.datetime.strptime(sefer['binisTarih'], "%b %d, %Y %I:%M:%S %p")
            if config.check_specific_hour:
                specified_time = datetime.datetime.strptime(f"{config.date} {config.hour}", "%Y-%m-%d %H:%M")
                if sefer_time.strftime("%H:%M") == specified_time.strftime("%H:%M"):
                    check_sefer(sefer)
            else:
                check_sefer(sefer)


# Function to check available seats in a journey
def check_sefer(sefer):
    print(f"Checking for time: {sefer['binisTarih']}")
    for vagon in sefer['vagonTipleriBosYerUcret']:
        for vagon_detail in vagon['vagonListesi']:
            vagon_sira_no = vagon_detail['vagonSiraNo']
            print(f"Checking for vagon: {vagon_sira_no}")
            check_specific_seats(sefer['seferId'], vagon_sira_no, sefer['trenAdi'], sefer['binisTarih'])


# Function to check for specific seats in a wagon
def check_specific_seats(seferId, vagon_sira_no, tren_adi, binis_tarih):
    body = {
        "kanalKodu": "3",
        "dil": 0,
        "seferBaslikId": seferId,
        "vagonSiraNo": vagon_sira_no,
        "binisIst": config.binis_istasyon_adi,
        "InisIst": config.inis_istasyon_adi
    }
    
    response = post_request(vagon_url, body)
    data = response.json()

    if data['cevapBilgileri']['cevapKodu'] == '000':
        for seat in data['vagonHaritasiIcerikDVO']['koltukDurumlari']:
            if seat['durum'] == 0: # Available
                if not seat['koltukNo'].endswith('h'): # Not Handicapped 
                    print(f"Available seat: {seat['koltukNo']} in Wagon {vagon_sira_no}")
                    send_email(tren_adi, binis_tarih, vagon_sira_no, seat['koltukNo'])
                else: # Handicapped
                    print(f"Available handicapped seat: {seat['koltukNo']} in Wagon {vagon_sira_no}")