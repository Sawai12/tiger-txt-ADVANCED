import os

API_ID = API_ID = 27412454

API_HASH = os.environ.get("API_HASH", "9a657988cb949b70a313e0c84f14207e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6524349789:AAG0ZLFSVCcscvTcz_DjQdU2HlB3Yrpd9iY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6319179448))


try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6319179448").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


