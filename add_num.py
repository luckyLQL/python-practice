# coding: utf-8
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

im = PIL.Image.open('pic.jpg')
draw = PIL.ImageDraw.Draw(im)
fontsize = PIL.ImageFont.truetype('arial.ttf',20)
draw.text((270,0),"4",fill=(255,0,0),font=fontsize)
im.save("red.jpg")
im.show()


