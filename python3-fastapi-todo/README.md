# python3-fastapi-todo

First thing, if you are a Linux's user, you need some dependencies like: **python3-pip** and **python3-venv**.

To install these dependencies run this command:
```bash
$ sudo apt install python3-venv python3-pip
```

To install all the dependencies that are needed on this project, run these commands:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

To build and run the backend, run this command:
```bash
$ uvicorn main:run
```
