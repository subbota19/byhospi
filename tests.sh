# shellcheck source=/dev/null
env_path="byhospivir/bin/activate"
source "$(pwd -P)/$env_path" && python3 manage.py test tests.test_hospital_models tests.test_client_models tests.test_region_models