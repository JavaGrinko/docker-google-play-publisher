# Google Play Publisher

An image to upload an Android App Bundle (`.apk`) to Google play.

## How-to

```sh
docker run --rm \
	-e "_APK_FILE_PATH=$(pwd)/app-release.apk" \
	-e "_KEY_FILE_PATH=$(pwd)/key.p12" \
	-e "_PACKAGE_NAME=package.name.app" \
	-e "_SERVICE_ACCOUNT_EMAIL=name@email.com" \
	javagrinko/google-play-publisher
```
