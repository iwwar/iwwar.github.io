import os
from flask import Flask, request, render_template, url_for, redirect;

app= Flask(__name__)

@app.route('/success', methods=['GET', 'POST'])
def success():
  return render_template("/augmentation/app/index.html")  

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    img_path = "static/tmp/target.jpg"
    stl_path = "static/stl/model"
    obj_path = "static/obj/model.obj"
    gltf_path = "static/gltf/model.gltf"
    f = request.files['img']
    f.save(img_path)
    print("Converting to STL")
    cmdstl = "./img2stl/makestl.py {} {}".format(img_path, stl_path)
    cmdobj = "ctmconv ./static/stl/model.stl {}".format(obj_path)
    cmdgltf = "obj2gltf -i {} -o {}".format(obj_path, gltf_path)
    os.system(cmdstl)
    os.system(cmdobj)
    os.system(cmdgltf)
    print("Modeling Done\n");
    return redirect(url_for("success"))
  
  return render_template("upload.html")

  if __name__ == "__main__":
    app.run(debug=false, host="0.0.0.0")
