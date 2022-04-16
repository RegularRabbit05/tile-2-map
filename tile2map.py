from PIL import Image

im = Image.open("tile.png")
re = Image.new('RGB', (1024, 1024), color = 'white')

relmax, relmay = im.size
relx, rely = 0, 0
width, height = re.size
for y in range(height):
    relx = 0
    for x in range(width):
        if relx == relmax:
            relx = 0
        pix = im.getpixel((relx,rely))
        re.putpixel([x, y], pix)
        relx+=1
    rely+=1
    if rely == relmay:
        rely = 0


re.save('map.png')
