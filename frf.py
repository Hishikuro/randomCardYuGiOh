
import requests
import json 
requet = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?")
data = json.loads(requet.text)
print(data["data"][1]["card_images"][0]['image_url'])
