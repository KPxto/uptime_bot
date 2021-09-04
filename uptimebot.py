import time
import urllib.request


# Have a loop that queries url
def uptime_bot(url, retries=3):
    # variable that counts the number of fails
    # in case the fails reaches the number of trials
    # it will do something else
    fails = 0
    while fails < retries:
        try:
            urllib.request.urlopen(url)
        except Exception as e:
            # we increment number of fail anytime code run
            # into exception
            fails += 1
            print(f"{e}: for {url}")
        else:
            print(f"success :) {url} is up!")
        time.sleep(3) 
    # Send Email


if __name__ == "__main__":
    url = "https://docs.python.org/3/drf"
    uptime_bot(url)