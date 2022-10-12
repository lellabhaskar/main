import json
import datetime
import requests
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def covid():
    if request.method == 'POST':
        country=request.form["country"]

        print(country)
        url = "https://api.covid19api.com/summary"
        print(url)

                    #1 using requests module

        resp=requests.get(url).json()
        print(resp)

        dictdata={}
        #rescountrydata = {'covid':resp["Countries"]}
        rescountrydata = resp["Countries"]
        for countrydata in rescountrydata:
            if countrydata['Country']==country:
               dictdata={'covid':countrydata['Country'],'TotalCases':countrydata['TotalConfirmed'],
                         'TotalDeaths':countrydata['TotalDeaths']}
               break

        return render_template('covidinfo.html', covidinfo=dictdata)
    else:
        dictdata =None
        return render_template('covidinfo.html',covidinfo=dictdata)

app.run()


# create app in heroku ----
            #app-name: bhaskarcovid-app

# heroku git:remote -a bhaskarcovid-app
#heroku login
#git init
# git statusgit commit -am "make it better"
#git add .
#git commit -am "make it better"
