#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-02-14
"""
from PIL import Image, ImageDraw, ImageFont
import math
import os
marker = 'marker'

def get_diagonal_angle(y,x):
    angle_radians = math.atan2(y, x)
    return math.degrees(angle_radians)  

class GeometrySet:
    def __init__(self, size=()):
        self.size = size
        self.width = 0
        self.height = 0
        self.x_centriod = 0
        self.y_centroid = 0
        self.diag_length = 0
        self.diag_angle = 0
        self.post_init()

    def post_init(self):
        # calc width & height
        self.width, self.height = self.size 
        # calc centroid
        self.x_centroid = self.width // 2
        self.y_centroid = self.height //2

        self.diag_angle = self.get_diagonal_angle()
        self.diag_length = math.sqrt(self.width**2 + self.height**2)
  
    def get_diagonal_angle(self):
        angle_radians = math.atan2(self.height, self.width)
        return math.degrees(angle_radians)


def stamp_cover(image, ownership):
    image = Image.open(image)

    image_width, image_height = image.size
  
    img_geo = GeometrySet(image.size)

    x_cent = image_width // 2
    y_cent = image_height //2

    text_length = int(img_geo.diag_length * 0.6)
    font_size = int(text_length / len("HARDCOPY") * 1.5)

    font = ImageFont.truetype("arial.ttf", font_size)  # Change font and size as needed
    length = font.getlength("HARDCOPY")

    text_image = Image.new('RGBA', (int(2*length), image_height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)

    # Draw the text onto the text image
    text_draw.text((x_cent, y_cent), "HARDCOPY",anchor="mm", fill="black", font=font)

    rotated_text_image = text_image.rotate(img_geo.diag_angle , center=(x_cent, y_cent))

    position = (0, 0)  # Change this to the desired position
    image.paste(rotated_text_image, position, rotated_text_image)

    image.show()  
    # image.save('result_image.jpg')  # Save the image with rotated text

def main():
    
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    image_path = r"C:\Users\natha\Desktop\calibre-hardcopy-entry\test\books_set\Andy Weir\Project Hail Mary_ From the Bestsel (569)\raw_cover.jpg"
    stamp_cover(image_path, ownership="Nathan's")
    # stamp_diagonal_text(image_path, "HARDCOPY")

if __name__ == '__main__':
    main()