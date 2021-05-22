#!/usr/bin/python3
'''Readme profile generator'''
import requests
import json
from sys import argv

if __name__ == '__main__':
    if len(argv) < 4:
        print('Run this file with your [Api_key] [Email] and [Password]')
    else:
        URL = 'https://intranet.hbtn.io/users'
        headers = {'Content-Type': 'application/json'}
        params = {'api_key': argv[1], 'email': argv[2], 'password': argv[3],
                  'scope': 'checker'}
        reqjson = requests.post('{}/auth_token.json'.
                                format(URL), headers=headers, params=params)
        if '200' not in str(reqjson):
            print(reqjson.json())
            exit()
        token = reqjson.json()
        requser = requests.get('{}/me.json?auth_token={}'.
                               format(URL, token['auth_token']),
                               headers=headers)
        user = requser.json()

    gitread = 'https://github-readme-stats.vercel.app/api'
    badge = 'https://img.shields.io/badge/-'
    linkedin = user['linkedin_url'].split("/")[-2]
    stats = '![GitHub Stats]({}?username={}&theme=default)\n'.format(gitread, user['github_username'])
    say_hi = 'Hi, I´m {} a Software Delevoleper Student at Holberton School!\n'.format(user['full_name'])
    languages = '![Top Langs]({}/top-langs/?username={}&layout=compact&theme=gotham)\n'.format(gitread, user['github_username'])
    twitter = '[![Twitter Badge]({}{}-00acee?style=flat&logo=Twitter&logoColor=white)](https://twitter.com/intent/follow?screen_name={} " Follow on Twitter")\n'.format(badge, user['twitter_username'], user['twitter_username'])
    linkedin = '[![Linkedin Badge]({}{}-blue?style=flat-square&logo=Linkedin&logoColor=white&link={})]({})\n'.format(badge, linkedin, user['linkedin_url'], user['linkedin_url'])

    with open('README.md', 'w') as file:
        file.write(say_hi, twitter, linkedin, stats, languages)
