import autopy

def find_image_example():
    needle = autopy.bitmap.Bitmap.open('needle.png')

    autopy.bitmap.capture_screen().save('ss.png')
    haystack = autopy.bitmap.Bitmap.open('ss.png')

    pos = haystack.find_bitmap(needle)
    print("Found needle at: %s" % str(pos))

    scale = autopy.screen.scale()
    print(str(scale))

    if pos:
      autopy.mouse.smooth_move(pos[0]/scale + 50, pos[1]/scale + 15)
      autopy.mouse.click()

find_image_example()