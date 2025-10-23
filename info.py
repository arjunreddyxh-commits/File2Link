import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'BQGNdJQAY3vnC14LispEuimf6lWS0nFFbbv3jjbWLtdjAb2I-AkOScEtmX_GfCueYW3Zl_klzFzPopWeQMlOdo1gQ8HFAvLL9JKIboy5jRZ6dTmlrAtiV_9rk--CsVWGzr-i6craL0s8bo6Zbo6Lde5Xhik7Lq-qJs6vrOt-Kl-P7tJUdtkaH3M9FhMxa5Rv_WCd2zMFJOhxP-aoARqMGca1XVMKlrvUPoJxWmplSvpNR7_6x0T-XdRP5scvHGirit3hZ6Tr5-nef2PmupM0VTgw5N1bkYnOGnNmQbc_RnP1IJvqToH-cCJW3Bx2DXBHko8dw70BBoVp5X5w_nYA6kJoGJFNXgAAAAGvczYoAA')
API_ID = int(environ.get('API_ID', '20232047'))
API_HASH = environ.get('API_HASH', 'ec4fab92f1d53f4b62db607225d994ad')
BOT_TOKEN = environ.get('BOT_TOKEN', "8357746722:AAGOy2I9Y7oN7Q4l3p_bShxIuqEu9vC-hz0")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002911946418'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '58973445314 7845335174').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/")
('DATABASE_NAME', "rohith")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
