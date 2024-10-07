import time

attempt=0
max=5
retries=1

while(attempt<max):
    print("Attempt: ",attempt+1 ,"-Wait for ",retries ,"sec")
    time.sleep(retries)
    retries=2*retries
    attempt+=1