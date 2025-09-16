#!/bin/bash -e

self=$(dirname $(which $0))

bundle exec jekyll build --config _config.yml,_build_config_staging.yml -d _site_build_staging

echo "Deploying to www.klayout.org/staging/klayout-pypi now .."
rsync -ah --delete _site_build_staging/ webadm@www.klayout.org:/var/www/vhosts/klayout.org/httpdocs/staging/klayout-pypi

