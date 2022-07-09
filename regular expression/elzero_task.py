import re

# task 2
def search_string():
    my_string="EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
    search=re.search('L(Elzero)',my_string)
    print(search)

# t3
def search_number():
    my_number='''
    +(0100) 600-1234
    +(0100) 60-1234
    (0100) 6000-1234
    01006001234
    0100 600 1234
    (0100) 600-1
    (0100) 600-12
    '''
    search=re.findall('(\+?\(\d+\)\s\d+-\d{3,})',my_number)
    print(search)

# t4
def search_website():
    my_web='''
    http://www.elzero.org:8888/link.php
    https://elzero.org:8888/link.php
    http://www.elzero.com/link.py
    https://elzero.com/link.py
    http://www.elzero.net
    https://elzero.net
    '''
    search=re.findall('(https?://)(www.)?(\w+)(.\w+)(:\d+)?(/\w+.\w+)',my_web)
    valid_site=[]

    
    if search !=valid_site:
        valid_site.append(search)
        # print("valid site: ",valid_site[0])
        print(len(valid_site))
    for site in valid_site:
        # print(site)
        for i in range(len(site)):
            print(f"the link of website =>{''.join(site[i][:])}")

search_website()