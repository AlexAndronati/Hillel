
import requests
import random

codes = [200, 300, 403, 404, 500]


def decorator_maker(attempts):

    def decorator_req(func):
        num_of_requests = 0

        def wrapper():
            nonlocal num_of_requests
            for i in range(5):
                attempt = func()
                print(attempt)
                if attempt != 200:
                    num_of_requests += 1
                else:
                    num_of_requests = 0
                    return "Ok"
            return "Error!"

        return wrapper
    return decorator_req


@decorator_maker(5)
def request_sender():
    code = random.choice(codes)
    r = requests.get(f"https://httpbin.org/status/{code}")

    return r.status_code


if __name__ == "__main__":

    print(request_sender())
