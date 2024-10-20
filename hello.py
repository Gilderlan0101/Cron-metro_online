from flask import Flask, render_template
import time


class Incrementador:
    def __init__(self, hora=0, minutos=0, segundos=0 ):
        self.horas = hora
        self.minutos = minutos
        self.segundos = segundos

    def display(self):
        '''função quue exibira o icrementador'''
        relogio = f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'
        print(relogio)
        return  relogio

    def icrementa(self):
        while True:
            time.sleep(1)
            self.segundos += 1

            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
                if self.minutos == 60:
                    self.minutos = 0
                    self.horas =+ 1
            self.display()


app = Flask(__name__)
app.secret_key == '23456trfdfdtr55'

@app.route('/')
def contador_online():

    horas = Incrementador.display

    return render_template('index.html',horas=horas)


if __name__ == '__main__':
    app.run(debug=True)




