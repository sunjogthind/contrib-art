import os
import subprocess
import random
from datetime import datetime, timedelta

# Art contribution period
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 3, 31)

# How often to commit (roughly 3-5 days per week)
commit_probability = 0.4

def make_commit(date, num_commits):
    for _ in range(num_commits):
        date_str = date.strftime('%Y-%m-%dT12:00:00')
        env = {
            'GIT_AUTHOR_DATE': date_str,
            'GIT_COMMITTER_DATE': date_str
        }
        subprocess.run([
            'git', 'commit', '--allow-empty', '-m', f'Backdated commit on {date_str}'
        ], env={**os.environ, **env})

current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 6 and random.random() < commit_probability:
        commits_today = random.randint(1, 10)  # Vary intensity for shade
        make_commit(current_date, commits_today)
    current_date += timedelta(days=1)

# Push the changes
subprocess.run(['git', 'push', 'origin', 'main'])
