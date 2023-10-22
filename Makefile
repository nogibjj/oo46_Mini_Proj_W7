install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py assignment_app/*.py

# run:
# 	python main_cli.py show
		
all: install test format refactor
