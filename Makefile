execute:
ifndef folder
	echo "Target folder not passed. Exiting !!" && exit 1
endif

	cd $(folder) && go run main.go