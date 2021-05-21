#!/usr/bin/python3

import requests


if __name__ == '__main__':

    def get_data(username='', dev_name='', twitter='_', linkedin='_'):
        git_stats = '![GitHub Stats](https://github-readme-stats.vercel.app/api?username=' + \
            username + '&theme=default)'

        say_hi = 'Hi, I´m ' + dev_name + \
            ', a Software Delevoleper Student at Holberton School!\n'

        most_used_lenguages = '![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=' + \
            username + '&layout=compact&theme=gotham)\n'

        twitter = '[![Twitter Badge](https://img.shields.io/badge/-' + twitter + \
            '-00acee?style=flat&logo=Twitter&logoColor=white)](https://twitter.com/intent/follow?screen_name=' + \
            twitter + ' " Follow on Twitter")\n'

        linkedin = '[![Linkedin Badge](https://img.shields.io/badge/-' + linkedin + \
            '-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wisvem/)](https://www.linkedin.com/in/' + \
            linkedin + '/)\n'

        with open('file', 'w') as file:
            file.write(say_hi)
            if twitter == '_':
                file.write(twitter)
            if linkedin == '_':
                file.write(linkedin)
            file.write(git_stats)
            file.write(most_used_lenguages)
