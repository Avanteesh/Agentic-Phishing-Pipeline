## Project Structure

```text
phishing-agent-pipeline/
├── data/
│   └── phishtank/
├── notebooks/
├── src/
│   ├── agents/
│   ├── graph/
│   └── tools/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or later
- Git
- A Groq API key if using Groq-powered agents
- Access to the PhishTank dataset

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd phishing-agent-pipeline
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

**Linux / macOS (Bash):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file.

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**Linux / macOS (Bash):**

```bash
cp .env.example .env
```

Add your API key and any required configuration to `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit `.env` or expose API keys publicly.

### 5. Prepare the PhishTank dataset

Download the PhishTank dataset and place the CSV file at:

```text
data/phishtank/online-valid.csv
```

Make sure the dataset is available before running tests or components that perform local PhishTank lookups.

## Running the Project

Activate the virtual environment, then run the project entry point once configured.

For example, if using a Python module entry point:

```bash
python -m src.main
```

The exact entry point may change as the pipeline is developed.

## Running Tests

Run the test suite from the project root:

```bash
pytest
```

To see more detailed output:

```bash
pytest -v
```

To run a specific test:

```bash
pytest tests/test_url_agent.py -v
```

## Development

Before committing changes, check the test suite:

```bash
pytest
```

Keep API keys, virtual environments, caches, and large dataset files out of version control.

## License

Add the project's chosen license here.oject Structure

```text
phishing-agent-pipeline/
├── data/
│   └── phishtank/
├── notebooks/
├── src/
│   ├── agents/
│   ├── graph/
│   └── tools/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or later
- Git
- A Groq API key if using Groq-powered agents
- Access to the PhishTank dataset

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd phishing-agent-pipeline
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

**Linux / macOS (Bash):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file.

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**Linux / macOS (Bash):**

```bash
cp .env.example .env
```

Add your API key and any required configuration to `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit `.env` or expose API keys publicly.

### 5. Prepare the PhishTank dataset

Download the PhishTank dataset and place the CSV file at:

```text
data/phishtank/online-valid.csv
```

Make sure the dataset is available before running tests or components that perform local PhishTank lookups.

## Running the Project

Activate the virtual environment, then run the project entry point once configured.

For example, if using a Python module entry point:

```bash
python -m src.main
```

The exact entry point may change as the pipeline is developed.

## Running Tests

Run the test suite from the project root:

```bash
pytest
```

To see more detailed output:

```bash
pytest -v
```

To run a specific test:

```bash
pytest tests/test_url_agent.py -v
```

## Development

Before committing changes, check the test suite:

```bash
pytest
```

Keep API keys, virtual environments, caches, and large dataset files out of version control.
