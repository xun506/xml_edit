#coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "F:/02 UCAS_Prj/01 R-FCN/数据集整理/xml_edit/xml_edit/xml_edit/源文件/"
path2 = "F:/02 UCAS_Prj/01 R-FCN/数据集整理/xml_edit/xml_edit/xml_edit/转换/"
files=os.listdir(path)
i=201976
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        print (xmlFile)
        dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
        root=dom.documentElement
        image_folder=root.getElementsByTagName('folder')
        image_filename=root.getElementsByTagName('filename')
        image_path=root.getElementsByTagName('path')
        image_folder[0].firstChild.data="image"
        image_path[0].firstChild.data="image"
        image_filename[0].firstChild.data=i
        i=i+1

        with open(os.path.join(path2,xmlFile),'w') as fh:
            dom.writexml(fh,encoding = 'utf-8' )
            print('写入OK!')