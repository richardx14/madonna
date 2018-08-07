from madynamodb import createTable, deleteTable, putItem, getItem

# aws dynamodb list-tables --endpoint-url=http://localhost:8000

# createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

# deleteTable("madonnaSongs", "eu-west-2", "http://localhost:8000" )

putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-4")

putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-5")

putItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-6")

getItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item-6")



