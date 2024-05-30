import logging
import os
import sys
from dataclasses import dataclass
from os import path

from decouple import AutoConfig

local_dev_mode = path.exists(path.abspath('./settings.ini'))

user_home = path.expanduser('~/texttote')
pwd = './'
config_root: str = pwd if local_dev_mode else user_home

os.makedirs(config_root, exist_ok=True)
autoconfig = AutoConfig(search_path=config_root)


@dataclass
class AppConfig:
    db_path: str
    model_name: str
    model_vector_size: int
    log_level: str


config = AppConfig(
    db_path=path.abspath(
        path.expanduser(
            autoconfig('DB_PATH', default='~/texttote/texttote.db')
        )
    ),
    # TODO compare between msmarco-MiniLM-L-6-v3 and all-MiniLM-L6-v2
    # https://www.sbert.net/examples/applications/semantic-search/README.html#symmetric-vs-asymmetric-semantic-search
    # Model msmarco-MiniLM-L-6-v3 chosen because our queries are asymmetric queries
    model_name=autoconfig('MODEL_NAME', default='all-MiniLM-L6-v2'),
    model_vector_size=autoconfig('MODEL_VECTOR_SIZE', cast=int, default=384),
    log_level=autoconfig('LOG_LEVEL', default='INFO'),
)

# Configure logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

root.addHandler(handler)