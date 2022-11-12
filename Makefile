execute:
ifndef folder
	echo "Target folder not passed. Exiting !!" && exit 1
endif
ifndef year
	echo "Target year not passed. Exiting !!" && exit 1
endif

	cd $(year)/$(folder) && go run main.go