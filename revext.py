import argparse
import requests
import re
import sys

def gen_header():
    print(r"""

───────────────────────────────────────────────────────────────────────────────────────────────────
─████████████████───██████████████─██████──██████─██████████████─████████──████████─██████████████─
─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─
─██░░████████░░██───██░░██████████─██░░██──██░░██─██░░██████████─████░░██──██░░████─██████░░██████─
─██░░██────██░░██───██░░██─────────██░░██──██░░██─██░░██───────────██░░░░██░░░░██───────██░░██─────
─██░░████████░░██───██░░██████████─██░░██──██░░██─██░░██████████───████░░░░░░████───────██░░██─────
─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─────██░░░░░░██─────────██░░██─────
─██░░██████░░████───██░░██████████─██░░██──██░░██─██░░██████████───████░░░░░░████───────██░░██─────
─██░░██──██░░██─────██░░██─────────██░░░░██░░░░██─██░░██───────────██░░░░██░░░░██───────██░░██─────
─██░░██──██░░██████─██░░██████████─████░░░░░░████─██░░██████████─████░░██──██░░████─────██░░██─────
─██░░██──██░░░░░░██─██░░░░░░░░░░██───████░░████───██░░░░░░░░░░██─██░░░░██──██░░░░██─────██░░██─────
─██████──██████████─██████████████─────██████─────██████████████─████████──████████─────██████─────
───────────────────────────────────────────────────────────────────────────────────────────────────
------------------- Revext version v0.1. -------------------
Created by: David "cybercitizen7" Kasabji
Twitter: @cybercitizen7
Date Created: 11.09.2020
Revext is a simple tool to convert Extensions IDs into Extensions Names.

DISCLAIMER: Currently it only supports CHROME Extensions.

For more information type revext.py -h or revext.py -i
    """)

def show_info():
    print("""
    In cybsercurity it comes time when you would like to fetch installed Extensions on ones endpoint.
    Installed extensions (located on default paths) are stored with weird naming, which is infact the Extension ID (tested for Google Chrome).
    This tools helps you convert that Extension ID into Extension Name.
    
    It is known that some extensions may be outdated or just vulnerable. Such information can be beneficial for red-teamers and blue-teamers.

    CURRENTLY SUPPORTS ONLY CHROME EXTENSIONS!
    """)

def parse_extension_name(extension_id):
    CHROME_WEBSTORE_HOOK = "https://chrome.google.com/webstore/detail/"
    url = CHROME_WEBSTORE_HOOK + extension_id
    try:
        response = requests.get(url)
        ext_name = re.findall(r".*\/(.*)\/", response.url)

        print("Extension Name:" + ext_name[0])
    except requests.exceptions.RequestException as e:
        print("Error occured during request: {}".format(e))


def main():
    gen_header()
  
    try:
        parser = argparse.ArgumentParser(description='Revextid is a small tool to ')
        parser.add_argument("-id", "--ext-id", help="Extension ID you want to reverse")
        parser.add_argument("-l", "--ext-id-list", nargs='+', help="Extension ID list format")
        parser.add_argument("-i", "--info", help="Provides more information on the Tool.")
    except SystemExit:
        raise
    except:
        print("Wrong argument provided!")
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.info:
        show_info()
    elif args.ext_id:
        parse_extension_name(args.extid)
    elif args.ext_id_list:
        for ext_id in args.ext_id_list:
            parse_extension_name(ext_id)

if __name__ == "__main__":
    main()
