.PHONY: graphs book

graphs:
	dot -Gdpi=200 -Tpng graphs/xncs_action_network.gv -o book/_static/graphs/xncs_action_network.png
	dot -Gdpi=200 -Tpng graphs/xncs_anticipation_network.gv -o book/_static/graphs/xncs_anticipation_network.png

book: graphs
	jupyter-book build -W -n --keep-going --all book/

publish: book
	(cd book && ghp-import -n -p -f _build/html)

notebook:
	jupyter notebook book/