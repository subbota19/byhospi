# shellcheck source=/dev/null
env_path="byhospivir/bin/activate"
source "$(pwd -P)/$env_path" && python3 manage.py test