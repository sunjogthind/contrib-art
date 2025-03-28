import os
import subprocess
import random
from datetime import datetime, timedelta


start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 9, 1)

commit_probability = 0.3

def make_commit(date, num_commits):
    for _ in range(num_commits):
        time = random.randint(9, 17)  # daytime hours
        date_str = date.replace(hour=time).strftime('%Y-%m-%dT%H:00:00')
        env = {
            'GIT_AUTHOR_DATE': date_str,
            'GIT_COMMITTER_DATE': date_str
        }
        subprocess.run(['git', 'commit', '--allow-empty', '-m', f'Backdated commit on {date_str}'], env={**os.environ, **env})

# Loop through date range
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 6 and random.random() < commit_probability:
        commits_today = random.randint(1, 5)
        make_commit(current_date, commits_today)
    current_date += timedelta(days=1)

subprocess.run(['git', 'push', 'origin', 'main'])
