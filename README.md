# flask-simple-api
A simple Flask API for floating point arithmetic operations.

Input: Two numbers. `a` and `b`
Output: A float number

Modulo is not supported.

Pytest is used for testing. 

Demonstrates the usage of `pytest.mark.parametrize()` for parametrizing tests. When stacked one after the other, all the parameter value combinations are used for the tests.

A pytest fixture is used to maintain the test client.

## Running development server
A server can be run in debug mode (with hot reloading enabled) with

    FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run

By default port 5000 is used. So the address would be something like 

    localhost:5000

## Testing with curl
GET requests: (not verified)

    curl localhost:5000/add?a=3&b=4 # 7.0
    curl localhost:5000/sub?a=3&b=4 # -1.0
    curl localhost:5000/mult?a=3&b=4 # 12.0
    curl localhost:5000/div?a=3&b=4 # 0.75
    curl localhost:5000/div?a=3&b=0 # Error: Cannot divide by zero

POST requests: (not verified)

    curl -X POST localhost:5000/mult?a=3&b=4

Or just use Postman.

---

## Using Docker

The containerised version can be used by building with

    sudo docker build -t sapi:0.1 .

where `-t` option "allocates a pseudo tty". `sapi` is the name and `0.1` is the version.

The container can then be run with

    sudo docker run -it -p 5000:5000 sapi:0.1

where

 - `-i` option is to run the container in a 'non-detached mode'. ie, it will "keep STDIN open even if not attached".
 - `-p` is to publish a container's port to host interface in the following format:

    ip:hostPort:containerPort | ip::containerPort | hostPort:co
