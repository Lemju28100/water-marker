from os import waitpid
from kivy.app import App
from page_controller import PageController


page_controller = PageController()

class WaterMarkApp(App):
    def build(self):
        return page_controller

if __name__ == '__main__':
    WaterMarkApp().run()

# from PIL import Image
# from PIL import ImageDraw
# import os
# from kivy.core.text import LabelBase


# current_dir = f'{os.getcwd()}/users/kathy/watermarks'
# img1 = Image.open(fp=f'{current_dir}/test1.png')
# img2 = Image.open(fp=f'{current_dir}/test2.png')

# resized_img1 = img1.thumbnail((img1.size[0]/5, img1.size[1]/5))

# img2.paste(img1, (0, 0), img1)
# img2.show()

# LabelBase.register(name="OpenSans", fn_regular="OpenSans-Regular.ttf", fn_bold="OpenSans-Bold.ttf", fn_bolditalic="OpenSans-BoldItalic.ttf")

# img = Image.new('RGB', (200, 100))
# d = ImageDraw.Draw(img)
# d.text((20, 20), 'Hello', fill=(255, 0, 0))
# img.show()

