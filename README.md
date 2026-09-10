# patchpay-demo

A throwaway sandbox repo used to demo **PatchPay** — community-funded Lightning
bounties on open-source GitHub issues.

The code here is deliberately tiny and slightly broken so that a contributor can
claim an issue, open a real pull request, and get it merged during the demo.

## Contents

| File | What it is |
|------|------------|
| `slugify.py` | A minimal slug helper with a couple of known bugs (see Issues) |
| `fizzbuzz.py` | Classic FizzBuzz with an off-by-one (see Issues) |
| `tests/test_slugify.py` | A few unit tests, some currently failing |

## Run the tests

```bash
python -m pytest
```
 ## Usage

  ```python
  >>> from slugify import slugify
  >>> slugify("Hello, World!")
  'hello-world'
