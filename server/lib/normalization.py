import emoji
import re
from bs4 import BeautifulSoup


def normalization(text):
    text = "".join(text.splitlines())
    text = BeautifulSoup(text, 'html.parser').text
    text = re.sub(r'[^ ]+\.[^ ]+', '', text)
    # 絵文字を削除
    text = ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
    # 全角記号削除
    text = re.sub(r'[︰-＠]', '', text)
    # 半角記号削除
    # text = re.sub(re.compile("[!-/:-@[-`{-~]"), '', text)

    return text
