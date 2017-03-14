#!/usr/bin/env python
import sys
import cv2
import cv2.cv as cv
from video import create_capture
from common import draw_str

def help():
    print '''
        Usage: facedetect.py [options] --input <file>

        args:
            --help              print this message
            --cascade           haarcascades xml file to use
            --scale             <opencv>
            --min-neightbor     <opencv>
            --min-size-width    <opencv>
            --min-size-height   <opencv>
            --input             image input file to process
            --output            image output file
    '''
    sys.exit(0)

def argvalue(name, default=''):
    args = sys.argv
    if name not in args:
        return default
    value =  args[args.index(name) + 1]
    if len(value) == 0:
        return default
    return value

def argexist(name):
    args = sys.argv
    if name in args:
        return True
    else:
        return False

def error(msg):
    print 'ERROR: ' + msg
    exit(1)

def detect(img, cascade, scaleFactor_fn, minNeighbors_fn, minSizeWidth_fn, minSizeHeight_fn):

    rects = cascade.detectMultiScale(img,
            scaleFactor=scaleFactor_fn,
            minNeighbors=minNeighbors_fn,
            minSize=(minSizeWidth_fn, minSizeHeight_fn),
            flags = cv.CV_HAAR_SCALE_IMAGE)

    if len(rects) == 0:
        return []

    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def output(img, rects, file):
    vis = img.copy()
    draw_rects(vis, rects, (0, 255, 0))
    cv2.imwrite(file, vis)

def main():
    if argexist('--help'):
        help()

    cascade_fn = argvalue('--cascade', "./data/haarcascades/haarcascade_frontalface_alt.xml")
    img_src = argvalue('--input')

    if len(img_src) == 0:
        error('param "--input" is invalid')

    cascade = cv2.CascadeClassifier(cascade_fn)

    cam = create_capture('synth:bg=' + img_src)

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    scaleFactor_fn = float(argvalue('--scale',           1.1))
    minNeighbors_fn = int(argvalue('--min-neightbor',    3))
    minSizeWidth_fn = int(argvalue('--min-size-width',   0))
    minSizeHeight_fn = int(argvalue('--min-size-height', 0))

    rects = detect(gray, cascade, scaleFactor_fn, minNeighbors_fn, minSizeWidth_fn, minSizeHeight_fn)

    if argexist('--output'):
        output(img, rects, argvalue('--output'))

    return len(rects)

if __name__ == '__main__':
    print main()
