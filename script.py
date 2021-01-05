#!/usr/bin/python
"""Uploads an apk to the alpha track."""
import os
from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials

TRACK = 'internal'

PACKAGE_NAME = os.environ['_PACKAGE_NAME']
SERVICE_ACCOUNT_EMAIL = os.environ['_SERVICE_ACCOUNT_EMAIL']


def main():
    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with the Credentials. Note that the first parameter, service_account_name,
    # is the Email address created for the Service account. It must be the email
    # address associated with the key that was created.
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        SERVICE_ACCOUNT_EMAIL,
        'key.p12',
        scopes=['https://www.googleapis.com/auth/androidpublisher'])
    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build('androidpublisher', 'v3', http=http)

    # Process flags and read their values.
    package_name = PACKAGE_NAME
    bundle_file = '/app-release.apk'

    try:
        edit_request = service.edits().insert(body={}, packageName=package_name)
        result = edit_request.execute()
        edit_id = result['id']

        bundle_response = service.edits().apks().upload(
            editId=edit_id,
            packageName=package_name,
            media_body=bundle_file,
            media_mime_type='application/octet-stream').execute()

        version_code = bundle_response['versionCode']

        print('Version code %d has been uploaded' % version_code)

        track_response = service.edits().tracks().update(
            editId=edit_id,
            track=TRACK,
            packageName=package_name,
            body={'releases': [{
                'versionCodes': [version_code],
                'status': 'completed',
            }]}).execute()

        print('Track %s is set with releases: %s' % (
        track_response['track'], str(track_response['releases'])))

        commit_request = service.edits().commit(editId=edit_id, packageName=package_name).execute()

        print('Edit "%s" has been committed' % (commit_request['id']))

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')


if __name__ == '__main__':
    main()
