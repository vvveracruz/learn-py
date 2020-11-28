```
brew install postgresql
```

Starting:
```
brew services start postgresql
```

Restarting:
```
brew services restart postgresql
```

Stop:
```
brew services stop postgresql
```

Logging into command line tools:
```
psql postgres
```
- This logs into the default databse called `postgres`.


List all users:
```
postgres=# \du
```

List all databases:
```
postgres=# \l
```

Create a database called `mydb`: 
```
postgres=# CREATE DATABASE mydb;
```
