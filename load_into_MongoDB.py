import bottle
import pymongo
# pprint library is used to make the output look more pretty
from pprint import pprint
from collections import OrderedDict
#import helper

#setup a connection string. My sever is running on this computer so localhost
# is on
connection_string = "mongodb://127.0.0.1:27017"
#let PyMongo know about the MongoDB connection we want to use. PyMongo will
# mange the connection
connection = pymongo.MongoClient(connection_string)
database=connection.webservice
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
api_collection = database.api
mashup_collection = database.mashup


#tag at 17 has to be a list,
header_api = "id$#$title$#$summary$#$rating$#$name$#$label$#$author$" \
             "#$description$#$type$#$downloads$#$useCount$#$sampleUrl$" \
             "#$downloadUrl$#$dateModified$#$remoteFeed$#$numComments$" \
             "#$commentsUrl$#$tag$#$category$#$protocols$#$serviceEndpoint$#$" \
             "version$#$wsdl$#$dataFormats$#$apigroups$#$example$#$clientInstall" \
             "$#$authentication$#$ssl$#$readonly$#$VendorApiKits$#$" \
             "CommunityApiKits$#$blog$#$forum$#$support$#$accountReq$#$" \
             "commercial$#$provider$#$managedBy$#$nonCommercial$#$dataLicensing" \
             "$#$fees$#$limits$#$terms$#$company$#$updated"
label_api = header_api.strip().split("$#$")

#tag at 15 has to be a list, api1$$$url1###  at 16 has to be set of objects
header_mashup = "id$#$title$#$summary$#$rating$#$name$#$label$#$author$#$" \
                "description$#$type$#$downloads$#$useCount$#$sampleUrl$#$" \
                "dateModified$#$numComments$#$commentsUrl$#$tag$#$APIs$" \
                "#$updated"
label_mashup = header_mashup.strip().split("$#$")


def readAndProcess(file, collection, flag):
    count = 0
    with open(file, encoding='ISO-8859-1') as f:
        for line in f:
            count += 1
            temp_dict = OrderedDict()
            temp_list=line.strip().split("$#$")

            for i in range (len(temp_list)):
                if flag == "api":
                    if i == 17:
                        if  temp_list[i]!= "":
                            temp_dict[label_api[i]]= temp_list[i].strip().split("###")
                        else:
                            temp_dict[label_api[i]] = ""
                    elif i == 3 and temp_list[i] != "":
                        temp_dict[label_api[i]] = float(temp_list[i].strip())
                    else:
                        temp_dict[label_api[i]] = temp_list[i].strip()

                elif flag == "mashup":
                    if temp_list[i] != "":
                        if i == 15:
                            temp_dict[label_mashup[i]]= temp_list[i].strip().split(
                                "###")
                        elif i == 16 and  temp_list[i]!= "":
                            dict = {}
                            pairs = temp_list[i].strip().split("###")

                            for pair in pairs:
                                dict[pair.strip().split("$$$")[0]] = pair.strip().split("$$$")[1]
                            temp_dict[label_mashup[i]] = dict

                        elif i == 3 and temp_list[i] != "":
                            temp_dict[label_mashup[i]] = float(temp_list[i].strip())
                        else:
                            temp_dict[label_mashup[i]] = temp_list[
                                i].strip()
                    else:
                       temp_dict[label_mashup[i]] = ""



            temp_dict['year'] = int(temp_list[-1][:4])
            if flag == "api":
                api_collection.insert(temp_dict, check_keys=False)
            elif flag == "mashup":
                mashup_collection.insert(temp_dict, check_keys=False)


    print(flag + " Done!")



def main():
    #serverStatusResult = database.command("serverStatus")
    #pprint(serverStatusResult)

    '''

    Uncomment the readAndProcess lines to load data into MongoDB
    '''
    readAndProcess("api.txt", api_collection, "api")
    readAndProcess("mashup.txt", mashup_collection, "mashup")
    print("Done!")

if __name__=="__main__":
    main()