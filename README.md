# SMTP Template Python

This repository was created to simplify the process of sending automated emails. It provides a pre-configured project with ready-to-use files for sending plain emails, dynamic emails (with data inserted into templates), and non-dynamic emails (using templates without data insertion).
The goal is to allow users to easily integrate this email system into their own projects without needing to build everything from scratch. It offers a practical, fast, and accessible solution for various email-sending scenarios.

---

## Environment Variables

To run this project, you'll need to add the following environment variables to your `.env` file:

* `EMAIL_SERVER`
* `EMAIL_PORT`
* `SEND`
* `PASSWORD`

---

## Running Locally

Clone the project:

```bash
git clone https://github.com/LuisGomes18/SMTP-Template-Email/
```

Enter the project directory:

```bash
cd SMTP-Template-Email
```

### Create and activate a virtual environment

```bash
python3 -m venv .venv
```

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python3 file_name.py
```

> Replace `file_name.py` with the actual name of the Python file that starts the project.
