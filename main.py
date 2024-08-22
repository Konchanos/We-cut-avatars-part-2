from PIL import Image



image = Image.open("example.jpg")
red, green, blue = image.split()



coordinates = (100, 0, red.width, red.height)
cropped_left_red = red.crop(coordinates)



coordinates = (50, 0, red.width - 50, red.height)
cropped_right_left_red = red.crop(coordinates)


image_blend_red = Image.blend(cropped_left_red, cropped_right_left_red , 0.5)



coordinates = (0, 0, blue.width - 100, blue.height)
cropped_right_blue = blue.crop(coordinates)



coordinates = (50, 0, blue.width - 50, blue.height)
cropped_right_left_blue = blue.crop(coordinates)



image_blend_blue = Image.blend(cropped_right_blue, cropped_right_left_blue, 0.5)



coordinates = (50, 0, green.width - 50, green.height)
cropped_green = green.crop(coordinates)




rgb_image = Image.merge("RGB", (image_blend_red, cropped_green, image_blend_blue))
rgb_image.save("rgb_image.jpg")


rgb_image.thumbnail((80, 80)) 
rgb_image.save("image_avatar.jpg")
