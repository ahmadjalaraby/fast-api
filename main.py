from fastapi import FastAPI, Request
import json
from hill_cipher_cbc import *
from lazy_decoder import *

# from flask import Flask, jsonify, request
from  rc5_cbc import *
from const import *

app = FastAPI()

@app.get("/rc5/encrypt")
def hello(string = None):
    if string is None:
        text = 'Hello!'

    else:
        t = RC5_CBC_encryption(string, CONST.FINAL_VARIABLE)
        # text = RC5_CBC_decryption(t[0], CONST.FINAL_VARIABLE, t[1])

    return json.dumps(t)


@app.post("/rc5/decrypt")
def hello(t = None):
    if t is None:
        text = 'Hello!'

    else:
        t = json.loads(t)
        # t = RC5_CBC_encryption(string, CONST.FINAL_VARIABLE)
        text = RC5_CBC_decryption(t[0], CONST.FINAL_VARIABLE, t[1])

    return text


@app.get("/hill-cipher/encrypt")
def hello(string = None):
    if string is None:
        text = 'Hello!'

    else:
        blkChain = BlockChain(CONST.KEY,CONST.IV,VernamEncrypt,VernamDecrypt,BlockChain.CBC)
        cipherblks = blkChain.encrypt(string)
        print("\nCBC Ciphertext:")
        # for blk in cipherblks:
            # blk = blk.decode('utf8')

        j = json.dumps(cipherblks, ensure_ascii=False)
        print(cipherblks)

    return cipherblks
    

@app.post("/hill-cipher/decrypt")
async def hello(t = None):
    if t is 'a':
        text = 'Hello!'

    else:
        t = json.loads(t)
        print(t)
        # t = ['Lhnjo"|k', 'P`-W~>Fr', "#\x05N%\x1bJ\x19\x11"]
        
        blkChain = BlockChain(CONST.KEY,CONST.IV,VernamEncrypt,VernamDecrypt,BlockChain.CBC)
        dmsg = blkChain.decrypt(t)
        output = ''
        for ea in dmsg:
            output+=ea
        print(output)

    return output