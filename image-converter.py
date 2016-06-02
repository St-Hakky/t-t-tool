#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os, re, sys

def returnFormat(format):
    if format == "bmp":
        return "BMP"
    elif format == "jpg":
        return "JPEG"
    elif format == "png":
        return "PNG"
    elif format == "gif":
        return "GIF"
    else:
        print(format + " は対応していません。")
        sys.exit()

if __name__ == '__main__':
    if len(sys.argv) > 4:
        fileName = sys.argv[1]
        format = sys.argv[2]

        img = Image.open(fileName, "r")
        width, height = img.size

        fileName = re.search("(?<!\.)\w+", fileName).group(0) + "." + format

        flag = os.path.exists(fileName)
        if flag == True:
            print("That file already exists")
            sys.exit()
            
        canvas = Image.new("RGB", (width, height), (255, 255, 255))
        canvas.paste(img, (0, 0))

        canvas.save(fileName, returnFormat(format), quality=100, optimize=True)

    else:
        print("引数が少なすぎます。\nファイル名と変換するファイルの形式を指定子て下さい。\
            \n※フォーマットは小文字で指定して下さい。\
            \n例) python imgf.py fileName.jpg bmp 100 100")
