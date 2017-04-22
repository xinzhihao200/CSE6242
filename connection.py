import sys, os
from recommender import easy_search
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.mysql import MySQL
import ast

reload(sys)
sys.setdefaultencoding('utf-8')
application = Flask(__name__)
application.debug = True

@application.route('/welcome',methods = ['GET','POST'])
def welcome():
    if request.method == "POST":
        r = request.form['search']
        return redirect(url_for('search_result', request=r))
    else:
        return render_template('welcome.htm')


@application.route('/searchresult', methods=['GET','POST'])
def search_result():
    string = request.form['request']
#    string = request.form('search')
    data = easy_search(string)
    temp_show = {'name': 'none', 'city': 'none', 'stars': 0.0, 'address': 'none', 'categories': 'none'}
    show_result = []
    for element in data:
        temp_show['name'] = element['name']
        temp_show['categoires'] = element['categories'][0]
        temp_show['city'] = element['city']
        temp_show['stars'] = element['stars']
        temp_show['address'] = element['address']

        show_result.append(temp_show)

    return render_template('search_result.html', result=show_result)

@application.route('/Restaurantpage', methods=['GET', 'POST'])
def restaurant_page():
    restaurant=request.form['restaurant']
    return render_template('Restaurant_page.html', restaurant=restaurant)



if __name__ == '__main__':
    application.run()