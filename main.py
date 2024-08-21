from PIL import Image



red = Image.open("blend_red.jpg")
green = Image.open("cropped_right_left_green.jpg")
blue = Image.open("blend_blue.jpg")


rgb_image = Image.merge("RGB", (red, green, blue))
rgb_image.save("rgb_image.jpg")


rgb_image.thumbnail((80, 80)) 
rgb_image.save("image_avatar.jpg")