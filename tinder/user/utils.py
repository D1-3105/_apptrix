from PIL import Image
from django.conf import settings

def edit_avatar(img_base):
    img = Image.open(img_base, 'r').convert("RGBA")
    watermark = Image.open(settings.MEDIA['WATERMARKS']/'watermark4reg.png')
    watermark.putalpha(127)
    watermark.convert('RGBA')
    width, height = img.size
    width_watermark, height_watermark= watermark.size
    if width>width_watermark or height>height_watermark:
        raise ValueError(u'YOUR IMAGE IS TOO SMALL! IT SHOULD BE {}x{}pix'
                         .format(width_watermark*2, height_watermark*2))
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(img, (0, 0))
    transparent.paste(watermark, (width-width_watermark, height-height_watermark), mask=watermark)
    transparent.save(img_base)
