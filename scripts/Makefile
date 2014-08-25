PYTHON = python3
PROJECT_PATH = ..
ANNOT_DIR = ${PROJECT_PATH}/annot
PARSED_TEXT_PATH = ${CORPUS_PATH}/parsed/tweets.parsed.lst

.PHONY: clean

init:
	if [ ! -d ${ANNOT_DIR} ]; then mkdir ${ANNOT_DIR} && ${PYTHON} initkytea.py > ${ANNOT_DIR}/1-1000.annot; fi
