import os

username = os.environ["USER"]
os.mkdir("./" + username[:6])
