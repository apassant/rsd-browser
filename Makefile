all:
	rm assets/rsd.*
	python src/rsd.py > assets/rsd.json
	coffee -o ./assets ./src