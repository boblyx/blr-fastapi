set -o allexport
source .env.dev
source venv/bin/activate
python api.py
set +o allexport
