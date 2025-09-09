# Auto-appended __main__ runner for development convenience
from app import app, init_db
import os

if __name__ == '__main__':
    with app.app_context():
        try:
            init_db()
        except Exception as e:
            print('DB init error:', e)
    port = int(os.getenv('PORT', '5010'))
    app.run(host='0.0.0.0', port=port, debug=True)