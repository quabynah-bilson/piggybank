gen-protos-bank:
	./gen-go-protos.sh

gen-protos-mobile:
	./gen-dart-protos.sh

gen-protos-auth:
	./gen-python-protos.sh

mobile-deps:
	cd mobile && \
	flutter pub add grpc protobuf_google protobuf bloc flutter_bloc injectable get_it auto_route google_fonts lottie && \
	flutter pub add --dev build_runner auto_route_generator injectable_generator && \
	flutter pub upgrade --major-versions

build-savings-docker:
	cd savings-server && \
	docker build -t savings-server .

gen-auth-private-key:
	cd auth-server && \
	mkdir -p certs && \
	openssl genrsa -out certs/private.pem 4096

gen-mobile-avatars:
	cd mobile/assets/img && \
	mkdir -p avatars && cd avatars && \
	dicebear lorelei . --format png --count 10 --width 200 --height 200 --background "#ffffff" --radius 50 --margin 10 --outDir .

format-avatar-names:
	cd mobile/assets/img/avatars && ls -la && \
	for file in *; do mv "$file" "$(echo "$file" | sed 's/-/_/g')"; done

add-googleapis-to-protos:
	cd customer-server/proto && \
	git submodule add https://github.com/googleapis/googleapis && \
	git submodule update --remote