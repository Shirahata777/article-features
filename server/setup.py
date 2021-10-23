from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# MECAB設定
MECAB_DIC_URL = os.environ.get("MECAB_DIC_URL")


