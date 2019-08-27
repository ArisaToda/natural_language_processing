import pandas as pd
import Dependency_analysis as dep
import preprocessor as pro

df = pd.read_csv('inputs/disney.csv', encoding='SHIFT-JIS')

discs = df['PC用商品説明文'].iloc[:100]
discs = discs.rename(columns={'PC用商品説明文': '商品説明文のKeyWords'})

names = df['商品名'].iloc[:100]
names = names.rename(columns={'商品名': '商品名の候補'})


# 商品名に含まれている名詞を抽出
names = names.apply(pro.all_processor)
only_noun = names.apply(dep.get_noun)


# 商品説明文に含まれるKeywordsを抽出
target_words = discs.apply(dep.get_target_words)

for line in target_words:
    print(line)


df_parsed = pd.concat([df, only_noun, target_words], axis=1)
df_parsed.to_csv('outputs/disney_parsed.csv')
