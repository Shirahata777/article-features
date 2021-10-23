import MeCab
import setup


def tokenize(text):

    tagger = MeCab.Tagger(setup.MECAB_DIC_URL)

    key = tagger.parse(text)
    tokenize_texts = []
    for row in key.split("\n"):
        word = row.split("\t")[0]
        if word == "EOS":
            break
        else:
            pos = row.split("\t")[1]
            slice = pos.split(",")
            if len(word) > 2:
                if slice[0] == "名詞" and slice[1] == "固有名詞":
                    tokenize_texts.append(word)

    return tokenize_texts
