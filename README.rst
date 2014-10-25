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
        annot0.txt              ;訓練用の部分的ｱﾉﾃｯｼｮﾝｺｯﾊﾟｽｯ
    keyword/
        keyword.lst            ;こふ語のうち比較的変わった使い方をする単語ﾘｽﾖｯ

部分的ｱﾉﾃｯｼｮﾝｺｰﾊﾟｽ `annot.txt` は `KyTea <http://www.phontron.com/kytea/index-ja.html>`_ 用のものですっ
この部分的ｱﾉﾃｯｼｮﾝｺｰﾊﾟｽを利用して学習したこふ語の KyTea モデルを使って
生ｺｯﾊﾟｽ `raw/raw.txt` を解析した結果が `parsed/kovlang.parsed.txt` ですっ

実際にこふ語用の KyTea モデルを学習するには次のようにしますっ

.. code-block:: bash

    train-kytea -dictn 4 -charw 3 -charn 3 -typew 3 -typew 3 -global 1 \
        -feat kytea-0.4.2.feat \
        -part annot/preannot.txt \
        -part annot/annot.txt \
        -part annot/annot0.txt \
        -model kovlang.model

ここでは学習に `KyTea の素性ファイル <http://www.phontron.com/kytea/train-ja.html#feature>`_ を用いましたっ


こふ語と思われる単語には、通常の品詞タグではなく **こふ語** という品詞タグをつけていますっ
名前と思われる単語には、 **名前** タグをつけていますっ

