
cur=`pwd`

export GOPATH=$GOPATH:${cur}

echo $GOPATH

go run main.go
