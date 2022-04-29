import requests
import json 
import pygame 
import io 
from urllib.request import urlopen
from random import randint 

pygame.display.set_caption("RANDOM CARD") 

requet = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
info = requet.text
data = json.loads(info)
id = randint(0,len(data["data"])-1)


pygame.init()

image_url = data["data"][id]["card_images"][0]['image_url']

image_str = urlopen(image_url).read()
image_file = io.BytesIO(image_str)
white = (255, 255, 255)
screen = pygame.display.set_mode((421,614))
screen.fill(white)
image = pygame.image.load(image_file)
screen.blit(image, (0, 0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit