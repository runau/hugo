from PIL import ImageFont, ImageDraw, Image
import sys
import yaml
import re


def add_text_to_image(img, base_text, font_path, font_size, font_color, height, width, line=1, max_length=800, max_height=420):
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    lineCnt = 1
    base_text = base_text.strip()
    base_text = base_text.replace("\n\n", "\n")
    base_text = re.sub('\!\[.+\]','',base_text)
    base_text = base_text.replace("[", "")
    base_text = base_text.replace("]", "")
    base_text = re.sub('\(.+\)','',base_text)
    base_text = base_text[0:150]
    break_flg = False
    for lineCnt in range(line):
        text = base_text.split("\n")[0]
        position = (width, height)
        if len(text) == 0:
            break
        if lineCnt == line - 1 or \
                height + draw.textsize(text, font=font)[1] > max_height:
            if draw.textsize(text, font=font)[0] > max_length:
                # テキストの長さがmax_lengthより小さくなるまで、1文字ずつ削っていく
                while draw.textsize(text + '…', font=font)[0] > max_length:
                    text = text[:-1]
                text = text + '…'
                break_flg = True
        else:
            while draw.textsize(text, font=font)[0] > max_length:
                text = text[:-1]
        base_text = base_text.replace(text, "")
        base_text = base_text.strip()
        height = height + draw.textsize(text, font=font)[1]
        draw.text(position, text, font_color, font=font)
        print(f"draw:{text}")
        if break_flg:
            break

    return img, height


target = sys.argv[1]
print(f"target:{target}")

target = target.split("/")[-1]
target = target.replace(".md","")

with open(f'content/posts/{target}.md') as f:
    md = f.read().split("---")
    header_yaml = md[1]
    body = md[2]
    header = yaml.load(header_yaml)
    title = header["title"]

base_img_path = "content/posts/meta_image/base.png"
base_img = Image.open(base_img_path).copy()
font_path = "content/posts/meta_image/meiryo.ttc"
font_color = (88, 110, 117)
height = 155
width = 30

font_size = 57
line = 3
img, height = add_text_to_image(
    base_img, title, font_path, font_size, font_color, height, width, line)

font_size = 35
height = height + 20
line = 6
img, height = add_text_to_image(
    img, body, font_path, font_size, font_color, height, width, line)
img.save(f"content/posts/meta_image/{target}.png")
