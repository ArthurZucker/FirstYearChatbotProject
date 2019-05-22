all: run

run:
	@(python3 source/chatbot.py)

install: .depends
	@(pip3 install -q < .depends)

uninstall: .depends
	@(pip3 uninstall -q < .depends)

.PHONY: install uninstall run
