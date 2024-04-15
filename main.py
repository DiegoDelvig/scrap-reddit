import requests
import database
import sys

def parseURL(url):
    if ('i.redd.it' in url):
        url = url.split('/')[3]
        url = url.split('.')[0] + url.split('.')[1]
        return url



def parse(subreddit, after=''):
    url_template = 'https://www.reddit.com/r/{}/hot.json?t=all{}'
 
    headers = {
        'User-Agent': 'VirboxBot'
    }
 
    params = f'&after={after}' if after else ''
 
    url = url_template.format(subreddit, params)
    response = requests.get(url, headers=headers)

    data = response.json()['data']
    for post in data['children']:
        pdata = post['data']
        img = pdata['url']
        print(img)
        if (parseURL(img) != None):
            database.add(True, f'{subreddit}/' + parseURL(img))


        return data['after']
    else:
        print(f'Error {response.status_code}')
        return None


def main():
    subreddit = sys.argv[1]
    after = " "
    database.connect()

    try:
        while True:
            after = parse(subreddit, after)
            if not after:
                break
    except KeyboardInterrupt:
        print('Exiting...')
 
if __name__ == '__main__':
    main()


