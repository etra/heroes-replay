from pathlib import Path
from homm3.models import Repository, Player
from homm3.generator import Generator
import json

UI_EXPORT_PATH = '_exports'

if __name__ == '__main__':

    repository = Repository.default()
    generator = Generator(repository=repository)

    index = generator.generate_index()
    static = generator.generate_static()

    path = Path(UI_EXPORT_PATH)
    path.mkdir(parents=True, exist_ok=True)

    with open(path / f"index.json", "w") as f:
        json.dump(index, f)
    
    with open(path / f"static.json", "w") as f:
        json.dump(static, f)
    