def get_data_deviceinfo(df):
    r = requests.get("https://api.totalkilatgps.com/deviceInfo?grant_type=totalkilatgps&access_token"
                     "=avTTFbiU/myIij3DFe6Kl0YgFH6VCq6En5LxfXE0m1/k2FDVGm5d0XfiY4cThZLnJDSB3pERVSTpPghoDS/F9Nx"
                     "+rHZFGlCwNTC3mZWRQcwwaT1LPT6XKQDstLOJlvEQ")
    data = json.loads(r.text)
    df = pd.DataFrame.from_dict(data[0], orient='columns')
    return df

def get_output_schema():
    return pd.DataFrame({
        'vehicleName': prep_string(),
        'deviceName': prep_string()
    })
