# Google Play Publisher

An image to upload an Android App Bundle (`.apk`) to Google play.

## How-to

```sh
docker run --rm \
	-v "$(pwd)/app-release.apk:/app-release.apk" \
	-v "$(pwd)/key.p12:/key.p12" \
	-e "_PACKAGE_NAME=package.name.app" \
	-e "_SERVICE_ACCOUNT_EMAIL=name@email.com" \
	javagrinko/google-play-publisher
```
