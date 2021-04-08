from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/carousel')
def carousel():
    return f"""
            <link
             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
             rel="stylesheet" 
             integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
             crossorigin="anonymous">
            <title>Пейзажи марса</title>
            <h1><b>Пейзажи марса</h1>
            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                  <img class="d-block w-100" src="/static/img/23133.jpg" alt="Первый слайд">
                </div>
                <div class="carousel-item">
                  <img class="d-block w-100" src="/static/img/133284.jpg" alt="Второй слайд">
                </div>
                <div class="carousel-item">
                  <img class="d-block w-100" src="/static/img/gory-nebo-peyzazh-5478.jpg" alt="Третий слайд">
                </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
            </div>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')