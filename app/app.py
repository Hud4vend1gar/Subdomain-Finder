class Subdomain_Finder():
    def __init__(self,url,wordlist = "wordlist.txt") -> None:

        self.input_url = url
        self.wordlist = wordlist
        

    def check_domains(self):
        import requests        
        #google.com
        with open(file=f"app/{self.wordlist}",mode="r") as subdomains:
            for word in subdomains:
                word = word.strip()
                subdomain_url = f"http://{word}.{self.input_url}"

                try:
                    check_subdomain = requests.get(url=subdomain_url)
                    print(f"[+] {subdomain_url}")
                
                except:
                    continue
            
