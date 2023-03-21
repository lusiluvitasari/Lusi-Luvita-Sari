from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Nama : Lusi Luvita Sari</p><p> Tempat,Tanggal Lahir : Malang, 11 Juli 2003</p><p> Alamat : Dusun.Purwoasri, Singosari, Malang</p><p> Jenis Kelamin : Perempuan</p><p> Kewarganegaraan : Indonesia</p><p> Agama : Islam</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
