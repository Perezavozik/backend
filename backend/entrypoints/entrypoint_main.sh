#!/bin/bash

set -e

cd /app/

./entrypoints/migrations.sh
./entrypoints/createsuperuser.sh


echo "Running server..."
exec "$@"
