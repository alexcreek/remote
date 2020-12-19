docker build --build-arg COMMIT=$(git rev-parse --short HEAD) -t 192.168.1.10:4000/remote:latest .
docker push 192.168.1.10:4000/remote:latest
