from madynamodb import createTable, deleteTable, putItem, getItem, queryItem, deleteItem, updateItem

# aws dynamodb list-tables --endpoint-url=http://localhost:8000

# createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

# deleteTable("madonnaSongs", "eu-west-2", "http://localhost:8000" )

putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-4")

putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")

putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-6")

getItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-6")

queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-4")

#deleteItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-4")

queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")

queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-itemdsdfsdfasd")

updateItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5", "Music etc", 23)

queryItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")




