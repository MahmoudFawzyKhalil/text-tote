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
pip install -r requirements.txt

# Test
python -m pytest

# Build standalone CLI
pip install build
python -m build

# TODO build service
```