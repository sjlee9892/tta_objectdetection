import os
import re
from utils.utils import json_load

config = json_load('./config_iou.json')
DIR = config['DIR']

def convert_data_path(DIR):
    valid_txt_path = os.path.join(DIR['ROOT_DIR'], 'valid.txt')
    txt = open(valid_txt_path, 'r')
    lines = txt.readlines()
    new_lines = []
    for line in lines:
        line = line.split('/')
        new_lines.append(re.sub('[\\\]','/',os.path.join(DIR['ROOT_DIR'], 'images', line[len(line)-1])))
    with open(valid_txt_path, 'w') as file:
        file.writelines(new_lines)

convert_data_path(DIR)
