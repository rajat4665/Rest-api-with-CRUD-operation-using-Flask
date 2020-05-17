# Rest-api-with-CRUD-operation-using-Flask
<h3>Introduction:</h3>
Hi, reader, I hope you are doing great. Today I came up with an Innovative article for creating rest api in Flask framework. We have already discussed Django web  development framework. In this Article I have Created an api with CRUD operation. Basically CRUD Stands for Create-Read-Update-Delete in our data base.  I have used SQLite database because of it is portable.
<h3>What is Flask and Why Flask ?</h3>
Flask is one of the most popular python's web development framework. Most developer prefer flask because its simplicity and its light weight. In a nutshell it  is easy to work with flask as Compared with Django.
<h3>File Structure of this Project:</h3>
Usually flask app have only one file but I have split this project in 3 mains file just because of easiness.

<img class="alignnone size-full wp-image-209" src="https://getpython.files.wordpress.com/2020/05/screenshot-from-2020-05-17-21-24-22.png" alt="Screenshot from 2020-05-17 21-24-22" width="726" height="401" />

 

Lets talk about these files briefly :

<strong>data.sqlite:</strong> As I already discussed I have used Sqlite database for this rest api because it is portable and it remove the dependency to setup new database. This data.sqlite file is our database file which is connected using  SQLAlchemy.

<strong>models.py:  </strong>This file contains our database table details, In this file we can change our table structures like add new fields , remove existing one and add other validation properties.

<strong>settings.py: </strong>This is our settings file where we can define configurations of our application like define our database setting and debug settings. In this file I have defined two paths for linux as well as for windows os. Currently I have commented windows path and used linux path. If you are using window just uncomment it.

<strong>myapp.py: </strong>This is core file of our api which will handle all the CRUD operation on specific url with specified Http request method. I have created methods for handling Http request and performing CRUD operations.

<strong>requirement.txt: </strong>This is file contains dependencies information to run this project.

 
<h3>Requirements:</h3>
<ul>
	<li>Python 3.6+</li>
	<li>Flask</li>
	<li><a href="https://www.postman.com/downloads/" target="_blank" rel="noopener">postman</a></li>
</ul>
<h3>what you will learn from this tutorial:</h3>
 
<ul>
	<li>How to build rest Api in Flask</li>
	<li>Create database with Flask using SQLAlchemy</li>
	<li>Handling CRUD Operations</li>
</ul>
<h3>how to run this code:</h3>
<ul>
	<li>clone or download it from <a href="https://github.com/rajat4665/Rest-api-with-CRUD-operation-using-Flask" target="_blank" rel="noopener">here</a></li>
	<li>install requirements.txt file</li>
	<li><code>pip install -r requirements.txt</code></li>
	<li>run this command to execute this code
<pre>python myapp.py</pre>
<img class="alignnone size-full wp-image-210" src="https://getpython.files.wordpress.com/2020/05/screenshot-from-2020-05-17-21-47-20.png" alt="Screenshot from 2020-05-17 21-47-20" width="1279" height="528" />

When it runs your temrminal/cmd will be like above image</li>
</ul>
<h3>Output:</h3>
<ul>
	<li><strong>For fetching all user records</strong>, Just browse this url in your browser <strong>http://0.0.0.0:5000/user</strong></li>
</ul>
<img class="alignnone size-full wp-image-211" src="https://getpython.files.wordpress.com/2020/05/screenshot-from-2020-05-14-14-34-02-e1589732525173.png" alt="Screenshot from 2020-05-14 14-34-02" width="431" height="594" />
<ul>
	<li><strong>For creating new user with post request using postman</strong></li>
</ul>
<img class="alignnone size-full wp-image-212" src="https://getpython.files.wordpress.com/2020/05/screenshot-from-2020-05-14-14-31-31.png" alt="Screenshot from 2020-05-14 14-31-31" width="966" height="607" />
<ul>
	<li><strong>Update user details using Put request using Postman</strong></li>
	<li><img class="alignnone size-full wp-image-213" src="https://getpython.files.wordpress.com/2020/05/screenshot-from-2020-05-14-14-32-13.png" alt="Screenshot from 2020-05-14 14-32-13" width="928" height="604" /></li>
</ul>
 
<ul>
	<li><strong>Delete user using delete user using postman</strong></li>
	<li><img class="alignnone size-full wp-image-214" src="https://getpython.files.wordpress.com/2020/05/screenshot-from-2020-05-14-14-33-14.png" alt="Screenshot from 2020-05-14 14-33-14" width="946" height="434" /></li>
</ul>
 
