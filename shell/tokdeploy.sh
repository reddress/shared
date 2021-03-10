#!/usr/bin/sh

# Deploys tokpy3 to project 'tokwsv3' if run from the tokpy3 directory
# If called from the 'toksitedjango' directory, deploys to:
#   project 'tok-site-django' if no arguments are given
#   project 'tokws-dev' if 'dev' is given as an argument (staging.tempook.com)
#
# Ensure the appropriate database proxy is being run prior to running this script:
#   proxydj.sh for tok-site-django
#   proxydev.sh for tokws-dev

if [ "$PWD" = '/home/heitor/tokpy3' ]; then
    gcloud app deploy --project tokwsv3
elif [ "$PWD" = '/home/heitor/toksitedjango' ]; then
    echo Check that the right DB proxy is running and press Enter.
    read checkproxy
    
    cp toksite/debug_setting_false.py toksite/deploy_debug_setting.py
    cp toksite/dbsettingsproxy.py toksite/dbsettings.py

    rm static/CACHE/js/output.*.js
    rm static/CACHE/css/output.*.css
    python manage.py compress
    python manage.py collectstatic
    python manage.py migrate

    # restore the deployment db settings
    cp toksite/dbsettingsdeploy.py toksite/dbsettings.py

    if [ "$1" = 'dev' ]; then
        echo "\nDEPLOYING TO tokws-dev.\n"
        cp app-tokws-dev.yaml app.yaml
        gcloud app deploy --project tokws-dev
    else
        echo "\nDEPLOYING TO tok-site-django.\n"
        cp app-tok-site-django.yaml app.yaml
        gcloud app deploy --project tok-site-django
    fi

    # restore default settings
    cp toksite/debug_setting_true.py toksite/deploy_debug_setting.py
    cp app-tok-site-django.yaml app.yaml
else
    echo "Not in tokpy3, toksite-staging, or toksitedjango top level. Nothing was done."
fi
