from PIL import Image, ImageDraw

def generate_table_on_a4():
    A4_WIDTH = int(210 * 74 / 25.4)
    A4_HEIGHT = int(297 * 74 / 25.4)

    CELL_SIZE = 44

    img = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
    draw = ImageDraw.Draw(img)

    #Draw the table
    for x in range(0, A4_WIDTH, CELL_SIZE):
        draw.line((x, 0, x, A4_HEIGHT), fill='RED')

    for y in range(0, A4_HEIGHT, CELL_SIZE):
        draw.line((0, y, A4_WIDTH, y), fill='RED')
    img.save('A4.png')

if __name__ == "__main__":
    generate_table_on_a4()
