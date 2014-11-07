PYTHON=python3

halfwidthkatakana:
	${PYTHON} scripts/extract_halfwidthkatakana.py <raw/raw.txt >keyword/halfwidthkatakana.txt
