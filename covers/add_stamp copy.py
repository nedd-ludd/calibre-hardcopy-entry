`#!/usr/bin/env python3
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

def stamp_cover(image, ownership):
    image = Image.open(image)
    image_width, image_height = image.size

    x_cent = image_width/ 2
    y_cent = image_height /2
    text_image_center = (image_width // 2, image_height // 2)

    diag_angle = get_diagonal_angle(y_cent, x_cent)

    diagonal_length = math.sqrt(image_width**2 + image_height**2)
    text_length = int(diagonal_length * 0.6)

    font_size = int(text_length / len("HARDCOPY") * 1.8)

    font = ImageFont.truetype("arial.ttf", font_size)  # Change font and size as needed
    length = font.getlength("HARDCOPY")

    text_image = Image.new('RGBA', (int(1.6*length), image_height), (255, 255, 255, 0))

    #can i rotate image before draw
    text_draw = ImageDraw.Draw(text_image)

    # Draw the text onto the text image
    text_draw.text((x_cent, y_cent), "HARDCOPY",anchor="mm", fill="black", font=font)

    rotated_text_image = text_image.rotate(diag_angle, expand=0 , center=text_image_center)

    position = (0, 0)  # Change this to the desired position
    image.paste(rotated_text_image, position, rotated_text_image)

    image.show()  
    # image.save('result_image.jpg')  # Save the image with rotated text


    raise SystemExit(1)
    with Image.open(image).convert("RGBA") as base:
        image_width, image_height = base.size
        x_cent = image_width/ 2
        y_cent = image_height /2
        diag_angle = get_diagonal(y_cent, x_cent)

        diagonal_length = math.sqrt(image_width**2 + image_height**2)
        text_length = int(diagonal_length * 0.6)

        font_size = int(text_length / len("HARDCOPY") * 2)  # Adjusted to approximate better
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        fnt = ImageFont.truetype("arial.ttf", font_size)

        d = ImageDraw.Draw(txt)
        
        d.text((x_cent, y_cent), "HARDCOPY", anchor="mm", font=fnt, fill=(255, 0, 0, 145))
      
        rotated_text_image = txt.rotate(diag_angle, expand=1)

        # Paste the rotated text image onto the original image
        # Specify the position where you want to paste the text
        position = (int(x_cent), int(y_cent))  # Change this to the desired position
        base.paste(rotated_text_image, position, rotated_text_image)
                
        

        
        # owner = f"({ownership})"
        # d.text((10, 60), owner, font=fnt, fill=(255, 255, 255, 255))
        out = Image.alpha_composite(base, txt)
        out.show()

def main():
    
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    image_path = r"C:\Users\natha\Desktop\calibre-hardcopy-entry\test\books_set\Andy Weir\Project Hail Mary_ From the Bestsel (569)\raw_cover.jpg"
    stamp_cover(image_path, ownership="Nathan's")
    # stamp_diagonal_text(image_path, "HARDCOPY")

if __name__ == '__main__':
    main()