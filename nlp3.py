from pathlib import Path 
import imageio
from wordcloud import WordCloud

text = Path('RomeoAndJuliet.txt').read_text()

## the built-in image for word cloud is called a mask. but we can replace the mask with any other image

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap='prism',mask=mask_image,background_color='white')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

print("done")