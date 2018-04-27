import bottle
import pymongo

import helper


#This is the default route, our index page.  Here we need to read the documents from MongoDB.
@bottle.route('/')
def return_api_results():
    names = helper_fn.fetch_results()
    return bottle.template('test1', dict (mynames1=names ))



#We will post new entries to this route so we can insert them into MongoDB
@bottle.route('/search1api', method = 'POST')
def api_queryparams():
    params = {}
    year = bottle.request.forms.get("year")
    year_opt = bottle.request.forms.get("year_opt")
    if year != '':
        if year_opt == '1':
            params['year']=int(year)
        elif year_opt == '2':
            params['year'] = {"$gt":int(year)}
        else:
            params['year'] = {"$lt": int(year)}

    protocols = bottle.request.forms.get("protocols")
    if protocols != '':
        params['protocols'] = protocols

    category = bottle.request.forms.get("category")
    if category != '':
        params['category'] = category
    rating = bottle.request.forms.get("rating")
    rating_opt = bottle.request.forms.get("rating_opt")
    if rating != '':
        if rating_opt == '1':
            params['rating']=float(rating)
        elif rating_opt == '2':
            params['rating'] = {"$gt":float(rating)}
        else:
            params['rating'] = {"$lt": float(rating)}
    tags = bottle.request.forms.get("tags")
    if tags != '':
        temp = tags.strip().split(',')
        params['tag'] = {'$all': temp}
    keywords = bottle.request.forms.get("keywords")
    if keywords != '':
        temp = keywords.strip().split(',')
        params['$or'] = []
        for i in temp:
            reg = '(?=^.*' + i + '.*$)'
            params['$or'].append({'$and': [{'title': {'$regex': reg},
                                            'summary': {'$regex': reg},
                                            'description': {'$regex': reg}}]})
    helper_fn.get_param_api(params, 'api')
    bottle.redirect('/')




#We will post new entries to this route so we can insert them into MongoDB
@bottle.route('/search1mash', method = 'POST')
def mash_queryparams():
    params = {}
    year = bottle.request.forms.get("year")
    year_opt = bottle.request.forms.get("year_opt")
    if year != '':
        if year_opt == '1':
            params['year']=int(year)
        elif year_opt == '2':
            params['year'] = {"$gt":int(year)}
        else:
            params['year'] = {"$lt": int(year)}

    APIs = bottle.request.forms.get("APIs")
    if APIs != '':
        temp = APIs.strip().split(',')
        for api in temp:
            params['APIs.'+api] = {'$exists':'true'}
    tags = bottle.request.forms.get("tags")
    if tags != '':
        temp = tags.strip().split(',')
        params['tag'] = {'$all': temp}
    #{$or:[{$and:[{title: {$regex: '(?=^.*api.*$)' } ,
    # summary:{$regex: '(?=^.*api.*$)' }}]},
    # {$and:[{title: {$regex: '(?=^.*api.*$)' } ,
    # summary:{$regex: '(?=^.*api.*$)' }}]}]}
    keywords = bottle.request.forms.get("keywords")
    if keywords != '':
        temp = keywords.strip().split(',')
        params['$or'] = []
        for i in temp:
            reg = '(?=^.*'+i+'.*$)'
            params['$or'].append({'$and':[{'title': {'$regex': reg} ,
            'summary':{'$regex': reg},'description':{'$regex': reg}}]})

    helper_fn.get_param_mash(params, 'mashup')
    bottle.redirect('/')



#setup the connection
connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.webservice

#guestbook = guestbookDAO.GuestbookDAO(database)
helper_fn = helper.helper(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082)