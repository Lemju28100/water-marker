from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.uix.slider import Slider
import json

from kivy.uix.scrollview import ScrollView
import numpy as np
import cv2


from datetime import datetime

import tkinter as tk
from tkinter import filedialog

from PIL import Image as Im

from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image
from kivy.uix.popup import Popup


from functools import partial
from PIL import ImageChops

import os


class EditorPage(Screen):
    def __init__(self, page_controller, user, img_url, **kw):
        super().__init__(**kw)

        #TODO set self.user back to user
        self.user = user
        self.save_counter = 0
        self.number_of_times_image_edited =0
        self.temp_dir = f'{os.getcwd()}/temp'

        self.img_dir = f'{os.getcwd()}/users/{self.user}/images'
        self.watermark_dir = f'{os.getcwd()}/users/{self.user}/watermarks'

        #TODO set self.img_url back to img_url
        self.img_url = img_url

        self.watermark_path = f'{os.getcwd()}/users/{self.user}/watermarks'
        self.watermark_position = (0, 0)

        self.bg_image = Image(source='data/home_background.png', allow_stretch=True,
        keep_ratio = False)
        self.add_widget(self.bg_image)

        self.root_layout = BoxLayout(orientation='horizontal')
        self.root_layout.padding = 20
        self.root_layout.spacing = 50

        self.generate_recent_watermarks()
        self.generate_editing_box()
        self.generate_share_box(page_controller=page_controller)
        self.add_widget(self.root_layout)

    def generate_recent_watermarks(self):
        recent_watermark_box = BoxLayout(orientation='vertical', size_hint=(.15, 1), spacing=20)
        recent_watermark_label = Label(text='RECENT WATERMARKS', size_hint = (1, .4), font_size=15)
        recent_watermark_box.add_widget(recent_watermark_label)

        watermark_dir = os.listdir(self.watermark_path)
        
        for i in range(len(watermark_dir)):
            watermark_source =f'{self.watermark_path}/{watermark_dir[i]}'
            water_image_button = Button(background_normal=watermark_source, size_hint=(1, 1), on_release=self.generate_editor)
            if i == 3:
                break


            recent_watermark_box.add_widget(water_image_button)
        
        self.root_layout.add_widget(recent_watermark_box)

    
    def generate_editing_box(self):
        editing_box = BoxLayout(orientation='vertical', size_hint=(.4, 1), spacing=5)
        editing_button_box = BoxLayout(orientation='horizontal', spacing=3, size_hint=(1, .1), pos_hint={'x': 0, 'y': 0})

        # add_text_button = Button(text=' ADD \n\nTEXT', font_size=15, size_hint=(1, 1))
        self.add_watermark_button = Button(text='ADD WATERMARK', font_size=15, size_hint=(1, 1), on_release=self.generate_editor)
        # delete_watermark_button = Button(text='    DELETE \n\nWATERMARK', font_size=15, size_hint=(1, 1))

        # editing_button_box.add_widget(add_text_button)
        editing_button_box.add_widget(self.add_watermark_button)
        # editing_button_box.add_widget(delete_watermark_button)

        image_box = BoxLayout(orientation='vertical', size_hint=(1, .7))
        self.user_image = Image(source=self.img_url, allow_stretch=False, keep_ratio=True)
        image_box.add_widget(self.user_image)

        editing_box.add_widget(editing_button_box)
        editing_box.add_widget(image_box)

        self.root_layout.add_widget(editing_box)

    def generate_share_box(self, page_controller):
        share_box = BoxLayout(orientation='vertical', size_hint=(.15, 1), spacing=5)


        view_recents_button = Button(text="VIEW RECENTS", font_size=15, size_hint=(1, .1), on_release=partial(self.view_recents, page_controller))
        empty_space = BoxLayout(orientation='vertical', size_hint=(1, .3))
        self.save_button = Button(text='SAVE', font_size=15, size_hint=(1, .1), on_release=self.save_rendered_image, disabled=True)
        self.save_as_button = Button(text='SAVE AS', font_size=15, size_hint=(1, .1), on_release=self.save_rendered_image_as, disabled = True)
        empty_space2 = BoxLayout(orientation='vertical', size_hint=(1, .3))
        back_button = Button(text='BACK', font_size=15, size_hint=(1, .1), on_release=partial(self.return_to_homepage, page_controller))

        share_box.add_widget(view_recents_button)
        share_box.add_widget(empty_space)
        share_box.add_widget(self.save_button)
        share_box.add_widget(self.save_as_button)
        share_box.add_widget(empty_space2)
        share_box.add_widget(back_button)

        self.root_layout.add_widget(share_box)


    def generate_editor(self, button):

        if button.text == 'ADD WATERMARK':

            image_is_uploaded = False
            root = tk.Tk()
            root.withdraw()
            self.marker_path = filedialog.askopenfilename()

        else:
            self.marker_path = button.background_normal


        self.editor_box_popup = Popup(title='EDIT IMAGE')

        editor_box_content_box = BoxLayout(orientation="horizontal", size_hint=(1, 1), spacing=20)

        self.image_render_box = BoxLayout(orientation='horizontal', size_hint=(0.5, 1))
        self.rendered_image = Image(source='data/home_background.png', allow_stretch=True,
        keep_ratio = False)
        # TODO call render_image function to change the source of the rendered image
        

        self.image_render_box.add_widget(self.rendered_image)
        editor_box_content_box.add_widget(self.image_render_box)



        

        config_box = BoxLayout(size_hint=(.4, 1))



        # config_page = PageLayout(swipe_threshold=.2)
        # text_config_box = BoxLayout(orientation='vertical', size_hint=(1, 1))

        # enter_text_entry = TextInput(size_hint=(1, .2), font_size=25, hint_text='Enter Text')
        # text_config_box.add_widget(enter_text_entry)

        # font_dropdown = DropDown(size_hint=(1, .2))
        # font_dropdown.add_widget(Label(text='test'))
        # text_config_box.add_widget(font_dropdown)

        # color_picker_box = BoxLayout(orientation='vertical')
        # # color_picker_label = Label(text='Text Color: ', font_size=15)
        # color_popup = ColorPicker()
        # # color_picker_box.add_widget(color_picker_label)
        # color_picker_box.add_widget(color_popup)
        # text_config_box.add_widget(color_picker_box)

        # text_mode_box = BoxLayout(orientation='horizontal')
        # italic_button = Button(text='[i]I[/i]', font_size=15, markup=True)
        # bold_button = Button(text='[b]B[/b]', font_size=15, markup=True)
        # underline_button = Button(text='[u]U[/u]', font_size=15, markup=True)
        # strikethrough_button = Button(text='[s]S[/s]', font_size=15, markup=True)
        # text_mode_box.add_widget(italic_button)
        # text_mode_box.add_widget(bold_button)
        # text_mode_box.add_widget(underline_button)
        # text_mode_box.add_widget(strikethrough_button)
        # text_config_box.add_widget(text_mode_box)


        # font_size_box = BoxLayout(orientation='horizontal')
        # font_size_label = Label(text='Font Size: ')
        # font_size_dropdown = DropDown()

        # font_size_dropdown.add_widget(font_size_label)
        # font_size_dropdown.select(font_size_label)

        # font_size_box.add_widget(font_size_label)
        # font_size_box.add_widget(font_size_dropdown)
        # text_config_box.add_widget(font_size_box)

        # config_box.add_widget(text_config_box)






        watermark_config_box = BoxLayout(orientation='vertical', size_hint=(1, 1))

        position_label = Label(text='Watermark Position', font_size=15)
        watermark_config_box.add_widget(position_label)

        watermark_position_grid = GridLayout(rows=3, size_hint=(1, 3))
        
        self.watermark_position_button_names = [i.capitalize() for i in ['Top Left', 'Top middle', 'top right', 'left', 'middle', 'right', 'bottom left', 'bottom middle', 'bottom right']]
        for position in self.watermark_position_button_names:
            position_button = Button(text=position.capitalize(), font_size=12, on_release=self.render_image)
            watermark_position_grid.add_widget(position_button)

        watermark_config_box.add_widget(watermark_position_grid)

        space2 = BoxLayout(orientation='vertical')
        watermark_config_box.add_widget(space2)

        opacity_label = Label(text='opacity')
        self.opacity_slider = Slider(min=1, max=10, step=1, value=10)
        watermark_config_box.add_widget(opacity_label)
        watermark_config_box.add_widget(self.opacity_slider)
        self.opacity_slider.bind(value=self.render_image)

        rotation_label = Label(text='rotation')
        self.rotation_slider = Slider(min=0, max=270, step=10)
        watermark_config_box.add_widget(rotation_label)
        watermark_config_box.add_widget(self.rotation_slider)
        self.rotation_slider.bind(value=self.render_image)

        size_label = Label(text='size')
        self.size_slider = Slider(min=1, max=10, step=1, value=4)
        watermark_config_box.add_widget(size_label)
        watermark_config_box.add_widget(self.size_slider)
        self.size_slider.bind(value=self.render_image)

        up_arrow_spacing = BoxLayout(orientation='vertical')
        watermark_config_box.add_widget(up_arrow_spacing)

        move_up_button = Button(text='up', size_hint=(.3, 1), pos_hint={'x':.35, 'y':0}, on_release=self.render_image)
        watermark_config_box.add_widget(move_up_button)

        move_left_and_right_box = BoxLayout(orientation='horizontal')
        move_left_button = Button(text='left', on_release=self.render_image)
        move_label = Label(text='move', font_size=15)
        move_right_button = Button(text='right', on_release=self.render_image)
        move_left_and_right_box.add_widget(move_left_button)
        move_left_and_right_box.add_widget(move_label)
        move_left_and_right_box.add_widget(move_right_button)
        watermark_config_box.add_widget(move_left_and_right_box)

        move_down_button = Button(text='down', size_hint=(.3, 1), pos_hint={'x':.35, 'y':0}, on_release=self.render_image)
        watermark_config_box.add_widget(move_down_button)

        done_button_spacing = BoxLayout(orientation='horizontal')
        watermark_config_box.add_widget(done_button_spacing)

        done_button = Button(text='DONE', font_size=15, on_release=self.render_image)
        watermark_config_box.add_widget(done_button)

        config_box.add_widget(watermark_config_box)



        editor_box_content_box.add_widget(config_box)

        

        supported_image_extensions = ['jpg', 'jpeg', 'png']

        for extension in supported_image_extensions:
            if str(self.marker_path).endswith(extension):
                image_is_uploaded = True


        if self.marker_path == '':
            return

        if image_is_uploaded:
            self.editor_box_popup.content = editor_box_content_box
            self.editor_box_popup.open()
            self.render_image()
            

        else:
        
            warning_popup = Popup(title='Photo not Entered', size_hint=(0.5, 0.5))
                

            warning_content= BoxLayout(orientation='vertical', size_hint=(.9, .9), spacing=10, pos_hint={'x':.4, 'y':0})
            warning_label = Label(text='Please choose a photo', font_size=16, size_hint=(.9, .2))
            ok_button = Button(text='OK', size_hint= (.9, .1), on_release=warning_popup.dismiss)

            warning_content.add_widget(warning_label)
            warning_content.add_widget(ok_button)
            warning_popup.add_widget(warning_content)
            warning_popup.open()
 
        

    



    def view_recents(self, controller, event):
        controller.initialize_recents_page()
        self.delete_temp_files()


    def render_image(self, button='a', b='b'):
        self.main_image = Im.open(self.img_url)
        watermark = Im.open(self.marker_path)

        main_image_x_size = self.main_image.size[0]
        main_image_y_size = self.main_image.size[1]

                
        rotation_value = self.rotation_slider.value
        size_multiplier = self.size_slider.value
        opacity_multiplier = self.opacity_slider.value

        watermark_x_size = int(watermark.size[0]/20 * size_multiplier)
        watermark_y_size = int(watermark.size[1]/20 * size_multiplier)

        watermark_positions = {
            'Top left': (0, 0), 'Top middle': (int(main_image_x_size/2) - int(watermark_x_size/2), 0), 'Top right': (main_image_x_size - watermark_x_size, 0),
            'Left': (0, int(main_image_y_size/2) - int(watermark_y_size/2)), 'Middle': (int(main_image_x_size/2) - int(watermark_x_size/2), int(main_image_y_size/2)-int(watermark_y_size/2)), 'Right': (main_image_x_size - watermark_x_size, int(main_image_y_size/2)-int(watermark_y_size/2)),
            'Bottom left': (0, main_image_y_size-watermark_y_size), 'Bottom middle': (int(main_image_x_size/2) - int(watermark_x_size/2), main_image_y_size - watermark_y_size), 'Bottom right':(main_image_x_size - watermark_x_size, main_image_y_size - watermark_y_size)
            }

        # Position the image
        # Loop through all the other children in parent and enable them

        move_step = int(main_image_x_size/40)
        if type(button) == Button:
            print(button.parent)
            if type(button.parent) == GridLayout:

            # for butt in button.parent.children:
            #     butt.enabled = True
            #     button.parent._trigger_layout()
            #     print(butt.enabled)
                self.watermark_position = watermark_positions[button.text]
            else:
                if button.text == 'up':
                    self.watermark_position = (self.watermark_position[0], self.watermark_position[1] - move_step)
                elif button.text == 'down':
                    self.watermark_position = (self.watermark_position[0], self.watermark_position[1] + move_step)
                elif button.text == 'left':
                    self.watermark_position = (self.watermark_position[0] - move_step, self.watermark_position[1])
                elif button.text == 'right':
                    self.watermark_position = (self.watermark_position[0] + move_step, self.watermark_position[1])
                else:
                    self.editor_box_popup.dismiss()
                    self.user_image.source = self.rendered_image.source
                    self.main_image = Im.open(fp=self.user_image.source)
                    self.add_watermark_button.disabled = True
                    self.save_as_button.disabled = False
                    self.save_button.disabled = False
                    self.used_watermark = self.rotated_image

            
            



        # disable clicked button with different color
        # get the text of the clicked button
        # Depending on the text, place the marker on the image



        self.img_format = self.main_image.format
        
        watermark.thumbnail((watermark_x_size, watermark_y_size))
        watermark.putalpha(int(25.5 * opacity_multiplier))

        self.rotated_image = watermark.rotate(rotation_value, expand=1)
        self.main_image.paste(self.rotated_image, self.watermark_position, self.rotated_image)

        save_source = f'temp/temp_img{self.save_counter}.{self.img_format}'
        

        self.main_image.save(save_source)

        self.rendered_image.source = save_source

        if self.save_counter > 1:
            os.remove(f'temp/temp_img{self.save_counter - 1}.{self.img_format}')

        self.save_counter += 1
        self.main_image.close()
        watermark.close()

        
    def save_rendered_image(self, e):
        now_date = datetime.now()
        date_to_save = now_date.strftime('%b-%d-%I%M%p-%G')

        image_to_save = Im.open(self.rendered_image.source)
        fp_to_save = f'{os.getcwd()}/users/{self.user}/images/{date_to_save}.{self.img_format}'

        # for image in os.listdir(self.img_dir):
        #     saved_image_path = f'{self.img_dir}/{image}'
        #     saved_images = Im.open(saved_image_path)

            # if self.image_is_same(saved_image_path, self.rendered_image.source):
            #     image_to_save.show()
            #     saved_images.show()
            #     saved_popup = Popup(size_hint=(1, .5), title='Duplicate Image')
            #     saved_popup_content = BoxLayout(orientation='vertical')
            #     saved_label = Label(font_size=20, text=f'Duplicate Image! Image already exists')
            #     ok_save_button = Button(text='OK', font_size=20, on_release=lambda a: saved_popup.dismiss())
            #     saved_popup_content.add_widget(saved_label)
            #     saved_popup_content.add_widget(ok_save_button)
            #     saved_popup.add_widget(saved_popup_content)
            #     saved_popup.open()                
            #     return

        self.used_watermark.save(f'{self.watermark_dir}/{date_to_save}.png')


        watermark_details = {"path": fp_to_save, "date_created": f"{now_date}"}
        watermark_data = {}

        with open('data/save_watermark_data.json') as outfile:
            watermark_data = json.load(outfile)

        data_dates = []
        
        watermark_data["data"].append(watermark_details)

        
        if len(watermark_data["data"]) > 3:
            for obj in watermark_data["data"]:
                data_dates.append(self.convert_to_date(obj["date_created"]))
            oldest_date = max(data_dates)
            for obj in watermark_data["data"]:
                if oldest_date == self.convert_to_date(obj["date_created"]):
                    watermark_data["date_created"].remove(obj)
                    if os.path.exists(obj["path"]):
                        os.remove(obj["path"])
             

        with open('data/save_watermark_data.json', "w") as outfile:
            json.dump(watermark_data, outfile)



        # calender = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        
        image_to_save.save(fp= fp_to_save)


        saved_popup = Popup(size_hint=(1, .5), title='Saved')
        saved_label = Label(font_size=20, text=f'Saved Succesfully! Find image in recents page')
        ok_save_button = Button(text='OK', font_size=20, on_release=lambda a: saved_popup.dismiss())
        saved_popup_content = BoxLayout(orientation='vertical')
        saved_popup_content.add_widget(saved_label)
        saved_popup_content.add_widget(ok_save_button)
        saved_popup.add_widget(saved_popup_content)
        saved_popup.open()

        self.temp_dir = f'{os.getcwd()}/temp'

        


    def image_is_same(self, imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        imageA = cv2.imread(imageA)
        imageB = cv2.imread(imageB)
        
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        
        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err <= 0

        

    def save_rendered_image_as(self, e):
        # date_to_save = datetime.now().strftime('%b-%d-%I%M%p-%G')

        image_to_save = Im.open(self.rendered_image.source)
        
        # fp_to_save = f'{os.getcwd()}/users/{self.user}/images/{date_to_save}.{self.img_format}'
        

        # image_to_save.save(fp= fp_to_save)

        root = tk.Tk()
        root.withdraw()
        files = [('PNG Image', '*.png'), ('JPEG Image', '*.jpeg')] 
        f = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        if f is None:
            return
        else:

            image_to_save.save(fp=f.name)

        
    def delete_temp_files(self):
        for file in os.listdir(self.temp_dir):
            os.remove(f'{self.temp_dir}/{file}')
        


    def return_to_homepage(self, controller, e):

        controller.initialize_home_page()
        self.delete_temp_files()





    def convert_to_date(self, watermark_date):
    
        year_month_date = watermark_date.split(' ')[0].split('-')
        year=int(year_month_date[0])
        month=int(year_month_date[1])
        day = int(year_month_date[2])
        hour_minute_second = watermark_date.split(' ')[1].split(':')
        hour = int(hour_minute_second[0])
        minute = int(hour_minute_second[1])
        second = int(hour_minute_second[2].split('.')[0])
        date_saved = datetime(year, month, day, hour, minute, second)
        return date_saved


