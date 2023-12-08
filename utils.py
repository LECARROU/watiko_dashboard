# API settings
import requests
import pandas as pd
import numpy as np

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNTczODU3LCJpYXQiOjE3MDE4ODI2NTcsImp0aSI6Ijg2OWRjMjA3MTAyOTQxYzE4YTRjMmZhNzIzOTUzNmQzIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInFyX2NvZGUiOm51bGx9.5yPlfzd2yBWd9oXA-Ku-Vp45FvkwAkL7se8SWfqv1xU"

def get_data(endpoint):
    api_url = f"https://watiko.pac-ci.org/api/{endpoint}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print("Erreur lors de la récupération des données. Code de statut:", response.status_code)
        return None

# return patient site based on patient QRCODE
def get_patient_site(qrcode):
    df = pd.read_csv(f'qrcodes.csv',delimiter=",")
    df = df[(qrcode>=df['start']) & (qrcode<=df['end'])]
    if not df.empty:
        return df['structure'].values[0]
    else:
        return None

# return TBA username based on patient QRCODE
def get_patient_tba(qrcode):
    df = pd.read_csv(f'qrcodes.csv',delimiter=",")
    df = df[(qrcode>=df['start']) & (qrcode<=df['end'])]
    if not df.empty:
        return df['username_mat'].values[0]
    else:
        return None

# return TBA site based on her QRCODE
def get_site(qrcode):
    df = pd.read_csv(f'qrcodes.csv',delimiter=",")
    df = df[(qrcode==df['qr_code'])]
    if not df.empty:
        return df['structure'].values[0]
    else:
        return None

# return TBA username based on her QRCODE
def get_username(qrcode):
    df = pd.read_csv(f'qrcodes.csv',delimiter=",")
    df = df[(qrcode==df['qr_code'])]
    if not df.empty:
        return df['username_mat'].values[0]
    else:
        return None