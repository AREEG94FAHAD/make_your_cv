from flask import Flask, request, abort, jsonify, json, send_file, session, after_this_request,send_from_directory
from flask_cors import CORS
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
from flask_session import Session
from flask_mail import *
import os
from threading import Thread
import json
from reportlab.lib.colors import HexColor, white, Color, black
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.frames import ShowBoundaryValue
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import datetime
import random
import string
# from datetime import datetime, time
import traceback
from werkzeug.wsgi import ClosingIterator

class AfterResponse:
    def __init__(self, app=None):
        self.callbacks = []
        if app:
            self.init_app(app)

    def __call__(self, callback):
        self.callbacks.append(callback)
        return callback

    def init_app(self, app):
        # install extension
        app.after_response = self

        # install middleware
        app.wsgi_app = AfterResponseMiddleware(app.wsgi_app, self)

    def flush(self):
        for fn in self.callbacks:
            try:
                fn()
            except Exception:
                traceback.print_exc()

class AfterResponseMiddleware:
    def __init__(self, application, after_response_ext):
        self.application = application
        self.after_response_ext = after_response_ext

    def __call__(self, environ, after_response):
        iterator = self.application(environ, after_response)
        try:
            return ClosingIterator(iterator, [self.after_response_ext.flush])
        except Exception:
            traceback.print_exc()
            return iterator

def get_random_string(length):
    # print(type())
    letters = string.ascii_lowercase
    # removeSpace = str(datetime.datetime.now()).replace(" ","")
    # removecolon = removeSpace.replace(":","")
    # last = removecolon.split(".")[0]
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str



app = Flask(__name__)
AfterResponse(app)
cors = CORS(app, resources={"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# app.config["MAIL_SERVER"] = 'smtp.gmail.com'
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USERNAME"] = 'fahedareeg@gmail.com'
# app.config['MAIL_PASSWORD'] = '-'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

app.secret_key = 'any random string'

@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization,true')
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET,PATCH,POST,DELETE,OPTIONS')
    return response

@app.route('/', methods=['get'])
def hi():
    return 'Hi'


@app.route('/', methods=['post'])
def hello_world():

    
    # if(str(datetime.datetime.now().hour) == '23'):

    #     for f in os.listdir(os.getcwd()):
    #         print(f)
    #         if not f.endswith(".pdf"):
    #             continue
    #         os.remove(f)
    #         print("File Removed!")

    # timeToDelete = datetime.datetime.today()

    # pdf generate

    Current_Date = datetime.datetime.today().strftime('%d-%b-%Y')
    filename = r'Areeg' + str(Current_Date) + \
        str(get_random_string(10)) + '.pdf'
    pdf = canvas.Canvas(filename)

    # get data fom api

    if json.loads(request.form['checkImage']):
        uploaded_file = request.files['image']
        uploaded_file.save((uploaded_file.filename))
        image = Image.open((uploaded_file.filename)).resize((110, 90))
        os.remove(uploaded_file.filename)
        pdf.drawInlineImage(image, 440, 680)
        pdf.setStrokeColor(white)
        pdf.setLineWidth(30)
        pdf.circle(495, 725, 60, stroke=1, fill=0)

    name = json.loads(request.form['name'])
    abouteme = json.loads(request.form['abouteme'])
    acadmicBackground = json.loads(request.form['acadmicBackground'])
    experience = json.loads(request.form['experience'])
    skills = json.loads(request.form['skills'])
    certifcates = json.loads(request.form['certifcates'])
    accomplishments = json.loads(request.form['accomplishments'])
    contactinfo = json.loads(request.form['contactinfo'])

    # os.rename(r'ss.pdf',r'ss' + str(Current_Date) + '.pdf')
    pdf.setTitle(name)
    pdf.setFillColor(HexColor(0xff8100))
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(200, 725, name)

    # Title Style
    titile = ParagraphStyle('titile')
    titile.firstLineIndent = 0
    titile.textColor = HexColor(0xff8100)
    titile.fontSize = 16

    # text Style
    text = ParagraphStyle('text')
    text.firstLineIndent = 0
    text.textColor = HexColor(0x6f8b80)
    text.fontSize = 12
    text.spaceBefore = 6
    text.justifyBreaks = 1
    text.justifyLastLine = 1
    text.splitLongWords = 1

    # bold
    boldd = ParagraphStyle('boldd')
    boldd.firstLineIndent = 0
    boldd.textColor = HexColor(0x6f8b80)
    boldd.fontSize = 12
    boldd.borderPadding = 1
    boldd.spaceAfter = 12
    boldd.spaceBefore = 4

    # Abouteme
    addAbouteme = []
    addAbouteme.append(Paragraph("ABOUT ME", titile))
    addAbouteme.append(Paragraph(abouteme, text))
    addAboutemeFrame = Frame(27, 600, 300, 100)
    addAboutemeFrame.addFromList(addAbouteme, pdf)

    # Eduction
    addEduction = []
    addEduction.append(Paragraph("ACADEMIC BACKGROUND", titile))
    for i in range(0, len(acadmicBackground)):

        addEduction.append(Paragraph(acadmicBackground[i]['unversity'], text))
        addEduction.append(Paragraph(acadmicBackground[i]['depart'], boldd))

    addEductionFram = Frame(27, 445, 300, 150)
    addEductionFram.addFromList(addEduction, pdf)

    # Experience
    addExperience = []
    addExperience.append(Paragraph("Experience", titile))
    for i in range(len(experience)):
        addExperience.append(Paragraph(experience[i]['experience'], boldd))
    addExperienceFram = Frame(27, 320, 300, 120)
    addExperienceFram.addFromList(addExperience, pdf)

    # Skills
    addSkills = []
    addSkills.append(Paragraph("Skills", titile))
    for i in range(len(skills)):
        addSkills.append(Paragraph(skills[i]['skill'], boldd))
    addSkillsFram = Frame(27, 10, 300, 300)
    addSkillsFram.addFromList(addSkills, pdf)

    # Certifcates
    addCertifcates = []
    addCertifcates.append(Paragraph("Certifcates", titile))
    for i in range(len(certifcates)):
        addCertifcates.append(Paragraph(certifcates[i]['certifcate'], boldd))
    addCertifcatesFram = Frame(340, 395, 300, 200)
    addCertifcatesFram.addFromList(addCertifcates, pdf)

    # Contact Info
    addContactinfo = []
    addContactinfo.append(Paragraph("Contact Info", titile))
    for i in range(0, len(contactinfo)):

        addContactinfo.append(Paragraph(contactinfo[i]['type'], text))
        addContactinfo.append(Paragraph(contactinfo[i]['acount'], boldd))

    addContactinfoFram = Frame(340, 270, 250, 150)
    addContactinfoFram.addFromList(addContactinfo, pdf)

    # accomplishments
    addAccomplishments = []
    addAccomplishments.append(Paragraph("Accomplishments", titile))
    for i in range(len(accomplishments)):
        addAccomplishments.append(
            Paragraph(accomplishments[i]['accomplishment'], boldd))
    addAccomplishmentsFram = Frame(340, 50, 280, 200)
    addAccomplishmentsFram.addFromList(addAccomplishments, pdf)

    pdf.save()
    # msg = Message(subject = "hello", body = "hello", sender = "fahedareeg@gmail.com", recipients = ["fahedareeg@gmail.com"])
    # with app.open_resource(filename) as fp:
    #     msg.attach(filename=filename,disposition="attachment",content_type="application/pdf",data=fp.read())
    #     mail.send(msg)
    # os.remove(filename)



    # r = current_app.response_class(generate(), mimetype='application/pdf')
    # r.headers.set('Content-Disposition', 'attachment', filename="filename")

    # if(str(datetime.datetime.now().hour) == '9'):
    #     for f in os.listdir(os.getcwd()):
    #         print(f)
    #         if not f.endswith(".pdf"):
    #             continue
    #         os.remove(f)
    #         print("File Removed!")

    # def generate():
    #     with open(filename) as f:
    #         yield from f
    #     os.remove(filename)

    response = send_from_directory(directory=os.getcwd(), filename=filename)
    response.headers['my-custom-header'] = 'my-custom-status-0'

    # Thread(target = generate()).start()

    @app.after_response
    def generate():
#         print(filename)
        # with open(filename) as f:
        #     yield from f
        os.remove(filename)
#         print(filename)
    return response
    
    # return str(r)
