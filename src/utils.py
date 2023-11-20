import os
import json

def parse_data(path: str, id, data):
    '''
    Parses and returns Json data
    '''
    if not os.path.exists(path):
        print('None path', path)
        return None

    with open(path, 'r+', encoding='utf-8') as file:
        js_data = json.load(file)
        try:
            for user in js_data['users']:
                if user['details']['discord_id'] == id:
                    data_ret = user['details'][data]
        except KeyError as e:
            print('Key doesn\'t exist!', e)
            return None
    return data_ret

def replace_value(path: str, id, data_key, data_replace):
    '''
    Parses and returns Json data
    '''

    if not os.path.exists(path):
        print('None path', path)
        return None

    with open(path, 'r+', encoding='utf-8') as file:
        js_data = json.load(file)

        user_to_replace = next((user for user in js_data['users'] if user['details']['discord_id'] == id), None)
        print(user_to_replace)

        if user_to_replace and parse_data(path, id, data_key) is not None:
            user_to_replace['details'][data_key] = data_replace
            file.seek(0)
            file.truncate()
            json.dump(js_data, file, indent=2)
            return True

        return False

def batch_user_list(path: str, data_key, expected_data):
    '''
    Parses and returns Json data
    '''
    if not os.path.exists(path):
        print('None path', path)
        return None

    with open(path, 'r', encoding='utf-8') as file:
        js_data = json.load(file)

        user_to_replace = [user['details']['discord_id'] for user in js_data['users'] if user['details'][data_key] == expected_data]
        return user_to_replace


def main():
    print(parse_data(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_year'))
    print(parse_data(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_month'))
    print(parse_data(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_day'))
    print(parse_data(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'key_not working!'))

    #print(replace_value(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'key_not working!'))
    replace_value(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_day', 13)
    replace_value(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_day2', 13)
    replace_value(os.path.join(os.getcwd(), 'the_boys.json'), 1181560337208442911, 'dob_day', 13)

    replace_value(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'plex_tag', True)
    replace_value(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'plex_tag', False)

    batch_user_list(os.path.join(os.getcwd(), 'the_boys.json'), 'plex_tag', False)
    batch_user_list(os.path.join(os.getcwd(), 'the_boys.json'), 'plex_tag', True)


if __name__ == '__main__':
    print('main call')
    main()



    