import sys
from pathlib import Path

# Make the src/ folder importable for the tests
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
