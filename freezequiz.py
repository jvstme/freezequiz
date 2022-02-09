import shutil
from dataclasses import dataclass
from math import log10
from pathlib import Path
from typing import List

import hjson
from jinja2 import Template

FRONT_PATH = Path(__file__).parent / "front"
TEMPLATE_PATH = FRONT_PATH / "template.html"
STATIC_FILES = ["script.js", "style.css"]


class IdFormatter:
    def __init__(self, items_count):
        self._items_count = items_count
        self._id_len = int(log10(items_count)) + 1

    def format(self, num):
        return str(num % self._items_count).zfill(self._id_len)


@dataclass
class Slide:
    id: str
    prev_id: str
    next_id: str

    question: str
    video: str
    timecode: float
    check_button: str
    answer_keys: List[str]
    answer_values: List[str]

    @property
    def answer_items(self):
        return zip(self.answer_keys, self.answer_values)

    @classmethod
    def from_config(cls, slide_config, default_config, id_formatter, num_id):
        params = default_config.copy()
        params.update(slide_config)
        params["id"] = id_formatter.format(num_id)
        params["prev_id"] = id_formatter.format(num_id - 1)
        params["next_id"] = id_formatter.format(num_id + 1)

        return cls(**params)


@dataclass
class Config:
    defaults: dict
    slides: dict

    def flat_slides(self):
        id_formatter = IdFormatter(len(self.slides))
        flat = [
            Slide.from_config(self.slides[i], self.defaults, id_formatter, i)
            for i in range(len(self.slides))
        ]
        return flat

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            data = hjson.load(f)
            return cls(**data)


def gen_quiz(slides, out_dir_path):
    with open(TEMPLATE_PATH) as f:
        template = Template(f.read(), autoescape=True)

    for slide in slides:
        rendered_html = template.render(slide=slide)
        page_path = out_dir_path / f"{slide.id}.html"

        with open(page_path, "w") as out_f:
            out_f.write(rendered_html)

    for file_path in STATIC_FILES:
        source = FRONT_PATH / file_path
        destination = out_dir_path / file_path
        shutil.copy(source, destination)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Generate a FreezeQuiz from config.")
    parser.add_argument(
        "-c", dest="config", help="path to HJSON config file", required=True
    )
    parser.add_argument(
        "-o", dest="out_dir", help="directory for generated files", required=True
    )

    args = parser.parse_args()

    out_dir_path = Path(args.out_dir)
    slides = Config.from_file(args.config).flat_slides()

    gen_quiz(slides, out_dir_path)
