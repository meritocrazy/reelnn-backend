# Main configuration file

# Mandatory Variables
API_ID = 11853166 # Replace with your actual Telegram API ID
API_HASH = "ea6757c5018522a64f218c9b2b04b36a"  # Replace with your actual Telegram API Hash
BOT_TOKEN = "5233363208:AAFEertT_nqXcSSE5ZSj02_lrfMWRLsaYyA"  # Replace with your actual Bot Token
OWNER_ID = "1111361692"  # Replace with your actual Owner ID
# Database
DATABASE_URL = "your_database_url_here"  # Replace with your actual database URL

AUTH_CHAT = "-1001998401354" # Replace with your actual auth chat ID. You can use multiple IDs separated by ( space ).
LOGS_CHAT = -1002034956264 # Replace with your actual logs chat ID
POST_CHAT = -1001263140310 # Replace with your actual post chat ID

ADMIN_USERNAME = "serotonin" # Replace with your admin username
ADMIN_PASSWORD = "M@nusia123" # Replace with your admin password


SITE_SECRET = "kmzway87aa" # Replace with your site secret key
TMDB_API_KEY = "9d30545aa5e2035b2da1eecb2bfc05fd" # Replace with your TMDB API key

# Optional Variables

# If you want to use multiple bot tokens, uncomment the MULTI_TOKENS dictionary and add your tokens. this aditional bots will speed up the process of downloading and streaming files.
MULTI_TOKENS = {
     1: "7442262550:AAHZkfDBnkDHggyXkfk5lP3LT52F7FlUH3A",
     2: "8189763987:AAGDHoFALetc-A_hi133AIIjyV-bp219DxE",
    # Add more tokens as needed
}
DELETE_AFTER_MINUTES = 10 # Set the number of minutes after which files will be deleted from user message
POST_UPDATES = True # Set to True if you want to post updates in the post chat
USE_CAPTION = True # Set to True if you want to use captions for posts instead of file names.

# Port configuration
import os
PORT = int(os.environ.get("PORT", 8080))
















# (Don't touch this unless you know what you're doing)
SUDO_USERS = [int(x) for x in (OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in (AUTH_CHAT).split()]