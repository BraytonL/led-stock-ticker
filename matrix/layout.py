from dataclasses import dataclass, field

from PIL import ImageFont

from constants import LAYOUT_FILE
from util.utils import read_json, load_font


@dataclass
class Layout:
    """Matrix Layout class"""
    width: int
    height: int
    coords: dict = field(default_factory=dict)
    font: ImageFont = None
    clock_font: ImageFont = None
    show_logos: bool = False

    def __post_init__(self):
        self.coords = read_json(LAYOUT_FILE.format(self.width, self.height))
        self.font = load_font(self.coords['fonts']['primary'])
        clock_font = self.coords.get('fonts').get('clock', None)
        self.clock_font = load_font(clock_font) if clock_font else self.font
        self.show_logos = False
