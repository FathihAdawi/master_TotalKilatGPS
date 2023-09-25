from configparser import ConfigParser

import nacl.pwhash


def get_user_detail(filename="D:\All_app_code\Testing Apps\master_totalkilatgps\db.ini", section="api_tkgps"):
    parser = ConfigParser()
    parser.read(filename, encoding="cp1251")

    pwd = bytes(parser.get(section, 'password'), encoding="ascii")
    user = bytes(parser.get(section, 'user'), encoding="ascii")

    # Hashing the pass & user
    pwd = nacl.pwhash.str(pwd)
    user = nacl.pwhash.str(user)


    return user, pwd

get_user_detail()


