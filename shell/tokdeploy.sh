#!/usr/bin/sh

if [ "$PWD" = '/home/heitor/tokpy3' ]; then
    gcloud app deploy --project tokwsv3
elif [ "$PWD" = '/home/heitor/toksite-staging' ]; then
    gcloud app deploy --project toksite-staging
elif [ "$PWD" = '/home/heitor/toksitedjango' ]; then
    cp toksite/debug_setting_false.py toksite/deploy_debug_setting.py
    rm static/CACHE/js/output.*.js
    rm static/CACHE/css/output.*.css
    python manage.py compress --force
    python manage.py collectstatic
    python manage.py migrate --settings=toksite.settingsdbproduction
    gcloud app deploy --project tok-site-django
    cp toksite/debug_setting_true.py toksite/deploy_debug_setting.py
else
    echo "Not in tokpy3, toksite-staging, or toksitedjango top level. Nothing was done."
fi
