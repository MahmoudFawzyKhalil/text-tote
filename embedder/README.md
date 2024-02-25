# TextTote Embedder

Converts web pages or text into vectors for use in vector similarity search.
Used by TextTote Server as a service.
Can also be used as a standalone CLI application `texttote`.

## Usage


## Development

```sh
# Local development
python -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt

# Install as editable site-package - https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html
pip install -e .
# Test with  IntelliJ as the diff reporter - https://github.com/approvals/ApprovalTests.Python.PytestPlugin
python -m pytest --approvaltests-add-reporter="idea" --approvaltests-add-reporter-args="diff";

# Build standalone CLI
pip install build
python -m build
```

## Configuration

For deployment as a server: use environment variables

For local dev and tests of CLI app:

```
./settings.ini - local dev
./tests/settings.ini - for tests
```

For installed CLI app:

```ini
# Keys are shown in the format
# KEY=default-value
# To override configurations create a settings.ini in the ~/texttote directory
[settings]
DB_PATH=~/texttote/texttote.db
```