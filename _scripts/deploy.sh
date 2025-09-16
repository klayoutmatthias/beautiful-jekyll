#!/bin/bash -e

self=$(dirname $(which $0))

bundle exec jekyll build --config _config.yml,_build_config.yml -d _site_build

echo "Deploying to www.klayout.org/klayout-pypi now .."
rsync -ah --delete _site_build/ webadm@www.klayout.org:/var/www/vhosts/klayout.org/httpdocs/klayout-pypi

