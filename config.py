from configparser import ConfigParser


def get_user_detail(filename="D:\All_app_code\Testing Apps\master_totalkilatgps\db.ini", section="api_tkgps"):
    parser = ConfigParser()
    parser.read(filename)
    user = parser.get(section, 'user')
    pwd = parser.get(section, 'password')

    return user, pwd


