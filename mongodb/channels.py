#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# المطور ,,,,, t.me/shnider_bots

from pymongo import MongoClient
from sample_config import Config

MONGO_URL=Config.MONGO_URL
url, params = MONGO_URL.split("?")

MONGO_URL = url + "?ssl=true&ssl_cert_reqs=CERT_NONE&" + params
client = MongoClient(MONGO_URL)





async def add_channel_to_db(channel_id):
    # Add user to database
    mydb = client.dtu
    mycol = mydb.channels
    channel_id = str(channel_id)
    mydict = {
        "channel Id": "{}".format(channel_id)

    }
    mm = mydb.channels.count_documents({"channel Id": "{}".format(channel_id)})
    add_status = 0
    if mm == 0:
        mycol.insert_one(mydict)
        add_status = 1
    else:
        add_status = 0
    total_channels = len(mycol.distinct("channel Id"))
    client.close()
    return add_status, total_channels


async def channel_list():
    mydb = client.dtu
    mycol = mydb.channels
    broadcast_list = mycol.distinct("channel Id")
    client.close()

    return broadcast_list


async def remove_channel_from_db(channel_id):
    mydb = client.dtu
    mycol = mydb.channels
    mycol.remove({"channel Id": channel_id})
    print("[*] A channels, {} has been deleted!".format(channel_id))
    client.close()


