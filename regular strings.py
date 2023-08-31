import re
def task_1(s1: str):
    return re.findall(r'rb*r', s1.lower())
def task_2(s2: str):
    if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}', s2):
        return True
    else:
        return False
def task_3(s3: str):
    if re.match(r'^[a-zA-Z0-9][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$', s3):
        return True
    else:
        return False
def task_4(s4):
    if re.fullmatch(r'^[a-zA-Z0-9]{2,10}$', s4):
        return True
    else:
        return False
s1 = 'abcRbbrabc'
s2 = '9999-9999-9999-9999'
s3 = 'test_email-@gmail.com'
s4 = 'login1234'
print(task_4(s4))