import MeCab
import setup

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def summary_action(text):

    tagger = MeCab.Tagger(setup.MECAB_DIC_URL)
    key = tagger.parse(text)
    corpus = []
    for row in key.split("\n"):
        word = row.split("\t")[0]
        if word == "EOS":
            break
        else:
            corpus.append(word)

    parser = PlaintextParser.from_string(text, Tokenizer('japanese'))

    summarizer = LexRankSummarizer()
    summarizer.stop_words = [' ']

    summary = summarizer(document=parser.document, sentences_count=3)
    b = []
    for sentence in summary:
        b.append(sentence.__str__())

    if str(''.join(b)) == "":
        b = ""
    return ''.join(b)