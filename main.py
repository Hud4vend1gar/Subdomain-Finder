from app import app

if __name__ == "__main__":
    input_url = input("Enter a URL like google.com: ")
    program = app.Subdomain_Finder(url=input_url)
    program.check_network()
    program.check_domains()