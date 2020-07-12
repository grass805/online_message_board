# online_message_board

## Overview
using flask framework to build an online message board and deploy to AWS-EC2

## Result
website URL: http://ec2-54-168-200-241.ap-northeast-1.compute.amazonaws.com

![](https://github.com/grass805/online_message_board/blob/master/screeshot/screenshot1.jpg)

## Deployment
Amazon Linux AMI ec2-user

1.create a project directory 
```bash
~$ mkdir FOLDER
```

2. create a virtual environment (virtualenv) 
```bash
# with python3
~$ virtualenv VIRT --python=python3

# activate virtual environment
~$ source VIRT/bin/activate
```

3. download the codes or git clone
```bash
~$ git clone git@github.com:grass805/online_message_board.git
```

4. overall directory structure
```
FOLDER
|--VIRT
|--.flaskenv          # flask environment variables
|--requirements.txt   # application dependencies
|--msgboard
   |--templates       # html files
   |--static          # CSS and JavaScript files
   |--__init__.py
   |--......  .py
   
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
# root shell
~$ sudo su 

# run the application on port 80
~$ flask run --host='0.0.0.0' --port=80
```

```bash
*Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```





----------------------------------------------------------
## Reference

《Flask Web 开发实战》
https://github.com/greyli/sayhello










