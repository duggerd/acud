import dropbox

def sync_account(token, dropbox_path, local_path):
    with dropbox.Dropbox(oauth2_access_token=token) as dbx:
        response = dbx.files_list_folder(path=dropbox_path)
        for file in response.entries:
            dbx.files_download_to_file(download_path=local_path + file.name, path=file.path_lower)
            dbx.files_delete_v2(file.path_lower)
