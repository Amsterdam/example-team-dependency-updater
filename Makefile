init:
	git clone git@github.com:Amsterdam/dependency_updater.git
	gh auth login
	glab auth login

run:
	python main.py
