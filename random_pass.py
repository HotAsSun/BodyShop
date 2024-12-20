import random
def random_pass_generator():
    random_password = ""
    for i in range(8):
        num = random.randint(97,121)
        random_password += chr(num)
        return random_password
