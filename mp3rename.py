#!/usr/bin/python3

# 在飞机上闲的没事干写一个去掉下载来的mp3前面的数字曲目编号的脚本
# By Noctoid - 2017/12/16
import os
import os.path
import sys
import argparse

target = "1 2 3 4 5 6 7 8 9 0 -".split()+[" "]

def list_audio(dirname):
    return [d for d in os.listdir(dirname) if is_audio(d)]

def is_audio(filename):
    return filename.split(".")[-1] in "mp3 wma m4a aiff aif flac".split()

def trim_filename(filename):
    if filename[0] in target:
        return trim_filename(filename[1:])
    else:
        return filename

def main(flags):
    original_list = []
    process_list = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d',
        type=str,
        default='.',
        help="""\
        Path to the directory that you want to change their names.\
        """
    )

    flags, unparsed = parser.parse_known_args()
    main(flags)
