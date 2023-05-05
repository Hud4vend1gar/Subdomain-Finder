class Subdomain_Finder():
    def __init__(self,url,wordlist = "wordlist.txt") -> None:

        self.input_url = str(url)
        self.input_url = self.input_url.strip()
        self.wordlist = wordlist
        

    def check_domains(self):
        import requests      

        #google.com
        with open(file=f"app/{self.wordlist}",mode="r") as subdomains:
            for word in subdomains:
                word = word.strip()
                subdomain_url = f"http://{word}.{self.input_url}"

                try:
                    requests.get(url=subdomain_url)
                    print(f"[+] {subdomain_url}")
                
                except:                    
                    continue

    def check_network(self):

        import urllib.request

        def connect():
            try:
                urllib.request.urlopen("http://google.com") #Python 3.x
                return True
            except:
                return False  

        if connect() == True:
            pass
        else:
            print("\n --> Please check your connection and try again ...\n")


            
