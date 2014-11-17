PYTHON=python3

halfwidthkatakana:
	${PYTHON} scripts/extract_halfwidthkatakana.py <raw/raw.txt >keyword/halfwidthkatakana.txt
	sort keyword/halfwidthkatakana.txt | uniq | ${PYTHON} scripts/full2half.py >keyword/_full2half.txt
