import logging
import sys
from pathlib import Path
from urllib.parse import urlparse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def exists(path: Path) -> None:
    if path.exists():
        logger.error("%s already exists", path)
        sys.exit(1)


def parse_slug(problem: str) -> str:
    if problem.startswith("https"):
        url = urlparse(problem)
        segments = url.path.split("/")

        assert not segments[0] and segments[1] == "problems", f"invalid {url=}"

        return segments[2]
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

    logger.info("touch %s", src_file)
    logger.info("touch %s", test_file)


def main() -> None:
    if len(sys.argv) < 2:
        logger.error("please provide problem URL or slug")
        sys.exit(1)

    slug = parse_slug(sys.argv[1])
    create_templates(slug)


if __name__ == "__main__":
    main()
