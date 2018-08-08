from madynamodb import createTable, deleteTable, putItem, getItem, queryItem, deleteItem, updateItem, tableExists

# aws dynamodb list-tables --endpoint-url=http://localhost:8000

#createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

# deleteTable("madonnaSongs", "eu-west-2", "http://localhost:8000" )

#deleteTable("madonnaSongs", "eu-west-2", "http://localhost:8000" )

#createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

putItem("madonnaSongs", "eu-west-2", "richardx14-3", "http://localhost:8000")

#putItem(table, region, userID, endpoint = '' )

#putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")

#putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-6")

getItem("madonnaSongs", "eu-west-2", "richardx14-2", "http://localhost:8000")

#def getItem(table, region, userID, endpoint = ''):

queryItem("madonnaSongs", "eu-west-2", "test-item-4","http://localhost:8000")

queryItem("madonnaSongs", "eu-west-2", "richardx14-1","http://localhost:8000")

#def queryItem(table, region, userID, endpoint = '' ):

deleteItem("madonnaSongs", "eu-west-2", "richardx14-1", "http://localhost:8000")

#def deleteItem(table, region, userID, endpoint = ''):

queryItem("madonnaSongs", "eu-west-2", "richardx14-1","http://localhost:8000")

#queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")

#queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-itemdsdfsdfasd")

updateItem("madonnaSongs", "eu-west-2", "richardx14-2", "Hanky Panky etc", 24, "http://localhost:8000")

getItem("madonnaSongs", "eu-west-2", "richardx14-2", "http://localhost:8000")

#getItem("madonnaSongs", "eu-west-2", "richardx14-2")

#queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")

#deleteTable("madonnaSongs", "eu-west-2", "http://localhost:8000" )

#createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

#tableExists("madonnaSongs", "eu-west-2", "http://localhost:8000")

createTable("madonnaSongs", "eu-west-2")

putItem("madonnaSongs", "eu-west-2", "richardx14-3")

tableExists("madonnaSongs", "eu-west-2")





