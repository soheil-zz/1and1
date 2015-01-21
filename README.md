# 1and1 Tools

1and1 is the best registrar ever except for when it [doesn't work](https://twitter.com/search?q=1and1+ddos) which happens pretty often and the fact that its UI is shit and that there is no API ಥ﹏ಥ, well, what do you expect for $0.99? So STFU and deal with it, here is my attempt to do just that.

## The Never Existing 1and1 API

Python scripts in this repo allow you to automate the tasks of domain registration and DNS modification for 1and1.

### Requirements

- Python
- Webdriver
- Firefox
- Virtual Frame Buffer

Or more succinctly just run this command if you're on ubuntu:

```
sudo apt-get install python-pip xvfb firefox
```

### Login Info

Make sure to change the constants for user name and password at the top of both files to yours.

### Next Step

Yes, now you can run your pretty Python scripts (well actually the ones in this repo.)

#### Register Domain

Usage:
```
python register_domain.py DOMAIN_NAME.COM
```

#### Change Nameservers

Usage:
```
python change_dns.py DOMAIN_NAME.COM ns1 ns2 ns3 ns4
sudo pip install pyvirtualdisplay
sudo pip install selenium
```

You guessed it, I don't even use 1and1 nameservers anymore after their massive DDOS meltdown. I recommend AWS Route 53, it's practicly free and you can change shit using their beautiful UI or API.

## Maker
Give me a hollar [@soheil](https://twitter.com/soheil) if you like this.
