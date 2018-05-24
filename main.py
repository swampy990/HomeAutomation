from app import app
from config import config

if __name__ == "__main__":
    app.debug=False
    app.run(host='0.0.0.0', port=5000)
