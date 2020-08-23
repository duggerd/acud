import xfer

import json
import time

ACCT_FILE = 'accounts.json'
DELAY_SEC = 5

def main():
    with open(ACCT_FILE, 'r') as f:
        accounts_text = f.read()

    accounts_json = json.loads(accounts_text)

    try:
        print('started')

        while True:
            for account in accounts_json['accounts']:
                token = account['token']
                dropbox_path = account['dropbox_path']
                local_path = account['local_path']

                try:
                    xfer.sync_account(token, dropbox_path, local_path)
                except Exception as e:
                    print('sync account failed: ' + str(e))

            time.sleep(DELAY_SEC)
    except KeyboardInterrupt:
        print('stopping')
        pass

if __name__== '__main__':
    print('starting')
    main()
    print('stopped')
