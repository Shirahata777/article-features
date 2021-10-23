from flask import Blueprint, request, jsonify
import urllib.parse

from lib.mecab.tokenize import *
from lib.normalization import *
from lib.lda import *
from lib.summary import *
from lib.password_checker import *


article_features_hander = Blueprint(
    'article_features', __name__, url_prefix='/lda')


@article_features_hander.route('', methods=['GET'])
def article_features():

    try:
        req = request.args
        text = urllib.parse.unquote(req.get("text"))

        text = normalization(text)

        lad_corpus = lda(text)
        summary_text = summary(text)

        result_list = {"topic": lad_corpus, "summary": summary_text}

        return jsonify(result_list)

    except:
        return jsonify(["分析できませんでした。もう一度入力し直してみてください！"]), 500


def lda(text):

    tokenize_texts = tokenize(text)

    lad_corpus = lda_action(tokenize_texts)

    return lad_corpus


def summary(text):
    summary_text = summary_action(text)

    return summary_text
