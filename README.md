# online_message_board

## Overview
using flask framework to build an online message board and deploy to AWS-EC2

## Result
website URL: http://ec2-54-168-200-241.ap-northeast-1.compute.amazonaws.com  

![](https://github.com/grass805/online_message_board/blob/master/screeshot/screenshot1.jpg)

## Deployment
Amazon Linux AMI ec2-user


1. download the codes or git clone
```bash
~$ git clone git@github.com:grass805/online_message_board.git

~$ cd online_message_board
```

2. create a virtual environment (virtualenv) 
```bash
# enter root shell
~$ sudo su 

# with python3
~$ virtualenv VIRT --python=python3
```


3. overall directory structure
```
online_message_board
|--VIRT
|--.flaskenv          # flask environment variables
|--requirements.txt   # application dependencies
|--msgboard
   |--templates       # html files
   |--static          # CSS and JavaScript files
   |--__init__.py
   |--......  .py
   
```

4. activate virtual environment
```bash
# activate virtual environment
~$ source VIRT/bin/activate
```

5. install python packages
```bash
~$ pip install -r requirements.txt
```



6. deployment
```bash
~$ cd msgboard
```

```bash
# generate fake data
~$ flask forge
```

```bash
# run the application on port 80
~$ flask run --host='0.0.0.0' --port=80
```

```bash
*Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```


## notice
if you want to keep the connection,
which means performing a long-running task on a remote machine,
plz run the process in a Screen session.

https://linuxize.com/post/how-to-use-linux-screen/






----------------------------------------------------------
## Reference

李辉《Flask Web 开发实战》











