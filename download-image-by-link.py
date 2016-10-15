##########################################################################################################
# Code is based on: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/  #
##########################################################################################################
import urllib2
from urllib2 import HTTPError, URLError
import numpy as np
import os
from socket import timeout
    
def store_raw_pos_images():
    pos_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04096066'   
    pos_image_urls = urllib2.urlopen(pos_images_link).read()
    pic_num = len([name for name in os.listdir('road_classifier_data') if os.path.isfile(name)])+1
    fail_images = 0
    fail_url = 0
    
    if not os.path.exists('road_classifier_data'):
        os.makedirs('road_classifier_data')
        
    for i in pos_image_urls.split('\n'):
        try:
            i
            try:
                f = urllib2.urlopen(i)
                data = f.read()
                with open("road_classifier_data/"+str(pic_num)+".jpg", "wb") as code:
                    code.write(data)
                pic_num += 1
                print "no fail"
            except (HTTPError, URLError) as error:
                fail_url = 0
                print "fail"
            except timeout:
                fail_url = 0
                print "fail"
            
        except Exception as e:
            print str(e)
    print fail_images + " invalid imgages"
    print fail_url + " invalid urls"

store_raw_pos_images()
