import requests
import argparse


def send_requests(url):

    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"}
    verbs = ["GET", "POST", "PUT", "PATCH", "HEAD", "OPTIONS", "DELETE"]

    for verb in verbs:
        try:
            response = requests.request(verb, url, headers=headers)
            check_response(response)
        except requests.exceptions.ConnectionError:
            print("error")
            continue


def check_response(res):
    word_length = len(res.content.decode())
    verb = str(res.request).replace("PreparedRequest", "")
    verb = verb.strip("<> ")
    headers = res.headers['server']

    print(
        f'\n{verb} Status: ({res.status_code} Size: {word_length}) \n Server: {headers}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url", type=str, help="http://example.com or https://example.com")
    args = parser.parse_args()
    url = args.url
    if url == None:
        print("Enter a url")
        exit(0)

    send_requests(url)


if __name__ == '__main__':
    main()
