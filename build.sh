#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
python -m pip install --upgrade pip
pip install -r req.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate 