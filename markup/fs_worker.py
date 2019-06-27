import os
import numpy as np
import cv2
import io
from PIL import Image
import base64
import json

out_folder = '/Users/vadimksendzov/work/Fit/Flask_project/new_blog_start/git_app/out_folder/'
src = '/Users/vadimksendzov/work/Datasets/RA/Skeleton_hand/Dataset_3/'

path_list = []
whole_path_list = {}

ttt = 0



def create_work_list():
    src_list = []
    work_path_list = []

    global path_list
    #
    # global ttt

    src_folder = os.walk(src, topdown=False)

    already_marked_files = [file_name for file_name in os.listdir(out_folder) if '.png' in file_name]

    for root, dirs, files in src_folder:
        for name in files:
            if '.bin' in name and '._' not in name:
                file_src_name = os.path.join(root, name)
                src_list.append(file_src_name)

    for file in src_list:
        name_for_check = file.split('/')[-1].split('.')[0] + '.png'
        if name_for_check in already_marked_files:
            continue
        else:
            work_path_list.append(file)

    path_list = work_path_list

    return work_path_list


def get_the_first_img():

    the_first_path = path_list[0]

    bgr_img, rgb_img = read_bin_file(the_first_path)
    converted_img = readed_bin_to_base64(rgb_img)

    img_to_client = img_obj(the_first_path, converted_img)

    return img_to_client


def get_the_next_img(current_img_path):

    current_path_index = path_list.index(current_img_path)
    print('NEXT_current_path_index----', current_path_index)
    next_index = current_path_index + 1
    next_path = path_list[next_index]

    print('NEXT_path--->', next_path)
    bgr_img, rgb_img = read_bin_file(next_path)
    converted_img = readed_bin_to_base64(rgb_img)

    img_to_client = img_obj(next_path, converted_img)

    return img_to_client


def get_the_previous_img(current_img_path):

    current_path_index = path_list.index(current_img_path)
    print('PREVIOUS_current_path_index----', current_path_index)

    if current_path_index <= 0:
        next_index = 0
    else:
        next_index = current_path_index - 1

    next_path = path_list[next_index]

    print('PREVIOUS_path--->', next_path)
    bgr_img, rgb_img = read_bin_file(next_path)
    converted_img = readed_bin_to_base64(rgb_img)

    img_to_client = img_obj(next_path, converted_img)

    return img_to_client


def read_bin_file(path):
    print('PATH--->', path)
    fi_plain = np.fromfile(path, dtype=np.uint8)
    width = 720
    height = 1280
    YCbCr = np.zeros((width, height, 3), dtype=np.uint8)

    Y1 = 0
    Y2 = Y1 + height * width

    C1 = Y2
    C2 = C1 + height * int(width / 2)

    Y = fi_plain[Y1:Y2]
    Cb = fi_plain[C1:C2:2]
    Cr = fi_plain[C1 + 1:C2:2]

    Y = np.reshape(Y, [width, height])
    Cb = np.reshape(Cb, [int(width / 2), int(height / 2)])
    Cr = np.reshape(Cr, [int(width / 2), int(height / 2)])
    YCbCr[:, :, 0] = Y

    for c in range(2):
        for c1 in range(2):
            YCbCr[c:(int(width / 2)) * 2 + c:2, c1:(int(height / 2)) * 2 + c1:2, 1] = Cb
            YCbCr[c:(int(width / 2)) * 2 + c:2, c1:(int(height / 2)) * 2 + c1:2, 2] = Cr

    bgr_img = cv2.flip(cv2.cvtColor(np.transpose(YCbCr, axes=(1, 0, 2)), cv2.COLOR_YUV2BGR), 1)
    rgb_img = cv2.flip(cv2.cvtColor(np.transpose(YCbCr, axes=(1, 0, 2)), cv2.COLOR_YUV2RGB), 1)

    return bgr_img, rgb_img


def readed_bin_to_base64(readed_bin_file):

    buffer = io.BytesIO()
    img = Image.fromarray(readed_bin_file, 'RGB')
    img.save(buffer, format='JPEG')
    img_str = base64.b64encode(buffer.getvalue())
    r_img = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
    d_img = r_img.decode('utf-8')

    return d_img

def img_obj(img_path, img_str):

    img_object = dict(img_name=img_path, img_obj=img_str)
    # img_object['img_name'] = img_name
    # img_object['img_obj'] = img_str

    return img_object


def save_points(json_points, file_name):
    global out_folder
    global src
    global work_path_list

    clear_name = file_name.split('/')[-1].split('.')[0]
    json_name = clear_name + '.json'

    json_name_for_save = out_folder + json_name
    # bin_path = src + file_name


    png_name = clear_name + '.png'
    name_for_save_png = out_folder + png_name
    bgr_img, _ = read_bin_file(file_name)

    with open(json_name_for_save, 'w') as outfile:
        json.dump(json_points, outfile)

    cv2.imwrite(name_for_save_png, bgr_img)







