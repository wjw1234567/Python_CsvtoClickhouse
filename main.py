# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    columns_def=['`profile_id` Int64', '`person_id` String', '`profile_type` Int64', '`member_tier` String',
                  '`member_id` String', '`is_delete` Int64', '`person_status` Int64', '`album_id` String',
                  '`merge_count` Int64', '`face_count` Int64', '`identify_num` String', '`card_type` String',
                  '`address` String', '`name` String', '`age` Int64', '`gender` Int64', '`cover_page_image_uri` String',
                  '`cover_page_img_face_id` String', '`gmt_create` String', '`gmt_update` String']

    print({', '.join(columns_def)})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
