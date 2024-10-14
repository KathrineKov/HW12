import requests
import re
import os

url = 'https://gsom.spbu.ru/en/'
response = requests.get(url)
response_text = response.text

png_count = response_text.count('.png')
print("Number of '.png' image links: " + str(png_count))

first_png_position = response_text.find('.png')
if first_png_position != -1:
    start_quote = response_text.rfind('"', 0, first_png_position) + 1
    end_quote = first_png_position + 4  
    image_url = response_text[start_quote:end_quote]

    if not image_url.startswith('http'):
        image_url = 'https://gsom.spbu.ru' + image_url

    print("First PNG image link: " + image_url)

    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        filename = os.path.join(os.getcwd(), 'downloaded_image.png')
        with open(filename, 'wb') as f:
            f.write(image_response.content)
        print("Image successfully saved as " + filename)
    else:
        print("Failed to download the image.")
else:
    print("No '.png' images found.")