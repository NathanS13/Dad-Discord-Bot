import os
import json



def parse_json(path: str, id, data):
    '''
    Parses and returns Json data
    '''
    if not os.path.exists(path):
        print('None path', path)
        return None
    
    print(path)

    with open(path, 'r+', encoding='utf-8') as file:
        js_data = json.load(file)
        try:
            for user in js_data['users']:
                if user['details']['discord_id'] == id:
                    data_ret = user['details'][data]
            print(data_ret)
        except KeyError as e:
            print('Key doesn\'t exist!', e)
    return js_data

def main():
    parse_json(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_year')
    parse_json(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_month')
    parse_json(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'dob_day')
    parse_json(os.path.join(os.getcwd(), 'the_boys.json'), 118156033720844291, 'key_not working!')

if __name__ == '__main__':
    print('main call')
    main()



    