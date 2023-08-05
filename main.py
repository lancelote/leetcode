from pathlib import Path
from urllib.parse import urlparse

import click


@click.command()
@click.argument("problem")
def cli(problem: str) -> None:
    slug = parse_slug(problem)
    create_templates(slug)


def exists(path: Path) -> None:
    if path.exists():
        print(f"{path} already exists")
        exit(1)


def parse_slug(problem: str) -> str:
    if problem.startswith("https"):
        url = urlparse(problem)
        path = url.path

        assert not path[0] and path[1] == "problems", f"invalid {url=}"

        return url.path.split("/")[2]
    else:
        return problem


def create_templates(name: str) -> None:
    filename = name.replace("-", "_")
    if filename[0].isnumeric():
        filename = f"_{filename}"

    src_file = Path("src", f"{filename}.py")
    test_file = Path("tests", f"test_{filename}.py")

    exists(src_file)
    exists(test_file)

    src_file.open("w").close()
    test_file.open("w").close()

    print(f"touch {src_file}")
    print(f"touch {test_file}")


if __name__ == "__main__":
    cli()
