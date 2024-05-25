#!/usr/bin/env python
import os
import sys
import multiprocessing
import zoneresolver
from pathlib import Path


if __name__ == '__main__':
    

    db_file = Path("db.sqlite3")
    if not db_file.is_file():
        os.system("cp db.init.sqlite3 db.sqlite3")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dnslog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) >= 2 and sys.argv[1] == 'runserver':
        p = multiprocessing.Process(target=zoneresolver.main)
        p.daemon = False
        p.start()
    execute_from_command_line(sys.argv)
