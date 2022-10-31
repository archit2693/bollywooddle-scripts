from PIL import Image
image = Image.open('brahmastra.jpeg')
res = 16
while True:	
	if res > 250:
		break
	res = res + 16
	image_tiny = image.resize((res, res))    
	pixelated = image_tiny.resize(image.size,Image.NEAREST)
	name = "brahmastra_pixelate_"+str(res)+".jpeg"
	pixelated.save(name)