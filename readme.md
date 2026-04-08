# mini-rag

this is a minimal implementation of the rag model for question answering.

## requirements

- python 3.10+
- pip

## installation

### install required packages

```bash
uv pip install -r requirements.txt
```

### create virtual environment

```bash
python -m venv .venv
```

### setup environment variables

```bash
cp .env.example .env
```

### activate virtual environment

```bash
.\.venv\Scripts\activate
```

## run fast api

```bash
uvicorn main:app --reload --host [IP_ADDRESS] --port 5000
```

