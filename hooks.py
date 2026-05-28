import subprocess
from pathlib import Path


def on_pre_build(config):
    '''Generate docs/changelog.md from git log before each build.'''
    repo_root = Path(__file__).parent
    result = subprocess.run(
        ['git', 'log', '--pretty=format:%ad|%s', '--date=short'],
        capture_output=True,
        text=True,
        cwd=repo_root
    )

    lines = []
    current_date = None

    for line in result.stdout.strip().split('\n'):
        if '|' not in line:
            continue
        date, message = line.split('|', 1)
        if date != current_date:
            if current_date is not None:
                lines.append('')
            lines.append(f'## {date}')
            current_date = date
        lines.append(f'- {message.strip()}')

    content = '# Changelog\n\n' + '\n'.join(lines) + '\n'
    Path('docs/changelog.md').write_text(content)
