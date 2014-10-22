==============================
こふ語ｺｯﾊﾟｽｯ
==============================

こふ語ｺｯﾊﾟｽですっこふ語の解析にご利用くださいっ

::

    raw/
        raw.txt                ;生ｺｯﾊﾟｽｯ
    parsed/
        kovlang.parsed.txt     ;annot.txt で KyTea を訓練して raw.txt を解析した解析済みｺｯﾊﾟｽｯ
    annot/
        preannot.txt           ;raw.txt を KyTea ｺｯﾊﾟｽ用に変換したもの (ｽﾍﾟｯｽの挿入とｴｽｹｯﾌﾟ)
        annot.txt              ;訓練用の部分的ｱﾉﾃｯｼｮﾝｺｯﾊﾟｽｯ
    keyword/
        keyword.lst            ;こふ語のうち比較的変わった使い方をする単語ﾘｽﾖｯ

部分的ｱﾉﾃｯｼｮﾝｺｰﾊﾟｽ `annot.txt` は `KyTea <http://www.phontron.com/kytea/index-ja.html>`_ 用のものですっこの部分的ｱﾉﾃｯｼｮﾝｺｰﾊﾟｽを利用して訓練した KyTea のモデルを使って
生ｺｯﾊﾟｽ `raw/raw.txt` を解析した結果が `parsed/kovlang.parsed.txt` です。

こふ語と思われる単語には、通常の品詞タグではなく **こふ語** という品詞タグをつけていますっ

名前と思われる単語には、 **名前** タグをつけています。
