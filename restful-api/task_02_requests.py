import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)


def fetch_and_print_posts():

    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for i in posts:
            print("Title: {}".format(i['title']))


def fetch_and_save_posts():
    if response.status_code == 200:
        posts = response.json()
        data = [{'id': post['id'], 'title': post['title'],
                'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
