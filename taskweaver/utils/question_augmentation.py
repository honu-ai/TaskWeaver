import yaml
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

with open(ROOT_DIR / 'project/questions.yaml', 'r') as file:
    question_map = yaml.safe_load(file)

