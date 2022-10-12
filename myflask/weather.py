import urllib.request
import json
import datetime
import requests
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def weather():
    if request.method == 'POST':
        city=request.form["city"]
    # else:
    #     city='hyderabad'
        print(city)
        #api='997ea79e1c9575bd4f087cf90e68205d'
        api='c8d3cc0516e6dc92763c91ec42508c39'
        #url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api+"&units=metric"
        print(url)
                        #1
        # source = urllib.request.urlopen(url).read()
        # print(source)

        # lstdata=json.loads(source)
        # temparature={'temp':lstdata['main']['temp']}

        #cel=273
        #realtemp=round(temparature['temp'] - cel,2)
        #print(realtemp)



        #return render_template('weatherinfo.html',data=realtemp)
        #return render_template('weatherinfo.html',data=temparature)

                    #2 using requests module

        resp=requests.get(url).json()
        print(resp)
        # picdata='http://openweathermap.org/img/w/50d.png'
        if resp['cod']==200:
        #dicdata={"temp": resp.get("main")['temp']}
            # dicdata = {"temp": resp["main"]['temp'],"lon": resp["coord"]['lon'],"lat":resp["coord"]['lat'],'city':resp['name'],
            #        'sunrise':datetime.datetime.fromtimestamp(resp.get('sys')['sunrise']),
            #            'status':200}

            dataicon=resp["weather"]
            for icondata in dataicon:
                value=icondata['icon']
                break
            urlvalue="http://openweathermap.org/img/w/"+value+".png"
            print(urlvalue)

            dicdata = {"temp": resp["main"]['temp'], "lon": resp["coord"]['lon'], "lat": resp["coord"]['lat'],
                   'city': resp['name'],
                   'sunrise': datetime.datetime.fromtimestamp(resp.get('sys')['sunrise']),
                   'icon':urlvalue,
                   'status': 200}

        # lon = {"temp": resp["coord"]['lon']}
        # lat = {"temp": resp["coord"]['lat']}
        # city={"temp":resp['name']}
        #
        # print(lon)
        # print(lat)
        # print(city)
            return render_template('weatherinfo.html', weathinfo=dicdata)
        elif resp['cod']=='404':
            dicdata={'message':resp['message'],'status':404}
            return render_template('weatherinfo.html', weathinfo=dicdata)


    else:
        dicdata =None
        return render_template('weatherinfo.html',weathinfo=dicdata)

app.run()

#"http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid"=997ea79e1c9575bd4f087cf90e68205d
#http://api.openweathermap.org/data/2.5/weather?q=delhi&appid=997ea79e1c9575bd4f087cf90e68205d