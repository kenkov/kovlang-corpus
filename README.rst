==============================
こふ語ｺｯﾊﾟｽｯ
==============================

こふ語ｺｯﾊﾟｽですっこふ語の解析にご利用くださいっ

::

    raw/kovlang.lst            ;生ｺｯﾊﾟｽｯ
    parsed/kovlang.parsed.lst  ;*.annot で訓練して tweets.lst を解析した解析済みｺｯﾊﾟｽｯ
    annot/*.annot              ;訓練用の部分的ｱﾉﾃｯｼｮﾝｺｯﾊﾟｽｯ
    keyword/keyword.lst        ;こふ語のうち比較的変わった使い方をする単語ﾘｽﾖｯ

部分的ｱﾉﾃｯｼｮﾝｺｰﾊﾟｽ `annot/*.annot` は `KyTea <http://www.phontron.com/kytea/index-ja.html>`_ 用のものですっこの部分的ｱﾉﾃｯｼｮﾝｺｰﾊﾟｽを利用して訓練した KyTea のモデルを使って
生ｺｯﾊﾟｽ `raw/kovlang.lst` を解析した結果が `parsed/kovlang.parsed.lst` です。

こふ語と思われる単語には、通常の品詞タグではなく **こふ語** という品詞タグをつけていますっ
