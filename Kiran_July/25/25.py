import pickle
l=["sanket","sai","ram"]
bs=pickle.dumps(l)
print(bs)#b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x06sanket\x94\x8c\x03sai\x94\x8c\x03ram\x94e.'

po=pickle.loads(bs)
print(po)#['sanket', 'sai', 'ram']