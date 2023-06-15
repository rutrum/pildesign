from PIL import Image, ImageFont, ImageDraw

SIZE = (1200, 1200)
HEIGHT, WIDTH = SIZE

FONT_PRIMARY = "/usr/share/texmf/fonts/opentype/public/lm/lmmonolt10-bold.otf"
FONT_SECONDARY = "/usr/share/texmf/fonts/opentype/public/lm/lmmonolt10-oblique.otf"
FONT_2 = ""

COLOR_0 = (0, 0, 0)
COLOR_1 = (255, 228, 153)

def font(name, size=20):
    return ImageFont.truetype(name, size)

def text_box(d, text, font, position, padding, box_color, text_color, box_offset=(0, 0)):
    (left, top, right, bottom) = font.getbbox(text)
    d.rectangle([
        position[0] - padding + box_offset[0], 
        position[1] - padding + box_offset[1], 
        right+position[0] + padding + box_offset[1],
        position[1]+bottom-top + padding + box_offset[1],
    ], box_color)
    d.text(position, text, font=font, anchor="lt", fill=text_color)

def main():
    out = Image.new("RGB", (1200, 1200), COLOR_0)
    
    # setbackgroun
    bg = Image.open("julia_set.png")
    out.paste(bg, (-700,0))

    d = ImageDraw.Draw(out)

    title_pos = (100,220)

    text_box(d, "Euchre", font(FONT_PRIMARY, 120), title_pos, padding=30, box_color=COLOR_1, text_color=COLOR_0)
    text_box(d, "at Dave and Rachel's", font(FONT_SECONDARY, 60), (title_pos[0]-30, 120+title_pos[1]), padding=20, box_color=COLOR_1, text_color=COLOR_0, box_offset=(0, -5))

    time_pos = (600, 100)

    text_box(d, "3pm start", font(FONT_PRIMARY, 60), (time_pos[0]+40, 70+time_pos[1]), padding=20, box_color=COLOR_1, text_color=COLOR_0, box_offset=(0, -5))
    text_box(d, "Saturday June 17", font(FONT_SECONDARY, 60), time_pos, padding=20, box_color=COLOR_1, text_color=COLOR_0, box_offset=(0, -5))

    guest_pos = (500, 500)

    text_box(d, "with special guest", font(FONT_SECONDARY, 60), guest_pos, padding=15, box_color=COLOR_1, text_color=COLOR_0, box_offset=(0, -5))
    text_box(d, "Ryan Graham", font(FONT_PRIMARY, 60), (50+guest_pos[0], 70+guest_pos[1]), padding=15, box_color=COLOR_1, text_color=COLOR_0, box_offset=(0, -5))

    bring_pos = (60, 510)

    d.text(bring_pos, "You Bring", font=font(FONT_PRIMARY, 50), anchor="lt", fill=COLOR_1)
    d.text((40+bring_pos[0], 50+bring_pos[1]), "$5", font=font(FONT_PRIMARY, 150), anchor="lt", fill=COLOR_1)

    d.text((60, 750), "You Get", font=font(FONT_PRIMARY, 50), anchor="lt", fill=COLOR_1)
    d.text((330, 857), "(not forever)", font=font(FONT_SECONDARY, 20), anchor="lt", fill=COLOR_1)
    d.multiline_text((100, 780), "free snacks\na partner\nthe chance to win it all!\nthe chance to win $5!", font=font(FONT_SECONDARY, 45), fill=COLOR_1)

    text_box(d, "Tell Dave if you're coming!", font(FONT_PRIMARY, 60), (180, 1100), padding=15, box_color=COLOR_1, text_color=COLOR_0, box_offset=(0, -5))

    out.save("out.png")

if __name__ == "__main__":
    main()
