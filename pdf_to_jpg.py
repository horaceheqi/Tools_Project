import fitz

pdf = fitz.open('./image/1.pdf')
for pg in range(0, 1):
    page = pdf[pg]
    rotate = int(0)
    zoom_x = 2.0
    zoom_y = 2.0
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    pm.writePNG('./image/%s.png' % 1)