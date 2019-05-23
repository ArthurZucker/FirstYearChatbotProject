all: run

run:
	@(python3 source/chatbot.py)

install: .depends
	@(pip3 install -r requirement.txt --user)

uninstall: .depends
	@(sudo pip3 uninstall -r requirement.txt --user)

.PHONY: install uninstall run
