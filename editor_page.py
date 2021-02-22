from kivy.core import text
from kivy.core.text import markup
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.slider import Slider

from kivy.uix.scrollview import ScrollView

import tkinter as tk
from tkinter import filedialog
from PIL import Image as Im

from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image
from kivy.uix.popup import Popup


from functools import partial

import os


class EditorPage(Screen):
    def __init__(self, page_controller, **kw):
        super().__init__(**kw)

        #TODO set self.user back to user
        self.user = 'kathy'
        self.save_counter = 0

        #TODO set self.img_url back to img_url
        self.img_url = f'{os.getcwd()}/users/{self.user}/images/test.png'

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
        self.generate_share_box()
        self.add_widget(self.root_layout)

    def generate_recent_watermarks(self):
        recent_watermark_box = BoxLayout(orientation='vertical', size_hint=(.15, 1))
        recent_watermark_label = Label(text='RECENT WATERMARKS', size_hint = (1, .4), font_size=15)
        recent_watermark_box.add_widget(recent_watermark_label)

        watermark_dir = os.listdir(self.watermark_path)
        
        for watermark in watermark_dir:
            watermark_source =f'{self.watermark_path}/{watermark}'
            water_image = Image(source=watermark_source, size_hint=(1, 1), allow_stretch=False, keep_ratio=True)


            recent_watermark_box.add_widget(water_image)
        
        self.root_layout.add_widget(recent_watermark_box)

    
    def generate_editing_box(self):
        editing_box = BoxLayout(orientation='vertical', size_hint=(.4, 1), spacing=5)
        editing_button_box = BoxLayout(orientation='horizontal', spacing=3, size_hint=(1, .1), pos_hint={'x': 0, 'y': 0})

        add_text_button = Button(text=' ADD \n\nTEXT', font_size=15, size_hint=(1, 1))
        add_watermark_button = Button(text='    ADD \n\nWATERMARK', font_size=15, size_hint=(1, 1), on_release=self.generate_editor)
        delete_watermark_button = Button(text='    DELETE \n\nWATERMARK', font_size=15, size_hint=(1, 1))

        editing_button_box.add_widget(add_text_button)
        editing_button_box.add_widget(add_watermark_button)
        editing_button_box.add_widget(delete_watermark_button)

        image_box = BoxLayout(orientation='vertical', size_hint=(1, .7))
        user_image = Image(source=self.img_url, allow_stretch=False, keep_ratio=True)
        image_box.add_widget(user_image)

        editing_box.add_widget(editing_button_box)
        editing_box.add_widget(image_box)

        self.root_layout.add_widget(editing_box)

    def generate_share_box(self):
        share_box = BoxLayout(orientation='vertical', size_hint=(.15, 1), spacing=5)


        view_recents_button = Button(text="VIEW RECENTS", font_size=15, size_hint=(1, .1))
        empty_space = BoxLayout(orientation='vertical', size_hint=(1, .3))
        save_button = Button(text='SAVE', font_size=15, size_hint=(1, .1))
        save_as_button = Button(text='SAVE AS', font_size=15, size_hint=(1, .1))
        empty_space2 = BoxLayout(orientation='vertical', size_hint=(1, .3))
        back_button = Button(text='BACK', font_size=15, size_hint=(1, .1))

        share_box.add_widget(view_recents_button)
        share_box.add_widget(empty_space)
        share_box.add_widget(save_button)
        share_box.add_widget(save_as_button)
        share_box.add_widget(empty_space2)
        share_box.add_widget(back_button)

        self.root_layout.add_widget(share_box)


    def generate_editor(self, button):

        editor_box_popup = Popup(title='EDIT IMAGE')

        image_is_uploaded = False
        root = tk.Tk()
        root.withdraw()
        self.marker_path = filedialog.askopenfilename()

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
        self.size_slider = Slider(min=1, max=10, step=1)
        watermark_config_box.add_widget(size_label)
        watermark_config_box.add_widget(self.size_slider)
        self.size_slider.bind(value=self.render_image)

        up_arrow_spacing = BoxLayout(orientation='vertical')
        watermark_config_box.add_widget(up_arrow_spacing)

        move_up_button = Button(text='up', size_hint=(.3, 1), pos_hint={'x':.35, 'y':0})
        watermark_config_box.add_widget(move_up_button)

        move_left_and_right_box = BoxLayout(orientation='horizontal')
        move_left_button = Button(text='left')
        move_label = Label(text='move', font_size=15)
        move_right_button = Button(text='right')
        move_left_and_right_box.add_widget(move_left_button)
        move_left_and_right_box.add_widget(move_label)
        move_left_and_right_box.add_widget(move_right_button)
        watermark_config_box.add_widget(move_left_and_right_box)

        down_arrow_button = Button(text='down', size_hint=(.3, 1), pos_hint={'x':.35, 'y':0})
        watermark_config_box.add_widget(down_arrow_button)

        done_button_spacing = BoxLayout(orientation='horizontal')
        watermark_config_box.add_widget(done_button_spacing)

        done_button = Button(text='DONE', font_size=15)
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
            editor_box_popup.content = editor_box_content_box
            editor_box_popup.open()
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


    def render_image(self, button='a', b='b'):
        main_image = Im.open(self.img_url)
        watermark = Im.open(self.marker_path)

        main_image_x_size = main_image.size[0]
        main_image_y_size = main_image.size[1]

                
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
        if type(button) == Button:
            # for butt in button.parent.children:
            #     butt.enabled = True
            #     button.parent._trigger_layout()
            #     print(butt.enabled)
            self.watermark_position = watermark_positions[button.text]
            



        # disable clicked button with different color
        # get the text of the clicked button
        # Depending on the text, place the marker on the image



        img_format = main_image.format
        
        watermark.thumbnail((watermark_x_size, watermark_y_size))
        watermark.putalpha(int(25.5 * opacity_multiplier))

        rotated_image = watermark.rotate(rotation_value, expand=1)
        main_image.paste(rotated_image, self.watermark_position, rotated_image)

        save_source = f'temp/temp_img{self.save_counter}.{img_format}'
        self.save_counter += 1
        if self.save_counter > 2:
            os.remove(f'temp/temp_img{self.save_counter - 2}.{img_format}')

        main_image.save(save_source)

        self.rendered_image.source = save_source

        main_image.close()
        watermark.close()

        
        







