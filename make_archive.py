from pathlib import Path
import shutil
root = Path(__file__).resolve().parent
zip_path = root.parent / (root.name + '.zip')
if zip_path.exists():
    zip_path.unlink()
# Create zip archive of the project directory
shutil.make_archive(str(zip_path.with_suffix('')), 'zip', root)
print('created', zip_path)
print('size', zip_path.stat().st_size)
