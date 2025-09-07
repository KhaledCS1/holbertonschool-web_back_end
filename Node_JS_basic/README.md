Node JS basic - quick guide

Run examples
- 0-constants.js (stdout helper):
	node -e "require('./0-constants')('Hello Holberton School!')"

- 1-stdin.js (interactive):
	node 1-stdin.js

- 2-read_file.js (sync parsing):
	node -e "require('./2-read_file')('database.csv')"

- 3-read_file_async.js (async parsing):
	node -e "require('./3-read_file_async')('database.csv')"

- 4-http.js (HTTP hello):
	node 4-http.js
	curl http://127.0.0.1:1245/

- 5-http.js (HTTP + students):
	node 5-http.js database.csv
	curl http://127.0.0.1:1245/students

- 6-http_express.js (Express hello):
	node 6-http_express.js
	curl http://127.0.0.1:1245/

- 7-http_express.js (Express + students):
	node 7-http_express.js database.csv
	curl http://127.0.0.1:1245/students

Notes
- CSV must include a header row with at least firstname and field columns.
- Trailing blank lines are ignored.
