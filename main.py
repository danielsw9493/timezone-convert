"""Timezone Convert — Convert a timestamp across time zones and print IANA names you can copy."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='timezone_convert',
        description='Convert a timestamp across time zones and print IANA names you can copy.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Timezone Convert')
    print('IANA timezone conversion without a website.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# revisit later (2026-11-03)
# refactor bit (2026-11-03)
# update note (2026-11-04)
# revisit later (2026-11-05)
# small fix (2026-11-05)
# tune (2026-11-05)
# cleanup (2026-11-06)
# small fix (2026-11-06)
