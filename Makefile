all:
	rm -f assets/rsd.*
	python src/rsd.py > assets/rsd.json
	coffee -o ./assets ./src