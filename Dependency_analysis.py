import CaboCha
from collections import Counter

# 商品名から名詞を抽出
def get_noun(sentence):
    """
    get every nouns from sentence.
    """
    c = CaboCha.Parser("mecab-ipadic-neologd")
    tree = c.parse(str(sentence))

    # chunkId: sentenceの中で何番目のチャンクにあたるか
    chunkId = 0

    # targertId:　targert_wordのchunkId
    targetId = []

    for i in range(tree.size()):
        token = tree.token(i)
        feature = token.feature.strip().split(',')
        hinshi = feature[0]
        if hinshi == '名詞':
            targetId.append(chunkId)
        chunkId += 1

    target_word = []
    for _ in targetId:
        for i in range(tree.size()):
            token = tree.token(i)
            feature = token.feature.strip().split(',')
            genkei = feature[6]
            if genkei.isalpha() and not len(genkei) < 2:
                target_word.append(genkei)
    words = set(target_word)
    return words


# def counter_noun(text):
#     """
#     よく繰り返される名詞をtextの中から上位三つ取り出す（商品名の候補）
#     """
#
#     mycounter = Counter(text)
#     return mycounter.most_common(1)


# 商品説明文からKeywordsの抽出
def get_target_words(sentence):
    """
    get target words(list) from sentence.
    """
    c = CaboCha.Parser("mecab-ipadic-neologd")
    tree = c.parse(str(sentence))

    # chunkId: sentenceの中で何番目のチャンクにあたるか
    chunkId = 0

    # targertId:　targert_wordのchunkId
    targetId = []

    for i in range(tree.size()):
        token = tree.token(i)
        if token.chunk != None:
            # print(chunkId, token.chunk.link, token.chunk.head_pos,
            # token.chunk.func_pos, token.chunk.score)
            if token.chunk.link != -1:  # かかり先が無い場合link=-1
                targetId.append(chunkId)
        chunkId += 1

    target_word = []
    for _ in targetId:
        for i in range(tree.size()):
            token = tree.token(i)
            feature = token.feature.strip().split(',')
            genkei = feature[6]
            hinshi = feature[0]
            pos1 = feature[1]

            if i in targetId \
                    and genkei.isalpha() \
                    and not hinshi == '動詞' and '接頭詞' and '助詞' \
                    and not pos1 == '非自立' and '副詞可能' and '数' \
                    and not len(genkei) < 2:
                target_word.append(genkei)
    words = set(target_word)
    return words



