import os
from dataclasses import dataclass
from os import path

from decouple import AutoConfig

local_dev_settings_or_test_settings = path.abspath('./settings.ini')
user_home = path.expanduser('~/texttote')
config_root: str = './' if path.exists(local_dev_settings_or_test_settings) else user_home
os.makedirs(config_root, exist_ok=True)
config = AutoConfig(search_path=config_root)


@dataclass
class AppConfig:
    db_path: str


db_path = path.abspath(path.expanduser(config('DB_PATH', default='~/texttote/texttote.db')))

appconfig = AppConfig(
    db_path=db_path
)
