server:
    pip install -e .
	python cloudmesh_data/data/server.py

test:
	@head -c 79 /dev/zero |tr '\0' '#'
	@echo
	@echo  TEST
	@head -c 79 /dev/zero |tr '\0' '#'
	@echo
	@echo
	test/test.sh

file:
	@echo "----------------------LIST OF FILES FROM GOOGLE------------------"
	curl GET "http://localhost:5000/cloudmesh_data/files?service=google_cloud"
	sleep 5
	@echo "---------------------DOWNLOAD A FILE FROM GOOGLE-----------------"
	curl GET "http://localhost:5000/cloudmesh_data/file?service=google_cloud&filename=MapReduce.docx&user_uuid=richa"
	@echo "---------------------FILE DOWNLOADED TO GOOGLE PROVIDER DIRECTORY CREATED------------------"
	sleep 5
	@echo "---------------------DELETE THE FILE FROM GOOGLE--------------------------------------"
	curl -X DELETE "http://localhost:5000/cloudmesh_data/file/delete?service=google_cloud&filename=MapReduce.docx"
	@echo "---------------------FILE DELETED IN GOOGLE-----------------------------------------"

