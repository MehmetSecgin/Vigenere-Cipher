def cipher():
    msg=input('Please write the message you want to encrypt/decrypt: ')
    key = input('Please give the key: ')
    choise = input('Please write 0 to Encrypt and 1 to Decrypt: ')
    count = 0
    if(choise =="0"):
        for x in msg:
            if(x != " "):
                print(chr(65 + ((ord(x.upper()))+ (ord((key[count%len(key)]).upper())))%26), end ="")
                count+=1
            else:
                print(" ",end="")
    elif (choise =="1"):
        for x in msg:
            if(x !=" "):
                print(chr(65 + ((ord(x.upper()))- (ord((key[count%len(key)]).upper())))%26), end ="")
                count+=1
            else:
                print(" ",end="")
cipher()