from madynamodb import createTable, deleteTable, createItem, getItem

# aws dynamodb list-tables --endpoint-url=http://localhost:8000

# createTable("madonnaSongs", "eu-west-2", "http://localhost:8000")

# deleteTable("madonnaSongs", "eu-west-2", "http://localhost:8000" )

createItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item")

getItem("madonnaSongs", "eu-west-2", "http://localhost:8000", "test-item")



