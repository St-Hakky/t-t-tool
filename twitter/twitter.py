#-*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import sqlite3
import twitkey
import json

# タイムライン取得用のURL
url_get_timeline = "https://api.twitter.com/1.1/statuses/home_timeline.json"

def printReqLimit(req):
    # API残り
    limit = req.headers['x-rate-limit-remaining']
    # API制限の更新時刻 (UNIX time)
    reset = req.headers['x-rate-limit-reset']

    print ("API remain: " + limit)
    print ("API reset: " + reset)


# 認証、APIの取得
def createOath():
    CONSUMER_KEY = twitkey.twkey['cons_key']
    CONSUMER_SECRET = twitkey.twkey['cons_sec']
    ACCESS_TOKEN_KEY = twitkey.twkey['accto_key']
    ACCESS_TOKEN_SECRET = twitkey.twkey['accto_sec']

    oath = OAuth1Session(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET
    )
    return oath

# すべての友達を取得
def getAllFriends(oath):
    print ("getAllFriends")
    url = "https://api.twitter.com/1.1/friends/list.json"
    params = {"count":200}
    friends_id_list = []
    while True:
        req = oath.get(url, params = params)
        if req.status_code == 200:
            printReqLimit(req)
            list_friend = json.loads(req.text)
            for i in list_friend['users']:
                friends_id_list.append(i)

            # next_cursorがもうない時
            if list_friend['next_cursor'] == 0:
                return friends_id_list
                break
            else:
                params = {"count":200, "cursor":list_friend['next_cursor_str']}
        elif req.status_code == 429:
            print ("429 error occur")
            return friends_id_list


# すべてのフォロワーを取得
def getAllFollowersId(oath):
    print ("getAllFollowers")
    url = "https://api.twitter.com/1.1/followers/ids.json"
    params = {}
    followes_id_list = []
    while True:
        req = oath.get(url, params = params)
        if req.status_code == 200:
            printReqLimit(req)

            # TODO フォロワー数が5000を超えたらcurserを考慮に入れること
            list_followers = json.loads(req.text)
            followes_id_list += list_followers['ids']
            if list_followers['next_cursor'] == 0:
                return followes_id_list
            else:
                params = {"cursor":list_friend['next_cursor_str']}
        elif req.status_code == 429:
            print ("429 error occur")
            return followes_id_list

def getAllFriendsId(oath):
    print("getAllFriendsId")
    url = "https://api.twitter.com/1.1/friends/ids.json"
    params = {}
    friends_id_list = []
    while True:
        req = oath.get(url, params = params)
        if req.status_code == 200:
            printReqLimit(req)

            # TODO フォロワー数が5000を超えたらcurserを考慮に入れること
            list_frineds = json.loads(req.text)
            friends_id_list += list_frineds['ids']
            if list_frineds['next_cursor'] == 0:
                return friends_id_list
            else:
                params = {"cursor":list_friend['next_cursor_str']}
        elif req.status_code == 429:
            print ("429 error occur")
            return friends_id_list

# すべての友達申請を取得
def getAllFriendshipRequests(oath):
    print ("getAllFriendshipRequests")
    url = "https://api.twitter.com/1.1/friendships/incoming.json"

def destroyFriendships(oath, account_list):
    print ("destroyFriendships")
    url = "https://api.twitter.com/1.1/friendships/destroy.json"
    for account in account_list:
        params = {"user_id":account}
        req = oath.post(url, params = params)

def followNewAccounts(oath,account_list):
    print ("followNewAccounts")
    url = "https://api.twitter.com/1.1/friendships/create.json?follow=true"
    for account in account_list:
        params = {"user_id":account}
        req = oath.post(url, params = params)

def getFriendsFromUserId(oath, user_id):
    print ("getFriendsFromUserId")
    url = "https://api.twitter.com/1.1/friends/list.json"
    params = {"user_id":user_id}
    req = oath.get(url, params = params)
    printReqLimit(req)
    account_info = json.loads(req.text)
    return account_info

def getFollowesFromUserId(oath, user_id):
    print ("getFollowesFromUserId")
    url = "https://api.twitter.com/1.1/followers/ids.json"
    params = {"user_id":user_id}
    req = oath.get(url, param)
    printReqLimit(req)
    account_info = json.loads(req.text)
    return account_info

def getTweetTime(oath, user_id):
    print ("getTweetTime")
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {"user_id":user_id}
    req = oath.get(url, params = params)
    printReqLimit(req)
    tweet_info = json.loads(req.text)
    return tweet_info["created_at"]

if __name__ == "__main__":
    # DBへの接続
    conn = sqlite3.connect('./sqlite.db')

    # カーソルの作成
    cur = conn.cursor()

    cur.execute("""CREATE TABLE user(user_id text, follow_time text);""")



    oath = createOath()
    frineds_list = getAllFriendsId(oath)
    followers_list = getAllFollowersId(oath)
    friends_not_in_followers = []
    followers_not_in_friends = []
    for friend_id in frineds_list:
        if friend_id not in followers_list:
            friends_not_in_followers.append(friend_id)
    for follower_id in followers_list:
        if follower_id not in frineds_list:
            followers_not_in_friends.append(follower_id)

    print("friends_not_in_followers")
    print(friends_not_in_followers)
    print(len(friends_not_in_followers))
    print("followers_not_in_friends")
    print(followers_not_in_friends)
    print(len(followers_not_in_friends))

    destroyFriendships(oath, friends_not_in_followers)
    followNewAccounts(oath, followers_not_in_friends)



    """followers_list = getAllFollowers(oath)
    match_list = []
    mismatch_list = []
    for friend_id in frineds_list:
        match_list    += filter(lambda int: int == friend_id, followers_list)
        mismatch_list += filter(lambda int: int != friend_id, followers_list)

    print ("match_list")
    print (match_list)
    print (mismatch_list[0])
    info = getFriendsFromUserId(oath, mismatch_list[0])
    user = info['users']
    #print user
    #print user['name']
    #print user['id_str']
    print (getTweetTime(oath, mismatch_list[0]))"""
