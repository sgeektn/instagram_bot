#!/bin/python3

import instaloader
import sys


def get_instagram_followers(username,password,account):
    L = instaloader.Instaloader()
    L.login(username, password) 

    self_profile = instaloader.Profile.from_username(L.context, username)
    self_followees = [ followee.username for followee in self_profile.get_followees() ]
    self_followers = [ follower.username for follower in self_profile.get_followers() ]

    profile = instaloader.Profile.from_username(L.context, account)
    result = [ follower.username for follower in profile.get_followers() if follower.username not in self_followees and follower.username not in self_followers ]
    print('\n'.join(result))
    return result


if __name__ == '__main__':
    get_instagram_followers('sami_fakhfakh','zatla123birra',sys.argv[1])
