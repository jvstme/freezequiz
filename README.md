# FreezeQuiz

Create quizzes where each question is a freeze-frame from a video. FreezeQuiz
was originally intended to be used by a presenter at public events, hence its
minimalistic design.

## Example slide

![Example slide animation](example.gif)

## Installation and usage

Clone and cd into the repository.

```bash
git clone https://github.com/ilunev/freezequiz.git
cd freezequiz
```

Create a virtual environment and install the dependencies. You should have
Python installed.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Edit quiz configuration. See instructions in the example config file.

```bash
$EDITOR config.hjson
```

Run FreezeQuiz passing the configuration and a directory for generated files.

```bash
python freezequiz.py -c config.hjson -o /output/dir
```

Open one of the generated HTML pages in your browser.

```bash
xdg-open /output/dir/0.html
```