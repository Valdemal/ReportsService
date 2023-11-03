from django.conf import settings
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONTS_DIR = settings.STATIC_ROOT / 'fonts'

FONTS_MAP = {
    'Arial': 'arial.ttf',
    'ArialBd': 'arialbd.ttf',
    'ArialIt': 'ariali.ttf',
    'ArialBI': 'arialbi.ttf',
}


def load_fonts():
    for font_name in FONTS_MAP:
        font = str(FONTS_DIR / FONTS_MAP[font_name])
        pdfmetrics.registerFont(TTFont(font_name, font))
