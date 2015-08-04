import glob
import os
from shutil import copyfile
from PIL import Image

images = [file for file in glob.glob('*.png')]
for i, image in enumerate(images):
    im = Image.open(image)
    im.save('html/images/{}.jpg'.format(i))
    if i % 25 == 0:
        print('{} of {} converted.'.format(i, len(images)))



# [copyfile(file, './html/images/{}.png'.format(i))
# #[print('{}: {}'.format(i, file))
#     for (i,file)
#     in enumerate(glob.glob('*.png'))
#     if os.path.isfile(file)
# ]
# #[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]
