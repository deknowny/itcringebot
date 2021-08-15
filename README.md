# [ITCringeBot](https://vk.com/itcringe)

!["Made with Python"][1] [![][2]][3]

[1]: https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white
[2]: https://img.shields.io/badge/python-3.9.6-blue.svg
[3]: https://www.python.org/downloads/release/python-396

> This script parses posts from your VK group and publishes them in the Telegram channel (text and photos).

## Install
```bash
git clone https://github.com/Moonquit/itcringebot.git
```

## Run (Basic)
* Install dependencies
```bash
pip install -r requirements.txt
```

* Configure `config.py`

* Run
```bash
python -m src
```

## Run (Docker)

* Create `.env` basic `.env.sample`

* Take VK and Telegram tokens

* Configure `.env`

* Run
```bash
docker-compose up -d
```

## Environment

* TG_TOKEN - Access token for telegram (XXX) 
* TG_CHANNEL - link to channel w/ at (@xxx)
* VK_TOKEN - Access token for VK (XXX)
* VK_API_VERSION - API Longpoll version (5.131)
