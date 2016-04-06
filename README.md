IIT Bombay's Blog Aggregator
===

Rawdog's documentation: http://offog.org/code/rawdog/

### Installation

Follow these steps. Here, `<home>` refers to the `iitb-blog-aggregator` directory.

* Make a virtual environment with **Python2** (Learn how to do so [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)).
* Install feedparser

		pip install feedparser

* Got to `<home>/configurations/` and do

		cp config.example config

* In the `config` file, add path to your `iitb-blog-aggregator` directory at two places (replace `<path to github folder>` aptly by <kbd>Ctrl + F</kbd>-ing)
* Go to `<home>/rawdog` and run

		./rawdog

* If it doesn't work, post on the gitter chat.

### Running

If the above works, run the following

	./rawdog -u
	./rawdog -w

Your final generated website will be inside the `<home>/website` folder.
