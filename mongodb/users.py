#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# المطور ,,,,, t.me/shnider_bots
from pymongo import MongoClient
from sample_config import Config

MONGO_URL=Config.MONGO_URL
url, params = MONGO_URL.split("?")
MONGO_URL = url + "?ssl=true&ssl_cert_reqs=CERT_NONE&" + params
client = MongoClient(MONGO_URL)




async def add_client_to_db(chat_id):
    # Add user to database
    mydb = client.dtu
    mycol = mydb.users
    chat_id = str(chat_id)
    mydict = {
        "Chat Id": "{}".format(chat_id)

    }
    mm = mydb.users.count_documents({"Chat Id": "{}".format(chat_id)})
    add_status = 0
    if mm == 0:
        mycol.insert_one(mydict)

        add_status = 1
    else:
        add_status = 0
    total_users = len(mycol.distinct("Chat Id"))
    client.close()
    return add_status, total_users


async def user_list():
    mydb = client.dtu
    mycol = mydb.users
    broadcast_list = mycol.distinct("Chat Id")
    client.close()
    return broadcast_list



async def remove_client_from_db(chat_id):
    mydb = client.dtu
    mycol = mydb.users
    mycol.remove({"Chat Id": chat_id})
    print("[*] A user, {} has been deleted!".format(chat_id))
    client.close()
