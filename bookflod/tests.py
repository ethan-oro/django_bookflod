from django.test import TestCase
from django.test import Client
from django.conf import settings

import os

# Create your tests here.

class UnitTests(TestCase):

    def setUp(self) :
        settings.DEBUG = True
        c = Client()

    def test_urls(self):
        c = Client()
        print("running tests...")
        url_source = open('./bookflod/urls.py', 'r')
        lines = url_source.readlines()
        start_index = lines.index("urlpatterns = [\n") + 1
        try :
            end_index = lines.index("] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n")
        except ValueError :
            end_index = len(lines)
        line_iterator = iter(lines[start_index:end_index])

        while True :
            try :
                line = line_iterator.__next__()
                #Checks to see if it is a stand alone url
                if(")," in line[-3:-1]) :
                    line_parts = line.split(",")
                    path = line_parts[0].split("\'")[1]
                    view = line_parts[1]
                    name = line_parts[2].split("\'")[1]


                    response = c.get("/" + path)
                    print (response.client)
                    print ("//")
                    print (response.content)
                    print ("//")
                    print (response.context)
                    # print ("//")
                    # print (response.json())
                    print ("//")
                    print (response.request)
                    print ("//")
                    print (response.templates)
                    print ("//")
                    print (response.resolver_match)
                    print ("//")

                    #Prints out returned query path
                    print ("querying ", response.wsgi_request.get_full_path())

                    #Checks to make sure stats code is 200
                    if (response.status_code == 200) :
                        print ("Succesfully Conected")
                    else :
                        print ("ERROR: Status Code", response.status_code)

                    self.assertEqual(response.resolver_match.url_name, name)

                    #Checks to make sure URL tage name is correct
                    if (response.resolver_match.url_name == name) :
                        print ("Sucessfully tagged correct url resolver name")
                    else :
                        print ("ERROR: Wrong Name - should be " , name , " but is ", response.resolver_match.url_name)


                    #Checks to make sure the correct view is returned
                    if(response.resolver_match.func in view) :
                        print ("Sucessfully loaded the correct view")
                    else :
                        print ("ERROR")



                    print ("Path=", path, " View=", view, " Name=",name)

            except StopIteration :
                print ("Finished Unit Tests")
                break


if __name__ == "__main__":
    read_urls()
