from flask import Blueprint, render_template, request, jsonify
from markup.fs_worker import create_work_list, \
    read_bin_file, \
    readed_bin_to_base64, \
    save_points,\
    img_obj, \
    get_the_first_img,\
    get_the_previous_img,\
    get_the_next_img


import json

hands_markup = Blueprint('markup', __name__, template_folder='templates')

count = 0




# GET Create page, get image
@hands_markup.route('/', methods=['POST', 'GET'])
def skeleton_markup():
    global count

    if request.method == 'GET':
    #
        create_work_list()
    #     _, rgb_img = read_bin_file(work_paths_list[count])
    #     converted_img = readed_bin_to_base64(rgb_img)
    #     img_to_client = img_obj(work_paths_list[count], converted_img)


        # return render_template('markup_clients/hands_skeleton_11.html', str_img=img_to_client)
        return render_template('markup_clients/hands_skeleton_11.html')

    # elif request.method == 'POST':
    #
    #     next_previous_handle = request.form['count_action']
    #
    #     if next_previous_handle == 0:
    #         count -= 1
    #         work_paths_list = create_work_list()
    #         _, rgb_img = read_bin_file(work_paths_list[count])
    #         converted_img = readed_bin_to_base64(rgb_img)
    #
    #         return render_template('markup_clients/hands_skeleton_11.html', str_img=converted_img)
    #
    #     elif next_previous_handle == 1:
    #         count += 1
    #         work_paths_list = create_work_list()
    #         _, rgb_img = read_bin_file(work_paths_list[count])
    #         converted_img = readed_bin_to_base64(rgb_img)
    #
    #         return render_template('markup_clients/hands_skeleton_11.html', str_img=converted_img)


@hands_markup.route('/save_points', methods=['POST'])
def save_points_from_client():
    global count


    if request.method == 'POST':

        # src_dict_from_request = request.form.to_dict()
        src_dict_from_request = request.form.to_dict()

        for src_keys in src_dict_from_request:
            src_keys_1 = json.loads(src_keys)

        print(src_dict_from_request)
        img_name = src_keys_1['file_name']
        points = src_keys_1['points']

    work_paths_list = create_work_list()
    save_points(points, img_name)
    # count += 1

    # _, rgb_img = read_bin_file(work_paths_list[count])
    # converted_img = readed_bin_to_base64(rgb_img)

    # return converted_img
    return 'TTTTTTTT'

@hands_markup.route('/get_image', methods=['POST'])
def get_image():

    if request.method == 'POST':
        action_number = request.form.to_dict()
        for src_keys in action_number:
            action = json.loads(src_keys)['select_action']
            current_img_path = json.loads(src_keys)['current_path']
            print('action==', action)
            print('current_img_path==', current_img_path)


        if not action:
            print('NOT_Action')
            img_to_client = get_the_first_img()
            return jsonify(img_to_client)
        elif action == 1:
            print('PREVIOUS_Action')
            img_to_client = get_the_previous_img(current_img_path)
            return jsonify(img_to_client)
        elif action == 2:
            print('NEXT_Action')
            img_to_client = get_the_next_img(current_img_path)
            return jsonify(img_to_client)


@hands_markup.route('/tt', methods=['POST'])
def make_test_request():

    if request.method == 'POST':

        # src_dict_from_request = request.form.to_dict()
        src_dict_from_request = request.form.to_dict()
        for src_keys in src_dict_from_request:
            src_keys_1 = json.loads(src_keys)


        return 'good'

        # points_json = request.form['points']
        #
        # print(points_json)


