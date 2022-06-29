import requests
import hashlib
import sys

def request_api(query_char):
    url ='https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError({res.status_code})
    return res

def pwned_leaks_count(hashes,hash_to_count):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,c in hashes:
        if h == hash_to_count:
            return c
    return 0

def pwned_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5,tail = sha1password[:5],sha1password[5:]
    response = request_api(first5)
    return pwned_leaks_count(response,tail)

def main(args):
    for password in args:
        c = pwned_api(password)
        if c:
            print(f'{password} has been found {c} no. of times,please change it')
        else:
            print(f'{password} not found,carry on!')


if __name__ == '__main__':
 sys.exit(main(sys.argv[1:]))











