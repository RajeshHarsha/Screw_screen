import rotatescreen
import time

sc = rotatescreen.get_primary_display()
for i in range(13):
    time.sleep(1)
    sc.rotate_to(i*90 % 360)
