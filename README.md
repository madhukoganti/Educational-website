\# Educational Website



A Django-based educational website designed to provide students, parents, and visitors with information about classes, school activities, latest news, gallery, and contact/registration services.



\## Project Overview



This project is developed using Django and provides a simple and user-friendly educational website.



The website contains different sections for displaying educational information and also includes forms for collecting parent registration and contact information.



\## Features



\- Home page

\- About page

\- Classes section

\- Class-wise pages

\- Gallery

\- Photos and videos

\- Latest News section

\- Parent Registration form

\- Contact form

\- Admin data page

\- Django admin panel

\- Database-backed form submissions

\- Separate handling of Parent Registration and Contact information



\## Technologies Used



\- Python

\- Django

\- HTML

\- CSS

\- SQLite

\- Git

\- GitHub



\## Project Structure



```text

Educational-website/

│

├── app1/

│   ├── migrations/

│   ├── admin.py

│   ├── apps.py

│   ├── forms.py

│   ├── models.py

│   ├── tests.py

│   └── views.py

│

├── djangoproject1/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── static/

│   ├── css/

│   └── images/

│

├── templates/

│   └── app1/

│

├── manage.py

├── .gitignore

└── README.md

```



\## Main Functionalities



\### Parent Registration



Parents can submit their details through the Parent Registration form. The submitted information is stored in the database and can be viewed through the website's admin functionality.



\### Contact Form



Visitors can submit their name, phone number, email address, and message through the Contact form.



The Contact functionality is maintained separately from Parent Registration.



\### Educational Pages



The website provides dedicated pages for:



\- Classes

\- Class 8

\- Class 9

\- Class 10

\- Gallery

\- Photos

\- Videos

\- Latest News

\- About



\## Django Admin



The Django admin panel can be used to manage the application's stored data.



An administrator can access the Django admin interface and manage registered information.



\## How to Run the Project



\### 1. Clone the repository



```bash

git clone https://github.com/madhukoganti/Educational-website.git

```



\### 2. Navigate to the project directory



```bash

cd Educational-website

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



\*\*Windows:\*\*



```powershell

venv\\Scripts\\activate

```



\### 5. Install Django



```bash

pip install django

```



\### 6. Apply migrations



```bash

python manage.py migrate

```



\### 7. Start the development server



```bash

python manage.py runserver

```



\### 8. Open the website



Open the URL shown by Django in your browser, usually:



```text

http://127.0.0.1:8000/

```



\## Future Improvements



\- Deploy the website to a cloud hosting platform

\- Improve responsive design for mobile devices

\- Add user authentication

\- Add a dedicated student portal

\- Add online admission functionality

\- Add search functionality

\- Improve admin dashboard

\- Add automated testing



\## Author



\*\*Madhulatha\*\*



GitHub: https://github.com/madhukoganti

