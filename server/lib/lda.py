import re

from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel


def lda_action(common_texts):
    dictionary = Dictionary([common_texts])
    # LdaModelが読み込めるBoW形式に変換
    corpus = [dictionary.doc2bow(text) for text in [common_texts]]

    num_topics = 2
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, alpha=0.01, per_word_topics=True,  random_state = 1)

    topic_words = []
    for i in range(num_topics):
        tt = lda.get_topic_terms(i, 10)
        topic_words.append([dictionary[pair[0]] for pair in tt])

    result_topic = []
    for topic in topic_words:
        result_topic = result_topic + topic
    topics = list(dict.fromkeys(result_topic))

    result = []
    for topic in topics:
        if not bool(re.search(r'\d', topic)):
            result.append(topic)

    return result
