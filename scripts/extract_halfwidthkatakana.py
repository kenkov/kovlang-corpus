#! /usr/bin/env python
# coding:utf-8


import chartype


def extract(
        line: str) -> set:

    ch = chartype.Chartype()

    # add end symbol
    line = line + "E"
    length = len(line)
    ks = set()
    kflag = False
    curpos = 0
    endpos = 0

    for endpos in range(length):
        cond = ch.is_halfwidthkatakana(line[endpos])
        if kflag:
            if cond:
                kflag = True
            else:
                ks.add(line[curpos:endpos])
                kflag = False
                curpos = endpos + 1
        else:
            if cond:
                kflag = True
            else:
                curpos += 1
        endpos += 1

    return ks


if __name__ == '__main__':
    import sys
    ifd = open(sys.argv[1]) if len(sys.argv) >= 2 else sys.stdin

    for line in (_.rstrip() for _ in ifd):
        for x in extract(line):
            print(x)
