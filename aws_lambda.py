from aws_requests_auth.aws_auth import AWSRequestsAuth
import requests
import json
import urllib.parse
from requests.auth import HTTPBasicAuth
import requests
from time import sleep


# Get question
# get values
# submit question
# {type: get, q: 1, user: cody} -> status, question, data
# {type: submit, q: 1, user: cody, data: result} -> status, result

class Challenge:

    def __init__(self, prompt, data):
        self.prompt = prompt
        self.q = prompt
        self.question = prompt
        self.data = data

    def __str__(self):
        return f"{self.q} {self.data}"


class Server:

    def __init__(self, url, key, output=True):
        self.url = url
        self.api_key = key
        self.aws_header = {'X-API-KEY': self.api_key}
        self.chatty = output

    def output(self, *args, **kwargs):
        if self.chatty:
            print(*args, **kwargs)

    def get(self, q):
        data = {
            "type": "get",
            "q": q,
            "user": "cody"
        }
        r = requests.post(api_url, headers=self.aws_header, json=data)
        challenge = Challenge(r.json().get('q'), r.json().get('data'))
        self.output(f"\n{challenge}")
        return challenge

    def submit(self, q, answer):
        sleep(.25)
        data = {
            "type": "submit",
            "q": q,
            "user": "cody",
            "data": answer
        }
        self.output(f"Submitting: {answer} for Q{q}")
        r = requests.post(api_url, headers=self.aws_header, json=data)
        self.output(f'{answer} is {"Correct!" if r.json() else "Incorrect"} for Q{q}')

        return r.json()


api_key = 'TemYrAclqJ8z5zv0hLZ7bKaoXMkkGgI4H2PjzQAc'
api_url = 'https://q3yj5ww11i.execute-api.us-east-1.amazonaws.com/default/test-v3'

server = Server(api_url, api_key)


def solve_q0():
    challenge = server.get(0)
    answer = challenge.data
    server.submit(0, answer)


def solve_q1():
    challenge = server.get(1)
    answer = challenge.data[0] + challenge.data[1]
    server.submit(1, answer)


def solve_q2():
    challenge = server.get(2)
    answer = challenge.data[0] * challenge.data[1]
    server.submit(2, answer)


def solve_q3():
    challenge = server.get(3)
    answer = 0
    for i in challenge.data:
        answer += i
    server.submit(3, answer)


def solve_q4():
    challenge = server.get(4)
    answer = "Hello " + challenge.data
    server.submit(4, answer)


def solve_q5():
    challenge = server.get(5)
    answer = challenge.data.lower()
    server.submit(5, answer)


def solve_q6():
    challenge = server.get(6)
    answer = challenge.data.replace(" ", "")
    server.submit(6, answer)


def solve_q7():
    challenge = server.get(7)
    answer = challenge.data[:7]
    server.submit(7, answer)


def solve_q8():
    challenge = server.get(8)
    answer = len(challenge.data)
    server.submit(8, answer)


def solve_q9():
    challenge = server.get(9)
    answer = challenge.data[::-1]
    server.submit(9, answer)


def solve_q10():
    challenge = server.get(10)
    answer = challenge.data[-4:]
    server.submit(10, answer)


# solve_q0()
# solve_q1()
# solve_q2()
# solve_q3()
# solve_q4()
# solve_q5()
# solve_q6()
# solve_q7()
# solve_q8()
# solve_q9()
# solve_q10()

















