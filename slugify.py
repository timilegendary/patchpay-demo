"""A tiny slug helper. Intentionally imperfect — see the repo's open issues."""
import re


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # BUG: leaves a trailing "-" when the input ends with punctuation/space.
    return text


if __name__ == "__main__":
    print(slugify("Hello, World!"))
