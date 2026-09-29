# -*- coding: utf-8 -*-
"""重畫 og.png（1200×630 社群預覽圖）。macOS 系統字體：宋體 TC、黑體 TC、Menlo。

python3 scripts/make_og.py
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1200, 630

BG = (244, 247, 251)
WHITE = (255, 255, 255)
INK = (30, 37, 48)
INK_SOFT = (92, 101, 119)
INK_FAINT = (124, 135, 151)
LINE = (230, 235, 242)
ACCENT = (59, 92, 140)
ACCENT_SOFT = (234, 240, 248)
RED = (194, 90, 80)

SONG = "/System/Library/Fonts/Supplemental/Songti.ttc"
HEI_M = "/System/Library/Fonts/STHeiti Medium.ttc"
HEI_L = "/System/Library/Fonts/STHeiti Light.ttc"
MONO = "/System/Library/Fonts/Menlo.ttc"


def f(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


song_b = lambda s: f(SONG, s, 2)   # Songti TC Bold
hei_m = lambda s: f(HEI_M, s, 0)   # Heiti TC Medium
hei_l = lambda s: f(HEI_L, s, 0)   # Heiti TC Light
mono = lambda s: f(MONO, s, 0)


def rounded(img, r):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, img.size[0], img.size[1]], r, fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def cover(img, w, h):
    s = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * s + 0.5), int(img.height * s + 0.5)), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def pill(d, x, y, text, font, fg, bg, padx=16, pady=8, r=999):
    tw = d.textlength(text, font=font)
    asc, desc = font.getmetrics()
    h = asc + desc + pady * 2
    d.rounded_rectangle([x, y, x + tw + padx * 2, y + h], min(r, h // 2), fill=bg)
    d.text((x + padx, y + pady), text, font=font, fill=fg)
    return x + tw + padx * 2, y + h


def main():
    canvas = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(canvas)

    # white card
    card = [40, 40, W - 40, H - 40]
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle([card[0], card[1] + 12, card[2], card[3] + 12], 36, fill=(59, 92, 140, 40))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(24)))
    d.rounded_rectangle(card, 36, fill=WHITE)

    # photo on the right
    px0, py0, px1, py1 = 700, 40, W - 40, H - 40
    photo = Image.open(os.path.join(ROOT, "img", "hero.jpg")).convert("RGB")
    photo = cover(photo, px1 - px0, py1 - py0)
    mask = Image.new("L", photo.size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([-40, 0, photo.size[0], photo.size[1]], 36, fill=255)
    md.rectangle([0, 0, 40, photo.size[1]], fill=255)
    canvas.paste(photo, (px0, py0), mask)

    # ticket card over the photo
    tx, ty, tw, th = 760, 292, 380, 246
    tshadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(tshadow).rounded_rectangle([tx, ty + 14, tx + tw, ty + th + 14], 22, fill=(30, 37, 48, 70))
    canvas.alpha_composite(tshadow.filter(ImageFilter.GaussianBlur(18)))
    d.rounded_rectangle([tx, ty, tx + tw, ty + th], 22, fill=WHITE)
    d.text((tx + 22, ty + 18), "雪國轉運站", font=hei_m(15), fill=INK_FAINT)
    d.text((tx + tw - 22 - d.textlength("2026–27", font=mono(15)), ty + 19), "2026–27", font=mono(15), fill=INK_FAINT)
    rows = [("主選", "GALA湯澤", ACCENT), ("主選", "輕井澤", ACCENT), ("不要", "八方尾根", RED)]
    ry = ty + 52
    for label, name, color in rows:
        d.line([tx + 22, ry, tx + tw - 22, ry], fill=LINE, width=2)
        pill(d, tx + 22, ry + 16, label, hei_m(15), WHITE, color, padx=10, pady=5, r=8)
        d.text((tx + 86, ry + 11), name, font=song_b(30), fill=INK)
        ry += 62

    # left copy
    x = 96
    pill(d, x, 96, "●  2026–27 雪季", hei_m(20), ACCENT, ACCENT_SOFT, padx=18, pady=9)
    d.text((x - 4, 160), "今年冬天，", font=song_b(84), fill=INK)
    d.text((x - 4, 262), "去哪滑？", font=song_b(84), fill=INK)
    d.text((x, 384), "從台灣出發、全繁中、四題給答案", font=hei_l(28), fill=INK_SOFT)

    # CTA button
    bx, by = x, 446
    btxt = "30 秒選場  →"
    bw = d.textlength(btxt, font=hei_m(30)) + 64
    d.rounded_rectangle([bx, by, bx + bw, by + 68], 34, fill=ACCENT)
    d.text((bx + 32, by + 14), btxt, font=hei_m(30), fill=WHITE)

    # brand footer
    d.text((x, 540), "雪國轉運站", font=song_b(26), fill=INK)
    d.text((x + 150, 546), "japanski.djhousetw.com", font=mono(18), fill=INK_FAINT)

    canvas.convert("RGB").save(os.path.join(ROOT, "og.png"), optimize=True)
    print("og.png", W, H)


if __name__ == "__main__":
    main()
