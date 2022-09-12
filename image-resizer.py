from PIL import Image


def resizer(image,width,length):
    resized_image=image.resize((width,length))
    name=input('Write a name for the resized image. (for example: image.png): ')
    resized_image.save(name)
    print('Done :)')

def get_image():
    want_to_resize=input('Hi there. Do you wanna resize an image?[y/n] ').lower()
    YES_OR_NOT=['y','n']
    if want_to_resize == "y":
        image_name=input('Type the full name of the image: ')
        try:
            image=Image.open(image_name)
            print(f"Current size is {image.size}")
            width=int(input('Type the new width:'))
            length=int(input('Type the new length:'))
            resizer(image,width, length)
        except:
            print('There is no image with given name')    
    elif want_to_resize == "n":
        print('OK. Have a good day')
    elif want_to_resize not in YES_OR_NOT:
        print("You're just allowed to type Y or N")
        get_image()            



get_image()    


