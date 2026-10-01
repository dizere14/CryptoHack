from pwn import *

k1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k2_k1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
k2_k3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
f_k1_k2_k3 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

rk1 = bytes.fromhex(k1)
rk2_k1 = bytes.fromhex(k2_k1)
rk2_k3 = bytes.fromhex(k2_k3)
rf_k1_k2_k3 = bytes.fromhex(f_k1_k2_k3)

rk2 = xor(rk2_k1,rk1)
rk3 = xor(rk2_k3,rk2)
rf = xor(rf_k1_k2_k3,rk1,rk2,rk3)

print(rf)