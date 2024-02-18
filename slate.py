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
    
class OverlayText:
    def __init__(self, text="sample text", size=0, length=0, font="arial.ttf"):
        self.text = text
        self.size = size
        self.length = length
        self.font = font
        self.real_length = 0
        self.post_init()

    def post_init(self):
        try:
            self.size = self.calc_size() if not self.size else 0/0
        except Exception as e:
            print("Not a size or length was given")
        self.font = self.init_font()
        self.real_length = self.calc_real_length()

    def calc_size(self):
        text_length = int(self.length * 0.6)
        return int(text_length / len(self.text) * 1.5)
    
    def init_font(self):
        return ImageFont.truetype("arial.ttf", self.size)
    
    def calc_real_length(self):
        return self.font.getlength(self.text)

class TextImg:
    def __init__(self, text_object, oversize=1.02):
        self.text_object = text_object
        self.over = oversize
        self.dims = (0,0)
        self.image = 0
        self.draw  = 0
        self.geo = 0
        self.x_y = (0,0)
        self.post_init()

    def post_init(self):
        l = self.text_object.real_length
        h = self.text_object.size
        self.dims = (int(l*self.over), int(h*self.over))
        self.image = Image.new(
            'RGBA', self.dims, (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.geo = GeometrySet(self.dims)

    def text_on_image(self):
        self.x_y = (self.geo.x_centriod, self.geo.y_centroid)
        self.draw.text(self.x_y, "HARDCOPY", anchor="mm",
                       fill="black", font=self.text_object.font)
        
    def rotate_text(self, angle):
        return  self.image.rotate( angle, center=self.x_y, expand=1)


def stamp_cover(image, ownership):
    text = "HARDCOPY"
    image = Image.open(image)
    image_width, image_height = image.size
    # print("size", image.size)  # ! 326 500

    diag_angle = math.degrees(math.atan2(image_height, image_width))
    diag_length = math.sqrt(image_width**2 + image_height**2)
    # print(diag_length) #! 596

    text_length = int(diag_length * 0.7)
    font_size = int(text_length / len(text) * 1.5)

    # print("size", font_size)

    # font_size = int(min(image_width, image_height) / 4)
    font = ImageFont.truetype("arial.ttf", font_size)

    text_width = font.getlength(text)
    # print("length",text_width) #!

    # Create a transparent image for text large enough to hold the text
    dims = (int(text_width), int(font_size))
    # print("dims", dims )#!441, 78

    text_image = Image.new(
        'RGBA', dims, (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)

    # Draw the text at the top-left corner of the text_image
    text_draw.text((0, 0), text, fill="black", font=font)

    # Rotate the text image
    rotated_text_image = text_image.rotate(diag_angle, expand=1)

    # Calculate new position after rotation to ensure text is centered
    new_width, new_height = rotated_text_image.size

    new_x = (image_width - new_width) // 2
    new_y = (image_height - new_height) // 2

    image.paste(rotated_text_image, (new_x, new_y), rotated_text_image)
    image.show()  # Display the result


def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)

    image_path = r"C:\Users\natha\Desktop\calibre-hardcopy-entry\test\books_set\Andy Weir\Project Hail Mary_ From the Bestsel (569)\raw_cover.jpg"
    stamp_cover(image_path, ownership="Nathan's")


if __name__ == '__main__': 
    main()