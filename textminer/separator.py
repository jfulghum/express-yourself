import re


def words(text):
    if len(re.findall(r'[-A-za-z]+', text)) == 0:
        return
    else:
        return re.findall(r'[0-9-A-za-z]+', text)


def phone_number(text):
    phone_dict = {}
    split_list = re.findall(r'[0-9]+', text)
    if len(split_list) == 3:
        phone_dict['area_code'] = split_list[0]
        phone_dict['number'] = split_list[1] + '-' + split_list[2]
        return phone_dict
    elif len(split_list) == 2:
        return None
    elif len(split_list) == 1:
        for item in split_list:
            phone_dict['area_code'] = item[:3]
            phone_dict['number'] = item[3:6] + '-' + item[6:]
        return phone_dict
