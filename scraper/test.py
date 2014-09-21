import wikipedia as wiki 

page =  wiki.page('Atack on Titan')

print page.title

for image in page.images:
	if 'http://upload.wikimedia.org/wikipedia/en/' in image and '.jpg' in image: 
		print image

print page.sections
