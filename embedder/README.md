# TextTote Embedder

Converts web pages or text into vectors for use in vector similarity search.
Used by TextTote Server as a service.
Can also be used as a standalone CLI application powered by `typer` and `sqlite-vss`.

## Usage


## Development

```sh
# Local development
python -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt

# Test with diff reporter being IntelliJ
# See https://github.com/approvals/ApprovalTests.Python.PytestPlugin
python -m pytest --approvaltests-add-reporter="idea" --approvaltests-add-reporter-args="diff";

# Build standalone CLI
pip install build
python -m build

# TODO build service
```

## Configuration

```ini
# Keys are shown in the format
# KEY=default-value
# To override configurations create a settings.ini in the ~/texttote directory
[settings]
DB_PATH=~/texttote/texttote.db
```