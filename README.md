# inventory_management_system_using_django<br/>
------------------------------------------
This is an inventory management system for three devices i.e. **laptops,mobiles and desktops**.<br /> 

## CONTENTS<br />
------------
 * Tech stack<br /> 
 * Installation<br /> 
 * Configuration<br /> 
 * Process<br /> 
 * Configuration<br /> 
 * Troubleshooting<br /> 
 * FAQ<br /> 
 * Maintainers<br /> 
## TECH STACK<br />
--------------
1.IDE-Visual studio code.OR you can use any IDE of your choice. <br /> 
2.Web browser-Google chrome <br /> 
3.Database-SQLite3 - In-Built database for Visual studio code projects by django. <br />
3.CSV file-Notepad<br /> 
4.Microsoft excel-Notepad<br /> 
## INSTALLATION<br />
----------------
Download and install<br />
1.Python django install use command in terminal: >>pip install django <br /> 
2.Python Django import export package-  use command in terminal:  >>pip install django-import-export <br /> 

## CONFIGURATION<br />
-----------------
python version : Python 3.10.1<br /> 
Django version: 4.0<br/>

## PROCESS<br />
-----------
### we will develop the project in three phases
1.Model-Defining the database schemas(Tables) for the three devices <br /> 
2.Interfaces-Defining the templates (The user sees these) <br /> 
3.Control - Writing the backend logic for the project<br /> 

### Step 1.Start a project and Run it on a web browser<br />
--------------------------------------------------
open the IDE and terminal. Go to the desired directory and start a project there using command<br />
>>django-admin startproject inventory_management<br />
Now run the server using following command and check if the project is running.<br />
>>python manage.py runserver<br /> 
### Step 2. Make a new app inventory for project <br />
-------------------------------------------------------
Start an app 'inventory' into our project and register it in the setting.py inside the installed app list.<br />
>>python manage.py startapp inventory<br />
### Step 3. Define models(Database) and makemigrations<br />
-------------------------------------------------------------
Note:make Devices only an abstract class so that other classes can inherit it and mantain the django principle 'Don't Repeat Yourself(DRY)'<br />
![image](https://user-images.githubusercontent.com/93670405/147202587-c42dfcaf-9c98-4c99-b3a1-05b81b5be2e6.png)<br/>
Run command >> python manage.py makemigrations<br/>
Run this command everytime if there is a change in the file 'models.py'<br /> 
### Step 4. Define Templates<br />
----------------------------------------------------------
Make two new folders called static and templates inside app inventory.<br />
Now refer **getbootstrap.com** and copy the css and javascript files in the folder static.<br />
create a file base.html and copy the navbar code from **getbootstrap.com** into it.We can use template inheritance to use the same navbar in multiple files in the project.<br />
add_new.html<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203136-732217f0-566c-4655-9a47-9f548a2c12c9.png)<br /> 
base.html<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203223-6c8ab196-32c6-429b-a8cd-53c317771346.png)<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203288-1c2b8405-7787-4f6b-950f-fae3c14af27a.png)<br /> 
edit_item.html<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203329-71db2800-f44e-47de-95dc-41ec786f0a17.png)<br /> 
index.html<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203391-ee7b7492-76df-45a6-996a-e2e7d38e72b8.png)<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203464-007a4440-ace8-4ae9-b0e8-423e86d79c1d.png)<br /> 
![image](https://user-images.githubusercontent.com/93670405/147203524-39021c32-0215-4606-ad21-e53dc546be96.png)<br /> 
### Step 5. Define forms<br />
------------------------------
forms.py<br/>
![image](https://user-images.githubusercontent.com/93670405/147203064-bd1579a5-7788-4cc0-9a62-b23ffcf00e51.png)<br /> 
### Step 6. Define views(backend logic)<br />
----------------------------------------------
![image](https://user-images.githubusercontent.com/93670405/147202772-d13085af-e4f8-4c2f-aa1c-01520402a09c.png)<br /> 
![image](https://user-images.githubusercontent.com/93670405/147202817-37f4005a-517e-43a1-92ce-51e9b94eb955.png)<br /> 
![image](https://user-images.githubusercontent.com/93670405/147202838-026ff348-ae3c-466b-bac1-1a884bffb5d4.png)<br /> 
![image](https://user-images.githubusercontent.com/93670405/147202901-42d2e336-912d-4c52-bc1d-eeb79615b2fc.png)<br /> 
### Step 7. Register the models in admin panel <br />
-----------------------------------------------------
![image](https://user-images.githubusercontent.com/93670405/147202951-00b89bb9-feb6-450a-83ba-7f14f09a655f.png)<br /> 
### Step 8. Download django-import-export package<br />
-------------------------------------------------------
use command  >> pip install django-import-export<br /> 
### Step 9. Migrate and Runserver<br />
----------------------------------------
use following commands<br/>
>>python manage.migrate<br/>
>>python manage.py runserver<br/>
