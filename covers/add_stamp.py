#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
from PIL import Image, ImageDraw, ImageFont
import math
import os


class GeometrySet:
    def __init__(self, size=()):
        self.size = size
        self.width = 0
        self.height = 0
        self.x_centriod = 0
        self.y_centroid = 0
        self.x_y = (0, 0)
        self.diag_length = 0
        self.diag_angle = 0
        self.post_init()

    def post_init(self):
        # calc width & height
        self.width, self.height = self.size 
        # calc centroid
        self.x_centroid = self.width // 2
        self.y_centroid = self.height //2
        self.x_y = (self.x_centroid, self.y_centroid)

        self.diag_angle = self.get_diagonal_angle()
        self.diag_length = math.sqrt(self.width**2 + self.height**2)
  
    def get_diagonal_angle(self):
        angle_radians = math.atan2(self.height, self.width)
        return math.degrees(angle_radians)
    
    def trig(self, angle, length):
        angle_radians = math.radians(angle)
        x_length = length * math.cos(angle_radians)
        y_length = length * math.sin(angle_radians)
        return x_length, y_length
        
    
class OverlayText:
    def __init__(self, text="sample text", size=0, length=0, font="arial.ttf", ratio = 0.7):
        self.text = text
        self.size = size
        self.length = length
        self.font = font
        self.ratio = ratio
        self.real_length = 0
        self.post_init()

    def post_init(self):
        try:
            self.size = self.calc_size() if not self.size else self.size
        except Exception as e:
            print("Not a size or length was given")
        self.font = self.init_font()
        self.real_length = self.font.getlength(self.text)

    def calc_size(self):
        text_length = int(self.length * self.ratio)

        return int(text_length / len(self.text) * 1.5)
    
    def init_font(self):
        return ImageFont.truetype("arial.ttf", self.size)
  

class TextImg:
    def __init__(self, text_object, oversize=1.0):
        self.text_object = text_object
        self.over = oversize
        self.dims = (0,0)
        self.image = 0
        self.draw  = 0
        self.geo = 0
        self.x_y = (0,0)
        self.rgba = (255, 0, 0, 160)
        self.post_init()

    def post_init(self):
        l = self.text_object.real_length
        h = self.text_object.size
        self.dims = (int(l*self.over), int(h*self.over))
        self.image = Image.new(
            'RGBA', self.dims, (255,255,255, 40))
        self.draw = ImageDraw.Draw(self.image)

        self.geo = GeometrySet(self.dims)

    def text_on_image(self):
        self.x_y = (self.geo.x_centriod, self.geo.y_centroid)
        self.draw.text((0,0), self.text_object.text,
                       fill=self.rgba, font=self.text_object.font)
        
    def rotate_text(self, angle):
        self.image = self.image.rotate( angle, expand=1)
        return  self.image

    def post_rotate_positions(self, image_height, image_width):
        new_width, new_height = self.image.size
        new_x = (image_width - new_width) // 2
        new_y = (image_height - new_height) // 2
        self.dims = new_x, new_y

    def override_position(self, mod_x=0, mod_y=0):
        x , y = self.dims
        self.dims = x+ mod_x, y+ mod_y


def stamp_cover(image,save_location, ownership):
    # Image
    image = Image.open(image)
    image_width, image_height = image.size
    img_geo = GeometrySet(image.size)

    # HARDCOPY text
    hardcopy_text = OverlayText("HARDCOPY", length=img_geo.diag_length)
    hard_text_image = TextImg(text_object=hardcopy_text)
    h = hard_text_image
    h.text_on_image()
    h.rotate_text(img_geo.diag_angle)
    h.post_rotate_positions(image_height, image_width)

    # Owner's text
    owners_text = OverlayText(ownership, length=img_geo.diag_length, ratio=0.5)
    owner_text_image = TextImg(text_object=owners_text)
    o = owner_text_image
    o.rgba = (59, 186, 108) #override color
    o.text_on_image()
    o.rotate_text(img_geo.diag_angle)
    o.post_rotate_positions(image_height, image_width)
    x, y = img_geo.trig(90-img_geo.diag_angle, 2*(hardcopy_text.size/2))
    o.override_position(mod_x=int(x), mod_y=int(y))

    # Text on image
    image.paste(h.image, h.dims, h.image)
    image.paste(o.image, o.dims, o.image)
    # image.show()  
    image.save(save_location)  # Save the image with rotated text

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    image_path = os.getenv("TEST_BOOK_IMAGE")
    save_location = os.getenv("TEST_BOOK_STAMPED_IMAGE")
    stamp_cover(image_path, save_location, ownership="Gino's")

if __name__ == '__main__':
    main()