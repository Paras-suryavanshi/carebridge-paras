#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files (CSS, Images) so they work online
python manage.py collectstatic --no-input

# Update the database structure
python manage.py migrate