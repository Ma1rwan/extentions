import requests

with open("proxies.txt", "r", encoding="utf-8") as prxsfile:
    proxy_list = prxsfile.read().split("\n")

with open("httpsWorkingProxies.txt", "a")as file1:

    def check_https_proxy(proxy):
        """Check if a proxy works with HTTPS by sending a test request."""
        proxies = {
            'https': f'http://{proxy}'  # Test HTTPS traffic through the proxy
        }
        
        try:
            # Send a request to an HTTPS site (e.g., https://httpbin.org/ip) with a timeout
            response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=5)
            
            # If the request is successful (status code 200), the proxy is working for HTTPS
            if response.status_code == 200:
                print(f"Working HTTPS proxy: {proxy}")
                file1.write(proxy+"\n")
                return True
        except requests.RequestException:
            # If any exception occurs (connection error, timeout, etc.), the proxy is not working for HTTPS
            print(f"Bad HTTPS proxy: {proxy}")
            return False

    # Filter only the proxies that work with HTTPS
    working_https_proxies = [proxy for proxy in proxy_list if check_https_proxy(proxy)]

    print(f"Working HTTPS proxies: {working_https_proxies}")
