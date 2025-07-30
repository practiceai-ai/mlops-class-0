import sys
import pandas as pd
import sklearn

def main():
    """Prints library versions to verify the environment."""
    print("✅ Python environment is working!")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"pandas version: {pd.__version__}")
    print(f"scikit-learn version: {sklearn.__version__}")

if __name__ == "__main__":
    main()