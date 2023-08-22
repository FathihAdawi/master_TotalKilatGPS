import requests
import pandas as pd
import json
from datetime import datetime

pd.set_option('display.max_columns', 10, 'display.max_rows', 10)


def APIcall_geoFence():
    r = requests.get("https://api.totalkilatgps.com/geofenceInfo?grant_type=totalkilatgps&access_token=GBQ0cbg"
                     "/YOrLbmf0Z0DBfDH02FPUpJPHJ"
                     "/MDt99CnqAx5nUg3rE0Q9bCllY9gWCyI7zDTp6a9XFtLhcAbn6sDgfrhg3tNhepCibmzgdSD3iGilBZ1EK1LcIg+8RobUJh"
                     "&geoName=")
    data = json.loads(r.text)
    df_geoFence = pd.DataFrame(data[0])
    df_geoFence.reset_index(drop=True, inplace=True)
    print(df_geoFence)

    # df_geoFence.to_excel(
    #     "geoFence_"+str(datetime.now().strftime("%m-%d-%Y"))+".xlsx"
    # )
    return df_geoFence


def APIcall_DeviceInformation():
    r = requests.get("https://api.totalkilatgps.com/deviceInfo?grant_type=totalkilatgps&access_token=GBQ0cbg"
                     "/YOrLbmf0Z0DBfDH02FPUpJPHJ"
                     "/MDt99CnqAx5nUg3rE0Q9bCllY9gWCyI7zDTp6a9XFtLhcAbn6sDgfrhg3tNhepCibmzgdSD3iGilBZ1EK1LcIg+8RobUJh")
    data = json.loads(r.text)
    dfDeviceInformation = pd.DataFrame(data[0])
    dfDeviceInformation.reset_index(drop=True, inplace=True)
    print(dfDeviceInformation)

    # dfDeviceInformation.to_excel(
    #     "DeviceInformation_" + str(datetime.now().strftime("%m-%d-%Y")) + ".xlsx"
    # )
    return dfDeviceInformation


def APIcall_DeviceHistoryData():
    r = requests.get("https://api.totalkilatgps.com/deviceHistoryData?grant_type=totalkilatgps&access_token=GBQ0cbg"
                     "/YOrLbmf0Z0DBfDH02FPUpJPHJ"
                     "/MDt99CnqAx5nUg3rE0Q9bCllY9gWCyI7zDTp6a9XFtLhcAbn6sDgfrhg3tNhepCibmzgdSD3iGilBZ1EK1LcIg+8RobUJh"
                     "&device_name=42976836&start_time=2023-08-22 10:05:33&end_time=2023-08-23 23:00:00")

    data = json.loads(r.text)
    dfDeviceHistoryData = pd.DataFrame(data[0])
    dfDeviceHistoryData.reset_index(drop=True, inplace=True)

    print(dfDeviceHistoryData)

    # dfDeviceHistoryData.to_excel(
    #     "DeviceHistoryData_" + str(datetime.now().strftime("%m-%d-%Y")) + ".xlsx"
    # )
    return dfDeviceHistoryData


def APIcall_LatestVehiclePosition():
    r = requests.get("https://api.totalkilatgps.com/latestVehiclePosition?grant_type=totalkilatgps&access_token"
                     "=GBQ0cbg/YOrLbmf0Z0DBfDH02FPUpJPHJ"
                     "/MDt99CnqAx5nUg3rE0Q9bCllY9gWCyI7zDTp6a9XFtLhcAbn6sDgfrhg3tNhepCibmzgdSD3iGilBZ1EK1LcIg+8RobUJh"
                     "&device_name=42976836")

    data = json.loads(r.text)
    dfLatestVehiclePosition = pd.DataFrame(data[0])
    dfLatestVehiclePosition.reset_index(drop=True, inplace=True)

    print(dfLatestVehiclePosition)

    # dfLatestVehiclePosition.to_excel(
    #     "LatestVehiclePosition_" + str(datetime.now().strftime("%m-%d-%Y")) + ".xlsx"
    # )
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
