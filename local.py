from app import app
# from waitress import serve


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    # serve(app, host='0.0.0.0', port=8000)


# this one worked, python -m flask run


