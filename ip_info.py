#!/usr/bin/python3
from colorama import Fore
from colorama import init
init(autoreset = True)
import requests
import ipinfo, random , sys , time


class Whois_Ip(object):
    def __init__(self, ip):
        self.ip = ip
        # pass
    def token(self):
        token =random.choice(['2111c655baec9d', '4739a4a4d565ae',
                              'f27228a07e8887', '4d1d7f0646f6a5',
                              'd9feb34c01672a','7086838867b4f0',
                              'ee44d553cc8fd4', 'e0d0d5c26a960e',
                              '7c9b5904191f80', '760ba3b2eac4b4'])
        return token

    banner_t = """     
    
                +++++++++++++++++++++++++++++++++++++++++++++++++++++
                #    Ip_Info                                        #
                #    Version 0.1                                    #
                #    Ip_info : https://github.com/reza-tanha/       #
                #    Telegram : T.me/S3CURITY_GARY                  #
                #    Youtube : https://bit.ly/2yas3rm               #
                #    Code By : Haji (Reza)                          #
                #                                                   #
                #    Gray Security Team                             #
                +++++++++++++++++++++++++++++++++++++++++++++++++++++
    
        """
    def banner(self):
        for x in self.banner_t:
            print(Fore.LIGHTYELLOW_EX+x, end='', flush=True)
            time.sleep(0.0003)
        print()


    def whois_ip(self):
        handler =  ipinfo.getHandler(self.token())
        handler =  ipinfo.getHandler(self.token())
        details = handler.getDetails(self.ip)
        x_details = details.all
        for key, value in x_details.items():
            if type(value) is dict:
                for k , v in value.items():
                    print(Fore.GREEN + k + Fore.RED + " : ", Fore.CYAN + v)
                    time.sleep(0.1)
            else:
                print(Fore.GREEN+key+Fore.RED+" : ",Fore.CYAN+value)
                time.sleep(0.1)
        try:
            a = details.latitude
            b = details.longitude
            map_1 = "https://www.google.com/maps/place/"+a+b+"/@"+a+","+b
        except:
            pass
        try:
            r = requests.post("https://cleanuri.com/api/v1/shorten",
                              data={"url": map_1})
            map = r.json()['result_url']
            print(Fore.GREEN+"Google Map location : "+Fore.CYAN+map)
        except:
            print(Fore.RED + "Not Found Google Map location : ")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        w = Whois_Ip(sys.argv[1])
        w.banner()
        w.whois_ip()
    else:
        w = Whois_Ip('0.0.0.0')
        w.banner()
        print(Fore.LIGHTCYAN_EX+ "\t\tusage : python3 who-ip.py 0.0.0.0\n\n")
