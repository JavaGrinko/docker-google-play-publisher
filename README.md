# Google Play Publisher

An image to upload an Android App Bundle (`.apk`) to Google play.

## How-to

```sh
docker run --rm \
	-e "APK_FILE_PATH=$(pwd)/app-release.apk" \
	-e "KEY_FILE_PATH=$(pwd)/key.p12" \
	-e "PACKAGE_NAME=package.name.app" \
	-e "SERVICE_ACCOUNT_EMAIL=name@email.com" \
	javagrinko/google-play-publisher
```
