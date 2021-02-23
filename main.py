from os import waitpid
from kivy.app import App
from page_controller import PageController
from kivy.config import Config
import os



page_controller = PageController()


class WaterMarkApp(App):
    def build(self):
        self.icon = 'data/logo.png'
        return page_controller

    def on_stop(self):
        temp_dir = f'{os.getcwd()}/temp'
        for file in os.listdir(temp_dir):
            os.remove(f'{temp_dir}/{file}')
        return super().on_stop()

if __name__ == '__main__':
    WaterMarkApp().run()

# from PIL import Image
# from PIL import ImageDraw
# import os
# from kivy.core.text import LabelBase
# from tkinter import filedialog
# import tkinter as tk


# current_dir = f'{os.getcwd()}/users/kathy/watermarks'
# img1 = Image.open(fp=f'{current_dir}/test1.png')
# img2 = Image.open(fp=f'{current_dir}/test2.png')

# resized_img1 = img1.thumbnail((img1.size[0]/5, img1.size[1]/5))

# img2.paste(img1, (0, 0), img1)
# root = tk.Tk()
# files = [('PNG Image', '*.png'), ('JPEG Image', '*.jpeg')] 
# f = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
# img2.save(fp=f.name)


# img2.show()

# LabelBase.register(name="OpenSans", fn_regular="OpenSans-Regular.ttf", fn_bold="OpenSans-Bold.ttf", fn_bolditalic="OpenSans-BoldItalic.ttf")

# img = Image.new('RGB', (200, 100))
# d = ImageDraw.Draw(img)
# d.text((20, 20), 'Hello', fill=(255, 0, 0))
# img.show()

# import datetime

# date_to_save = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')
# d = datetime.datetime(date_to_save)
# print(date_to_save)
# print(d)
# print(datetime.datetime.no)

# import json
# import os
# import datetime






# # watermark_details = {
# #     "data": [{"path": "dksal", "date": f"{datetime.datetime.now()}"}, {"path":"asdklf", "date": f"{datetime.datetime.now() - datetime.timedelta(days=1)}"}]
# # }



# # with open('data/save_watermark_data.json', "w") as outfile:
# #     json.dump(watermark_details, outfile)

# # with open('data/save_watermark_data.json') as outfile:
# #     json_object = json.load(outfile)
# #     print(json_object)


# # now = datetime.datetime.now()

# # def convert_to_date(self, watermark_date):
    
# #     year_month_date = watermark_date.split(' ')[0].split('-')
# #     year=int(year_month_date[0])
# #     month=int(year_month_date[1])
# #     day = int(year_month_date[2])
# #     hour_minute_second = watermark_date.split(' ')[1].split(':')
# #     hour = hour_minute_second[0]
# #     minute = hour_minute_second[1]
# #     second = hour_minute_second[2].split('.')[0]
# #     date_saved = datetime.datetime(year, month, day, hour, minute, second)
# #     return date_saved

# a = datetime.datetime.now()
# b = datetime.datetime.now() - datetime.timedelta(days=1)
# c = [a, b]




