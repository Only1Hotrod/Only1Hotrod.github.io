from PIL import Image
my_image =  Image.open("Roderick.jpg")
image_pixels = my_image.load()
width,height = my_image.size 
for i in range(width-1-1-1): 
    for j in range(height-1-1-1):
        current_pixel = image_pixels[i,j]
        blue_component = current_pixel[0]
        green_component = current_pixel[1]
        red_component = current_pixel[2]
        gray_value = (int)(0.07 * blue_component + 0.72 * green_component + 0.21 * red_component)
        if(gray_value < 50):
            new_color = (0,31,59)
        elif(gray_value < 100):
            new_color = (215,30, 1)  
        elif(gray_value < 150):
            new_color = (250,237,192)
        elif(gray_value < 200):
            new_color = (12,198,139)
        elif(gray_value < 250):
            new_color = (217, 245, 7)
        else:
            new_color = (0, 255, 255)
        image_pixels[i,j] = (new_color[0], new_color[1], new_color[2],255)
my_image.show()
my_image.save("my_image", "JPEG")
