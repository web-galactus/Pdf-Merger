from flask import Flask,request,render_template,redirect,send_file

from io import BytesIO
from PyPDF2 import PdfMerger



app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    
   
    
    if request.method == "POST":
            
           pdfs = request.files.getlist("pdfs")
            
           print(len(pdfs))
          
           if not pdfs:
                   return "Please upload at least one PDF.", 400
           merger = PdfMerger()
           for pdf in pdfs:
                  print(pdf.filename)
                  if pdf.filename.lower().endswith(".pdf"):
                     merger.append(pdf)

           output = BytesIO()
           merger.write(output)
           merger.close()
           output.seek(0)
           return send_file(
           output,
           as_attachment=True,
           download_name="merged.pdf",
           mimetype="application/pdf"
           )

     

    return render_template("home.html")

 

if __name__ == "__main__":
    app.run(debug=True)