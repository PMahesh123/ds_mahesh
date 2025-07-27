# create_zip.py
import os
import zipfile
from pathlib import Path

# Create structure
base_dir = Path('ds_candidate_name')
(base_dir/'csv_files').mkdir(parents=True, exist_ok=True)
(base_dir/'outputs').mkdir(exist_ok=True)

# Create empty files (replace with actual files in real usage)
for f in ['notebook_1.ipynb', 'README.md', 'ds_report.pdf']:
    (base_dir/f).touch()

for img in ['sentiment_trend.png', 'pnl_vs_sentiment.png', 'leverage_distribution.png']:
    (base_dir/'outputs'/img).touch()

# Create zip
with zipfile.ZipFile('ds_candidate_name.zip', 'w') as zipf:
    for file in base_dir.rglob('*'):
        if file.is_file():
            zipf.write(file)

print("Submission package created: ds_candidate_name.zip")