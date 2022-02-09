<p align="center">
  <a href="https://github.com/swapnilsparsh/Rescue">
    <img src="https://github.com/swapnilsparsh/Rescue/blob/master/main_app/static/Images/rescues.gif" >
  </a>

  <h2 align="center"><b>Rescue (Women Safety Website)</b></h2>

  <p align="center">
    <p style align="center">📧 A women’s safety website that sends emails and messages to your trusted ones.🚺</p> 
    <br />
  </p>
</p>

# ✨About the Project

**RESCUE** is a responsive website to help women through panic and unsafe situations.<br>
A main feature of website is the <u>**Emergency Button**</u>.<br> If the person feels unsafe in any situtation, they can click on that emergency button and within no time an <u>**Alert Message**</u> will be sent to her <u>**Trusted Contacts**</u> with her <u>**Location Credentials**</u> that she is in need of help. 

_Our main aim is to help women with the support of latest technologies._

# 💻Technology Stack
Frontend

  <img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>   <img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>    <img src="https://img.shields.io/badge/bootstrap%20-%234f0599.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>

Backend

  <img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>   <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?&style=for-the-badge&logo=sqlite&logoColor=white"/>

# ⚙Installation

<p> Star the Repo 🌟 and this will keep me motivated. </p>

1. Download and install Python
2. Download and install Git.
3. Fork the Repository.
4. Clone the repository to your local machine 
```sh
git clone https://github.com/<your-github-username>/Rescue.git
```

5. Change directory to main_app
```sh
cd main_app
```

6.. Install django and other requirements by using the command below.
```sh
pip install -r requirements.txt
```

4. Fill the details in the files: 
  
  * [main_app/mail.py](main_app/mail.py)

  * [mysite/settings.py](main_app/settings.py)

5. Make migrations
```bash
python manage.py makemigrations
```

6. Migrate the changes to the database
```bash 
python manage.py migrate
```

7. Create admin 
```bash
python manage.py createsuperuser
```

8. Run the server
```bash
python manage.py runserver
```

9. View the website - 
    - [Click here](https://localhost:8000 "https://localhost:8000")
    <br> OR <br>
    - Paste the following in your browser
      ```bash
      https://localhost:8000
      ```

# Lint and Format 📜

We are using [Flake8](https://flake8.pycqa.org/en/latest/manpage.html) and [Black](https://pypi.org/project/black/) for _linting & formatting_ source code of this project.

### **Run QA checks on local environment ⚡** :

<br>

* For Windows 💾 :
```sh
...\rescue> .\rescue_QA_checks
``` 

* For Linux 👨‍💻 :
```bash
.../rescue$ ./rescue_QA_checks
``` 

* Alternate option ✔ Run the following commands ⚡:
  * For Windows 💾
    ```
    ...\rescue> black .
    ``` 
    ```
    ...\rescue> flake8 .
    ``` 
  * For Linux 👨‍💻
    ```
    .../rescue$ black .
    ``` 
    ```
    .../rescue$ flake8 .
    ``` 

# First time to [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Read [How to Contribute.](https://github.com/swapnilsparsh/Rescue/blob/master/Contributing.md)


# ✨Our Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<table>
	<tr>
		<td>
			<a href="https://github.com/swapnilsparsh/Rescue/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=swapnilsparsh/Rescue" />
</a>
		</td>
	</tr>
</table>

# Code Of Conduct

You can find our Code of Conduct [here](/Code_of_Conduct.md).


# 📄License

<a href="./LICENSE" target="_blank">
<img src="https://img.shields.io/badge/license-MIT-green" alt=MIT>
</a>

# Project Maintainer
### [Swapnil Srivastava](https://github.com/swapnilsparsh)
### [Utkarsh Mall](https://github.com/iamutkarshmall)
### [Utkarsh Sharma](https://github.com/U-c0de)

<div align="left">
<a href="https://github.com/swapnilsparsh" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://www.linkedin.com/in/swapnil-srivastava-sparsh/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
</div>
