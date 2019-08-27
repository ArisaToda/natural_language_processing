# natural_language_processing
自然言語処理

## 商品名の抽出：
csvファイルから商品名の文を取り出し、以下の条件を満たす物を商品名の候補として抽出した。
・名詞
・全てがカタカナ、ひらがな、漢字、アルファベットのどれか
・二文字以上

## 商品説明文：
csvファイルからPC商品説明文を取り出し、以下の条件を満たす物をその商品の特徴を表すKeywordの候補として抽出した。
・文章の中でどこかのchunkに掛かっている
・品詞が動詞、接頭詞、助詞で無い
・品詞の細分類(pos1)が非自立、副詞可能、数で無い
・二文字以上
