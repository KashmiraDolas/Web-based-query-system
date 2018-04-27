import string
import pymongo

class helper(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
    def __init__(self, database, flag ='api'):
        self.db = database
        self.coll = database.api
        self.aparams = {}
        self.mparams = {}
        self.flag = flag



    def fetch_results(self):
        result = []
        param= self.aparams
        if self.flag == 'api':
            self.coll = self.db.api
            param = self.aparams
            self.aparams = {}
        elif  self.flag == 'mashup':
            self.coll = self.db.mashup
            param = self.mparams
            self.mparams = {}


        for each in self.coll.find(param,{'title':1, '_id':0}):
            if each['title'] !='':
                result.append({'title': each['title']})


        print(result)
        return result


#This function will handle the insertion of names
    def get_param_api(self,params, flag):
        print(params)

        self.aparams = params
        self.flag = flag

        # This function will handle the insertion of names
    def get_param_mash(self, params, flag):

        print(params)
        self.mparams = params
        self.flag = flag

def main():

    # setup the connection
    connection_string = "mongodb://localhost"
    connection = pymongo.MongoClient(connection_string)
    database = connection.webservice
    h = helper(database)
    h.get_api_name({})
    h.fetch_api_results()

if __name__== "__main__":
    main()