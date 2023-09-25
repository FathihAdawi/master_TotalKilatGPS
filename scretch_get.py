import nacl.pwhash
import requests
import pandas as pd
import json
from datetime import datetime
from config import get_user_detail

pd.set_option('display.max_columns', 10, 'display.max_rows', 10)


def get_Token():
    user, pwd = get_user_detail()
    p = nacl.pwhash.str(b+pwd)

    r = requests.get("https://api.totalkilatgps.com/"
                     "token?grant_type=totalkilatgps&account_name=" + user + "&account_password=" + pwd)
    token = json.loads(r.text)
    m_token = token['access_token']

    return m_token


def APIcall_geoFence():
    r = requests.get("https://api.totalkilatgps.com/"
                     "geofenceInfo?grant_type=totalkilatgps&access_token=" + get_Token() + "&geoName=")
    data = json.loads(r.text)
    df_geoFence = pd.DataFrame(data[0])
    df_geoFence.reset_index(drop=True, inplace=True)
    print(df_geoFence)

    return df_geoFence


def APIcall_DeviceInformation():
    r = requests.get("https://api.totalkilatgps.com/deviceInfo?grant_type=totalkilatgps&access_token=" + get_Token())
    data = json.loads(r.text)
    dfDeviceInformation = pd.DataFrame(data[0])
    dfDeviceInformation.reset_index(drop=True, inplace=True)
    print(dfDeviceInformation)

    return dfDeviceInformation


def APIcall_DeviceHistoryData():
    r = requests.get("https://api.totalkilatgps.com/"
                     "deviceHistoryData?"
                     "grant_type=totalkilatgps&access_token="
                     + get_Token() + "&device_name=42976836"
                                     "&start_time=2023-08-22 10:05:33&end_time=2023-08-23 23:00:00")

    data = json.loads(r.text)
    dfDeviceHistoryData = pd.DataFrame(data[0])
    dfDeviceHistoryData.reset_index(drop=True, inplace=True)
    print(dfDeviceHistoryData)

    return dfDeviceHistoryData


def APIcall_LatestVehiclePosition():
    r = requests.get("https://api.totalkilatgps.com/latestVehiclePosition?grant_type=totalkilatgps&access_token"
                     "=" + get_Token() + "&device_name=42976836")

    data = json.loads(r.text)
    dfLatestVehiclePosition = pd.DataFrame(data[0])
    dfLatestVehiclePosition.reset_index(drop=True, inplace=True)
    print(dfLatestVehiclePosition)

    return dfLatestVehiclePosition


def combine_excel_per_sheet():
    with pd.ExcelWriter("Master_TotalKilatGPS_" + datetime.now().strftime("%m-%d-%Y") + ".xlsx") as writer:
        APIcall_geoFence().to_excel(writer, sheet_name='geoFence')
        APIcall_DeviceInformation().to_excel(writer, sheet_name='Device_Information')
        APIcall_DeviceHistoryData().to_excel(writer, sheet_name='Device_History_Data')
        APIcall_LatestVehiclePosition().to_excel(writer, sheet_name='Latest_Vehicle_Position')


APIcall_geoFence()
APIcall_DeviceInformation()
APIcall_DeviceHistoryData()
APIcall_LatestVehiclePosition()
combine_excel_per_sheet()
