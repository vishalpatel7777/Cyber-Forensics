import hashlib

text= input('Enter the text to convert into hash : ')
options = int(input('''# Hash Generator  ##
                    Choose Option: 
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    5) Exit
                    '''))

log_file = "hash_log.txt"

def save_log(method , hashed_value):
    with open(log_file, 'a') as f:
        f.write(f"{method} | input :{text} | hash: {hashed_value}\n")

if options == 1 :
    result = hashlib.md5(text.encode('utf-8')).hexdigest()
    print("The generated MD5 Hash is : " , result)
    save_log('MD5', result)

elif options == 2:
    result = hashlib.sha1(text.encode('utf-8')).hexdigest()
    print("The generated SHA1 Hash is : " , result)
    save_log('SHA1',result)

elif options == 3:
    result = hashlib.sha256(text.encode('utf-8')).hexdigest()
    print("The generated SHA256 Hash is : " , result)
    save_log('SHA256',result)

elif options == 4:
    result = hashlib.sha512(text.encode('utf-8')).hexdigest()
    print("The generated SHA512 Hash is : " , result)
    save_log('SHA512', result)

elif options == 5:
    exit()

else:
    print('something went wrong')
