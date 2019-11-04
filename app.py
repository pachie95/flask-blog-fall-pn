from codingtempleblog import app
from codingtempleblog.routes import * # * means import everything

if __name__ == "__main__": 
    app.run(debug = True)