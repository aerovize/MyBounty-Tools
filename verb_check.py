import requests
import argparse


def send_requests(url):
    responses = []
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"}
    verbs = ["GET", "POST", "PUT", "PATCH", "HEAD", "OPTIONS", "DELETE"]

    for verb in verbs:
        try:
            response = requests.request(verb, url, headers=headers)
            responses.append(response)
        except requests.exceptions.ConnectionError:
            print("error")
            continue

    return responses


def response_parser(resp):
    class color:
        Bold = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    for r in resp:

        verb = str(r.request).replace("PreparedRequest", "").strip("<> ")
        resp_size = len(r.content.decode())
        headers = r.headers

        print(
            f"{color.Bold}{verb}{color.END}\n Status Code: {r.status_code}\n Size: {resp_size}")
        for key, value in headers.items():
            print(f" {key}: {value}")
        print("\n")


def main():
    parser = argparse.ArgumentParser(description="http method checker")
    parser.add_argument(
        "url", type=str, help="http://example.com or https://example.com")
    args = parser.parse_args()
    url = args.url

    if not url or "http" not in url:
        print("Enter a url")
        exit(0)

    resp = send_requests(url)
    response_parser(resp)


if __name__ == '__main__':
    main()
