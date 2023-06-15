from typing import Tuple
from PIL import Image as PILImage, ImageFont, ImageDraw

def draw(elements, canvas):
    """ Draws the list of elements provided to a canvas """
    for element in elements:
        element.draw(canvas)

class Text(dict):
    def __init__(self, *arg, **kw) -> None:
        super(Text, self).__init__({**self.defaults(), **arg[0]}, **kw)

    def defaults(self):
        return {
            "anchor": "lt",
        }

    def draw(self, canvas) -> None:
        d = ImageDraw.Draw(canvas)
        d.text(
            self["pos"], 
            self["text"], 
            font=ImageFont.truetype(self["font"], self["size"]), 
            anchor=self["anchor"], 
            fill=self["color"],
        )

class TextBox(dict):
    def __init__(self, *arg, **kw) -> None:
        super(TextBox, self).__init__({**self.defaults(), **arg[0]}, **kw)

    def defaults(self):
        return {
            "offset": (0, 0),
        }

    def draw(self, canvas) -> None:
        text = self["text"]
        font = ImageFont.truetype(text["font"], text["size"])
        (left, top, right, bottom) = font.getbbox(text["text"])
        position = text["pos"]
        padding = self["padding"]
        offset = self["offset"]
        color = self["color"]
        d = ImageDraw.Draw(canvas)
        d.rectangle([
            position[0] - padding + offset[0], 
            position[1] - padding + offset[1], 
            right+position[0] + padding + offset[1],
            position[1]+bottom-top + padding + offset[1],
        ], color)
        self["text"].draw(canvas)


class Image(dict):
    def __init__(self, *arg, **kw) -> None:
        super(Image, self).__init__(*arg, **kw)

    def draw(self, canvas) -> None:
        canvas.paste(
            PILImage.open(self["path"]),
            self["pos"],
        )

class Canvas(dict):
    def __init__(self, 
        size: Tuple[int, int],
        color: Tuple[int, int, int], 
        out_path
    ) -> None:
        self.out_path = out_path
        self.im = PILImage.new("RGB", size, color)

    def draw(self, elements) -> None:
        for element in elements:
            element.draw(self.im)
        self.im.save(self.out_path)

FONT_PRIMARY = "/usr/share/texmf/fonts/opentype/public/lm/lmmonolt10-bold.otf"

Canvas((1200, 1200), (0,0,0), "out.png").draw([
    Image({
        "path": "julia_set.png",
        "pos": (-800, 0),
    }),
    Text({
        "text": "Welcome!",
        "font": FONT_PRIMARY,
        "pos": (600, 600),
        "size": 100,
        "anchor": "mm",
        "color": (200, 200, 200),
    }),
    TextBox({
        "color": (100, 50, 200),
        "padding": 15,
        "text": Text({
            "text": "Another!",
            "font": FONT_PRIMARY,
            "pos": (500, 800),
            "size": 100,
            "color": (255, 100, 100),
        }),
    })
])
