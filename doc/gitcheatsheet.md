************************************************************************
#####    VIRTUAL ENV      
************************************************************************
```shell
cd ~
mkdir eclipsevirtualenv
virtualenv eclipsevirtualenv/ref_env
source eclipsevirtualenv/ref_env/bin/activate

#here we are

pip install yolk
yolk -l
pip install pymongo
yolk -l

#YEAH !!!
```


eclipse->project->properties->new interpreter 

************************************************************************
#####     CASSANDRA
************************************************************************
pip install cql
pip install pycassa

 
sudo apt-get install cassandra
cassandra-cli
connect localhost/9160;
CREATE KEYSPACE CassandraTest with placement_strategy = 'org.apache.cassandra.locator.SimpleStrategy'and strategy_options = {replication_factor:1};
use CassandraTest;
CREATE COLUMN FAMILY users	WITH comparator = UTF8Type;
CREATE COLUMN FAMILY test	WITH comparator = IntegerType;

drop KEYSPACE CassandraTest;

http://www.datastax.com/docs/1.1/dml/using_cli

************************************************************************
#####     MONGODB
************************************************************************
sudo pip install pymongo


************************************************************************
#####     GIT
************************************************************************
```shell
git config --list

git config --global user.name "John Doe"

git clone git://github.com/schacon/grit.git

git clone https://github.com/GustavePate/sandbox.git

git status

git add README

cat .gitignore

# diff not staged <-> staged
git diff


#diff staged <-> last commit ==  next commit
git diff --staged

#committing staged diff
git commit -m "my commit comment"

#commit also not staged files
git commit -a -m "my commit comment"

#supprimer un fichier staged
git rm --cached readme.txt

#deplacer un fichier
git mv test.py hello.py

#listing des commits
git log

#listing des commits avec diff
git log -p


#listing des 2 derniers commits avec diff
git log -p -2

#volume des commitsq
git log --stat

#tout sur une ligne
git log --pretty=oneline
git log --pretty=format:"%h - %an, %ar : %s"

#listing des serveurs
git remote -v

#Tout pousser sur le serveur
git push origin master
```


