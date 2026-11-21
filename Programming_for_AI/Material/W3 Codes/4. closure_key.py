# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Mar 10 23:56:58 2026

# @author: awais
# """

# def api_client(api_key):
    
#     def get_data(endpoint):
#         print(f"Fetching from {endpoint} using key: {api_key}")
#     return get_data

# # The 'google_service' function now "carries" the key secretly
# google_service = api_client("SECRET_123")
# google_service("/maps")
# facebook_service = api_client("BRO_123")
# facebook_service("/reels")


def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c.__closure__)
print(c.__closure__[0].cell_contents)
print(c())
print(c())
print(c())

def outer():
    x = 100

    def inner():
        print(x)

    return inner


func = outer()

print(func.__closure__)
print(func.__closure__[0].cell_contents)