import time

# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

attempt = 0
retries = 5
wait = 1

while attempt < retries:
    print(f"Attempt: {attempt} -wait {wait}")
    attempt +=1
    wait *= 2
    time.sleep(wait)    
