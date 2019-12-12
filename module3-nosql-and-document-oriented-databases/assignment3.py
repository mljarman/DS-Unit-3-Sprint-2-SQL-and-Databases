"""
Working with MongoDB vs PostgreSql:

Perhaps the most obvious difference is that the commands/syntax are
slightly different between the two. SQL in general is more straight forward
and intuitive than MongoDB. I also do like how we could test out queries
in ElephantSQL and DB Browser. This is helpful especially since I'm just
getting startedand not entirely confident with the language. Another major
difference is how they operate and what they're used for. SQL is for relational
databases and MongoDB is used for unstructured databases. Structure
seems better for beginners like me. And, it was mentioned in class that
documents are easily lost with MongoDB compared to SQL's. As with everything
new, however, they both present unqiue challenges when learning.
"""
# Recreation of lecture:
import pymongo

# Connect to MongoDB:
client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-eb7sm.mongodb.net:27017,cluster0-shard-00-01-eb7sm.mongodb.net:27017,cluster0-shard-00-02-eb7sm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# First I'm going to delete all the existing documents from class:
db.test.drop()

# Insert data 1 at a time option 1(must cast as dictionary before inserting):
character1 = (2, "Optio dolorem ex a", 0, 0, 10, 1, 1, 1, 1)
db.test.insert_one({'rpg_character': character1})

# Insert RPG data 1 at a time option 2(seems better since get column names):
db.test.insert_one({
'character_id': 3,
'name': 'Minus c',
'level': 0,
'exp': 0,
'hp': 10,
'strength': 1,
'intelligence': 1,
'dexterity': 1,
'wisdom':1
})

"""
Too add multiple characters at once. Tried to define a function to only change
the name at the character ID but couldn't get it to work. Maybe we can go over.
Tried something similar to last sprint challenge.
"""

characters = [
{
'character_id': 4,
'name': 'Sit ut repr',
'level': 0,
'exp': 0,
'hp': 10,
'strength': 1,
'intelligence': 1,
'dexterity': 1,
'wisdom':1
},
{
'character_id': 3,
'name': 'Minus c',
'level': 0,
'exp': 0,
'hp': 10,
'strength': 1,
'intelligence': 1,
'dexterity': 1,
'wisdom':1
},
{
'character_id': 4,
'name': 'Sit ut repr',
'level': 0,
'exp': 0,
'hp': 10,
'strength': 1,
'intelligence': 1,
'dexterity': 1,
'wisdom':1
}
]

# Insert multiple documents at once:
db.test.insert_many(characters)

# Can find a specific document, like where character_id is 3:
print(list(db.test.find({'character_id': 3})))

# Can update a document. Will change hp to 20 on character_id 4:
db.test.update_one({'character_id': 4}, {'$set': {'hp':20}})

# Can update many documents. Will change all the levels to increase by 2:
db.test.update_many({'level':0}, {'$inc': {'level': 2}})

# Lets look at all the documents in the db:
print(list(db.test.find()))
