import requests
import json 
import pygame 
import io 
from urllib.request import urlopen
from random import random 
pygame.display.set_caption("RANDOM CARD") 
rand =True 
while rand :
	id=str(int(random()*1000000))
	requet = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?id="+id)
	info = requet.text
	data = json.loads(info)
	print(id)
	if requet.status_code != 400:
		rand = False

print(data["data"][0]["card_images"][0]['image_url'])



   

# initialize pygame
pygame.init()

# on a webpage right click on the image you want and use Copy image URL
image_url = data["data"][0]["card_images"][0]['image_url']

image_str = urlopen(image_url).read()
# create a file object (stream)
image_file = io.BytesIO(image_str)

# (r, g, b) color tuple, values 0 to 255
white = (255, 255, 255)

# create a 600x400 white screen
screen = pygame.display.set_mode((421,614))
screen.fill(white)

# load the image from a file or stream
image = pygame.image.load(image_file)

# draw image, position the image ulc at x=20, y=20
screen.blit(image, (0, 0))

# nothing gets displayed until one updates the screen
pygame.display.flip()

# start event loop and wait until
# the user clicks on the window corner x to exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit