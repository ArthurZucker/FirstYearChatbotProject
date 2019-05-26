all: run

run:
	@(python3 source/chatbot.py)

install: requirements.txt
	@(pip3 install -r requirements.txt --user)

uninstall: requirements.txt
	@(sudo pip3 uninstall -r requirements.txt --user)

.PHONY: install uninstall run
