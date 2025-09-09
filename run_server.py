import app as application
import os

app = application.app
init_db = application.init_db

if __name__ == '__main__':
    with app.app_context():
        try:
            init_db()
        except Exception as e:
            print('DB init error:', e)
    port = int(os.getenv('PORT', '5010'))
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
