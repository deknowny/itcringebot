import logging
import typing
import traceback

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import requests

from src import constants, config


# Configure the VK API
vk = vk_api.VkApi(
    token=config.VK_TOKEN,
    api_version=config.VK_API_VERSION
)
api = vk.get_api()

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt='%H:%M:%S',
)


def get_group() -> typing.List[dict]:
    """
    Fetch current group owns the token
    """
    return api.groups.getById()[0]


def create_tg_post(attachments: typing.List[dict], post_text: str) -> None:
    """
    Make a telegram post via vk post's attachments
    """
    url = constants.API_URL + config.TG_TOKEN
    params = {'chat_id': config.TG_CHANNEL}

    if len(attachments) == 0:
        url += '/sendMessage'
        params.update(text=post_text)
    elif len(attachments) == 1:
        url += '/sendPhoto'
        params.update(caption=post_text, photo=attachments[0])
    else:
        url += '/sendMediaGroup'
        pattern = """
            "type": "photo",
            "media": "{}",
            "caption": "{}"
        """
        formatted_text = ''
        count = 0

        for attach in attachments:
            count += 1
            raw_pattern = pattern
            caption_text = ''

            if count == 1:
                caption_text = post_text

            formatted_text += '{' + raw_pattern.format(attach, caption_text) + '}'

            if count != len(attachments):
                formatted_text += ','

        params.update(media=f'[{formatted_text}]'

    resp = requests.post(url, params=params).json()
    if not resp['ok']:
        raise Exception(f'TG API Error: {resp}')


def main() -> None:
    group = get_group()
    logging.info('VK Group <%s> (vk.com/%s) listening', group['name'], group['screen_name'])
    longpoll = VkBotLongPoll(vk, group['id'])

    for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.WALL_POST_NEW:
                attachments = []

                if 'attachments' in event.object:
                    for attach in event.object['attachments']:
                        if attach['type'] == 'photo':
                            attachments.append(attach['photo']['sizes'][-1]['url'])

                create_tg_post(attachments, event.object['text'])
        except Exception as err:
            logging.error(traceback.format_exc())


if __name__ == '__main__':
    main()
