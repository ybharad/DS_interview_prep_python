print('hello world')

sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

emp = ['kelly','emma','john']

# remove keys from a dict
sdict = {
   "name": "Kelly",
   "age": 25,
   "salary": 8000,
   "city": "New york"

}
keysToRemove = ["name", "salary"]

# check if a value 200 exists in a dict
sdict = {'a': 100, 'b': 200, 'c': 300}

200 in sdict.values()

# rename key city to location
sdict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sdict['location'] = sdict.pop('city')