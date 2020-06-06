import db

if __name__ == "__main__":
    # TODO - Replace the USERNAME and PASSWORD with the login username and password
    admin_cred = {
        "_id": "loginCredentials",
        "username": "USERNAME",
        "password": "PASSWORD",
    }
    db.admin.insert_one(admin_cred)
    cred_count = {
        "_id": "recordSequence",
        "last": 0
    }
    db.admin.insert_one(cred_count)
