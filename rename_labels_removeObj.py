import os
#from xml.etree.ElementTree import parse, Element, SubElement, ElementTree
import xml.etree.ElementTree as ET
#from __future__ import annotations

files_path = "/home/slabs016/Descargas/Dataset_Miguel/"

#files_path = "/home/slabs016/Documentos/Springlabs/image_datasets/ppe/Dataset_Jesus/"

#files_path = "VOCdevkit/VOC2022/Annotations/"
files = os.listdir(files_path)
#files = ['hard_hat_workers0_test.xml']
text_to_replace = ["person", "Persona", "Casco", "Chaleco_bien"] #'helmet'
text_desired = ['W', 'W', 'H', 'V']

labels_to_remove = ["Chaleco_mal", "Sin_Casco", "Guantes_bien", "Guantes_mal", "Cubrebocas_bien", "Cubrebocas_mal", "Lentes_bien", "Lentes_mal"]

save_path = os.path.join(os.getcwd(), "labels")
try:
    os.mkdir(save_path)
except OSError as error:
    print(error) 

for file in files:
    if not file.endswith(".xml"):
        continue
    xml_file = files_path + file
    tree = ET.parse(xml_file)
    #tree = ET.parse('VOCdevkit/VOC2022/Annotations/hard_hat_workers0_test.xml')
    root = tree.getroot()

    for elem in root.iter():
        if not elem.tag == 'name':
            continue
        for index, text in enumerate(text_to_replace):
            if elem.text == text:
                elem.text = text_desired[index]

    objetos = tree.findall('object')
    for objeto in objetos:
        for elem in objeto:
            #print("objeto ", elem.tag, " ", elem.text)
            for label_to_remove in labels_to_remove:
                if elem.text == label_to_remove:
                    root.remove(objeto)


    tree.write(save_path + "/" + file)
