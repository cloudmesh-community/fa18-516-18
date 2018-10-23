import aws_setup

d = aws_setup.driver.list_container_objects(aws_setup.container)
print(d)
