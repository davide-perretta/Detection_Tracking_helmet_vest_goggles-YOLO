import xml
from xml.dom import minidom
import os
import glob

lut = {}
lut["person"] = 0
lut["helmet"] = 1
lut["vest"] = 2
lut["goggles"] = 3

countPerson = 0
countHelmet = 0
countVest = 0
countGoggles = 0

def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_xml2yolo(lut, countPerson, countHelmet, countVest, countGoggles):


    for fname in glob.glob("PATH file /*.xml"):

        xmldoc = minidom.parse(fname)

        fname_out = (fname[:-4] + '.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)
            for item in itemlist:
                # get class label
                classid = (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                    if classid == "person":
                        countPerson = countPerson + 1
                    if classid == "helmet":
                        countHelmet = countHelmet + 1
                    if classid == "vest":
                        countVest = countVest + 1
                    if classid == "goggles":
                        countGoggles = countGoggles + 1
                else:
                    label_str = "-1"
                    print("warning: label '%s' not in look-up table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width, height), b)
                # print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print("wrote %s" % fname_out)
        print("Person = " + str(countPerson), " Helmet = " + str(countHelmet), " Vest = " + str(countVest), " Goggles = " + str(countGoggles))


def main():
    convert_xml2yolo(lut, countPerson, countHelmet, countVest, countGoggles)

if __name__ == '__main__':
    main()
