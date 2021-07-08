from pathlib import Path

import click


@click.command()
@click.argument("slug")
def cli(slug: str) -> None:
    create_templates(slug)


def exists(path: Path) -> None:
    if path.exists():
        print(f"{path} already exists")
        exit(1)


def create_templates(name: str) -> None:
    filename = name.replace("-", "_")

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
