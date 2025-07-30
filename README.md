# 🚀 Class 0 – Setup for Success

Welcome! 
This setup guide ensures your development environment is clean, reproducible, and perfectly aligned with the course. 
Following these steps carefully will prevent common issues later on and teach you the professional standard for managing Python projects.

---

### ✅ What You’ll Accomplish

* **Install a specific Python version (3.12.4)** to ensure code compatibility.
* **Create an isolated virtual environment** for this project using `venv`.
* **Install all required course libraries** from a `requirements.txt` file.
* **Verify your complete setup** with a test script.

---

### 1. Install `pyenv` (The Professional Python Version Manager)

We use `pyenv` to manage Python versions. 
This avoids system conflicts and ensures you're using the exact same version as the course.

**On macOS (using Homebrew):**
```bash
brew update
brew install pyenv
```

**On Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev \
xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash
```

Be sure to add the shell config lines shown by the installer and restart your terminal.

**On Windows:** Use [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and follow the Ubuntu instructions above.

---

### 2. Install and Set the Course Python Version
```bash
pyenv install 3.12.4
pyenv global 3.12.4
python --version  # Expect: Python 3.12.4
```

---

### 3. Create and Activate a Virtual Environment
```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
.\venv\Scripts\Activate.ps1
```

---

### 4. Install Project Dependencies

**File: `requirements.txt`**
```
pandas==2.3.1
scikit-learn==1.7.0
numpy==2.3.2
```

Then install:
```bash
pip install -r requirements.txt
```

---

### 5. Verify Your Environment

**File: `hello.py`**
```python
import sys
import pandas as pd
import sklearn
import numpy as np

def main():
    print("✅ Python environment is working!")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"pandas version: {pd.__version__}")
    print(f"scikit-learn version: {sklearn.__version__}")
    print(f"numpy version: {np.__version__}")

if __name__ == "__main__":
    main()
```

Run:
```bash
python hello.py
```

---

### 6. Optional: Configure VSCode

**File: `.vscode/settings.json`**
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    }
}
```

---

### 🔧 Troubleshooting

* `pyenv install` fails: Check [pyenv wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems)
* `command not found: pyenv`: You missed the shell setup step. Rerun the installer.

---

### 🧭 What’s Next?

Your dev environment is ready.
Happy coding! 🚀
