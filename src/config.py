import os


# TG bot token
TG_TOKEN: str = os.environ.get('TG_TOKEN')
# Link to TG channel (required with @)
TG_CHANNEL: str = os.environ.get('TG_CHANNEL')

# VK group longpoll token
VK_TOKEN: str = os.environ.get('VK_TOKEN')
# VK API version, may don't change it
VK_API_VERSION: str = os.environ.get('VK_API_VERSION')
