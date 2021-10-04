import argparse, sys, subprocess

def proto_check(url):
    try:
        domain_check = subprocess.run([f"node greenenergy.js '{url}' get_full_url"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, shell=True)
        final_url = domain_check.stdout.rstrip()
        if "Error" not in final_url:
            if "?" in final_url:
                proto_pollution_check = subprocess.run([f"node greenenergy.js '{final_url}&__proto__[prototype]=pollution&__proto__.prototype=pollution'"], stdout=subprocess.PIPE, text=True, shell=True)
                if "Error" not in proto_pollution_check.stdout and "[+]" in proto_pollution_check.stdout:
                    print(f'\033[92m[+] {final_url} appears to be vulnerable!\033[0m')
                else:
                    proto_pollution_constructor_check = subprocess.run([f"node greenenergy.js '{final_url}&constructor[prototype][prototype]=pollution'"], stdout=subprocess.PIPE, text=True, shell=True)
                    if "Error" not in proto_pollution_constructor_check.stdout and "[+]" in proto_pollution_constructor_check.stdout:
                        print(f'\033[92m[+] {final_url} appears to be vulnerable!\033[0m')
            else:
                proto_pollution_check = subprocess.run([f"node greenenergy.js '{final_url}?__proto__[prototype]=pollution&__proto__.prototype=pollution'"], stdout=subprocess.PIPE, text=True, shell=True)
                if "Error" not in proto_pollution_check.stdout and "[+]" in proto_pollution_check.stdout:
                    print(f'\033[92m[+] {final_url} appears to be vulnerable!\033[0m')
                else:
                    proto_pollution_constructor_check = subprocess.run([f"node greenenergy.js '{final_url}?constructor[prototype][prototype]=pollution'"], stdout=subprocess.PIPE, text=True, shell=True)
                    if "Error" not in proto_pollution_constructor_check.stdout and "[+]" in proto_pollution_constructor_check.stdout:
                        print(f'\033[92m[+] {final_url} appears to be vulnerable!\033[0m')
        else:
            print("[!] Puppeteer returned an invalid URL.  Skipping...")
    except Exception as e:
        print(f"[!] EXCEPTION: {e}")

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', help='Check a Single URL', required=False)
    parser.add_argument('-uL','--ulist', help='Check a List of URLs', required=False)
    parser.add_argument('-v','--verbose', help='Include Verbose Output', required=False, action='store_true')
    return parser.parse_args()

def check_args(args):
    if not args.url and not args.ulist:
        print("[!] Please provide either a URL (-u|--url) or URL List ('uL|--ulist)!")
        sys.exit(1)

def check_single_url(args):
    proto_check(args.url)

def check_url_list(args):
    url_list = open(args.ulist, 'r')
    urls = url_list.readlines()
    length = len(urls)
    print(f"[-] Scanning {length} URLs for Prototype Pollution...")
    for url in urls:
        url_rstrip = url.rstrip()
        if url[0:4] == "http":
            if args.verbose:
                print(f"[-] Checking {url_rstrip}")
            proto_check(url_rstrip)
        else:
            if args.verbose:
                print(f"[-] Checking http://{url_rstrip}")
            proto_check(f"http://{url_rstrip}")
            if args.verbose:
                print(f"[-] Checking https://{url_rstrip}")
            proto_check(f"https://{url_rstrip}")

if __name__ == '__main__':
    args = arg_parse()
    check_args(args)
    print("[-] Beginning \033[92mGreen Energy\033[0m Scan for Prototype Pollution...")
    if args.url:
        check_single_url(args)
    if args.ulist:
        check_url_list(args)
