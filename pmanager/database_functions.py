import db
import math


def validate_login(username, password):
    result = db.admin.find_one({'_id': 'loginCredentials', 'username': username, 'password': password})
    if result:
        return result
    else:
        return 0


def add_record(data):
    result = db.admin.find_one({'_id': 'recordSequence'})
    data['_id'] = result['last']
    db.data.insert_one(data)
    db.admin.update_one({'_id': 'recordSequence'}, {'$set': {'last': result['last'] + 1}})


def update_record(data):
    db.data.update_one({'_id': data['_id']},
                       {'$set': {'email_username': data['email_username'], 'website': data['website'],
                                 'password': data['password']}})


def delete_record(_id):
    db.data.delete_one({'_id': _id})


def page_records(page_no=1):
    records = []
    result = db.data.find().limit(page_no * 10)
    total_records = db.data.find().count()
    total_page = math.ceil(float(total_records) / 10)
    previous_page = page_no - 1
    next_page = page_no + 1
    for x in result:
        records.append(x)
    records_info = {"records": records[page_no * 10 - 10:page_no * 10], "total_page": int(total_page),
                    "page_no": page_no,
                    "previous_page": previous_page, "next_page": next_page}
    return records_info


def uppercase_word(word):
    return word.upper()


def search(keywords, page_no):
    search_result = []
    keywords = list(map(uppercase_word, keywords.split(' ')))
    records = db.data.find()
    for x in records:
        website = list(map(uppercase_word, x['website'].split('.')))
        for y in keywords:
            if y in website:
                if x not in search_result:
                    search_result.append(x)
    total_records = len(search_result)
    total_page = math.ceil(float(total_records) / 10)
    previous_page = page_no - 1
    next_page = page_no + 1
    records_info = {"records": search_result[page_no * 10 - 10:page_no * 10],
                    "total_page": int(total_page),
                    "page_no": page_no,
                    "previous_page": previous_page, "next_page": next_page}
    return records_info
