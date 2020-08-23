import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

app_key = input("enter app key: ").strip()
app_secret = input("enter app secret: ").strip()

auth_flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = auth_flow.start()

print('copy authorization code from: ' + authorize_url)

auth_code = input("enter authorization code: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
except Exception as e:
    print('error: ' + str(e))
    exit(1)

with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
    dbx.users_get_current_account()
    print('connection successful')
    print('token: ' + oauth_result.access_token)
