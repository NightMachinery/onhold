from os import environ
from pathlib import Path
from sys import exit, stderr

from .base import play_after, dumb_pipe, \
  play_file, RC_ENV_VAR

import click


ENV_VAR = 'DING'


def run(file: Path):
  try:
    dumb_pipe()

  finally:
    if file:
      play_file(file)


@click.command(help="Play specified sound after job is complete.")
@click.option('-s', '--sound_path', required=False,
  type=click.Path(exists=True))
def cmd(sound_path):
  path: Optional[Path] = None

  if sound_path:
    path = Path(str(sound_path))

  else:
    if ENV_VAR in environ:
      path = Path(file_loc)

    else:
      stderr.write(f"Please set ${ENV_VAR}.\n")

    run(path)

    if not path:
      exit(RC_ENV_VAR)

if __name__ == "__main__":
  cmd()
