import sys
from PyQt5.QtWidgets import QTextEdit, QScrollBar, QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QLineEdit, QDateEdit, QListWidget, QListWidgetItem
from PyQt5.QtGui import QDoubleValidator
import mysql.connector
from PyQt5.QtCore import Qt, QDate


db_config = {
    'host': 'db4free.net',
    'user': 'mohanad',
    'password': 'mohanad123456',
    'database': 'mohanad_wuzzuf',
    'raise_on_warnings': True
}
def fetch_skills_from_database():
    try:
        connection = mysql.connector.connect(**db_config)

        cursor = connection.cursor()

        query = "SELECT DISTINCT skill FROM job_posting_skills;"
        cursor.execute(query)

        skills = cursor.fetchall()

        cursor.close()
        connection.close()

        return [skill[0] for skill in skills]

    except Exception as e:
        print(f"Error fetching skills from the database: {e}")
        return []
class WuzzufDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Welcome to the Wuzzuf Dashboard!\n\n")

        self.menu_combo = QComboBox(self)
        self.menu_combo.addItem("Register a user")
        self.menu_combo.addItem("Add a new user application for an existing Job posting")
        self.menu_combo.addItem("Show all the job postings for a given sector")
        self.menu_combo.addItem("Show all the job postings for a given set of skills")
        self.menu_combo.addItem("Show the top 5 sectors by number of job posts, and the average salary range for each")
        self.menu_combo.addItem("Show the top 5 skills that are in the highest demand")
        self.menu_combo.addItem("Show the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date")
        self.menu_combo.addItem("Show the top 5 most paying companies in the field in Egypt")
        self.menu_combo.addItem("Show all the postings for a given company / organization")
        self.menu_combo.addItem("Show the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings")
        
        
        
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)  
        
        scrollbar = QScrollBar(self)
        scrollbar.setOrientation(Qt.Vertical)
        scrollbar.valueChanged.connect(self.result_text.verticalScrollBar().setValue)


        self.ok_button = QPushButton("OK", self)
        self.search_input = QLineEdit(self)

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit(self)
        self.email_label = QLabel("Email Address:")
        self.email_input = QLineEdit(self)
        self.gpa_label = QLabel("GPA:")
        self.gpa_input = QLineEdit(self)
        self.gpa_input.setValidator(QDoubleValidator(0.00, 4.00, 2))
        self.birthdate_label = QLabel("Birthdate:")
        self.birthdate_input = QDateEdit(self)
        self.gender_label = QLabel("Gender:")
        self.gender_input = QComboBox(self)
        self.gender_input.addItems(['M', 'F'])
        self.skills_label = QLabel("Skills:")
        self.skills_input = QListWidget(self)
        

        skills_from_database = fetch_skills_from_database()
        for skill in skills_from_database:
            item = QListWidgetItem(skill)
            self.skills_input.addItem(item)
        self.skills_input.setSelectionMode(QListWidget.MultiSelection)
        
        

        self.job_postings_combo = QComboBox(self)
        self.populate_job_postings_combo()  

        self.username_input_app = QLineEdit(self)
        self.application_date_input = QDateEdit(QDate.currentDate(), self)
        self.application_date_input.setDisplayFormat("yyyy-MM-dd")
        self.application_date_input.setReadOnly(True)
        self.cover_letter_input = QTextEdit(self)
        self.submit_button = QPushButton("Submit Application", self)
        self.submit_button.clicked.connect(self.submit_application)


        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.hide()  
        self.confirm_button.clicked.connect(self.on_confirm_button_click)
        self.search_button = QPushButton("Search", self)
        self.search_button.hide()  
        self.search_button.clicked.connect(self.on_search_button_click)
        self.username_label.hide()
        self.username_input.hide()
        self.email_label.hide()
        self.email_input.hide()
        self.gpa_label.hide()
        self.gpa_input.hide()
        self.birthdate_label.hide()
        self.birthdate_input.hide()
        self.gender_label.hide()
        self.gender_input.hide()
        self.skills_label.hide()
        self.skills_input.hide()
        self.search_input.hide()
        self.result_text.hide()

        self.job_postings_app = QLabel("Available job postings:")
        self.job_postings_combo.hide()
        self.job_postings_app.hide()
        self.username_input_app_label = QLabel("Username:")
        self.username_input_app.hide()
        self.username_input_app_label.hide()
        self.application_date_input_label = QLabel("Date:")
        self.application_date_input.hide()
        self.application_date_input_label.hide()
        self.cover_letter_input_label = QLabel("Cover letter:")
        self.cover_letter_input.hide()
        self.cover_letter_input_label.hide()
        self.submit_button.hide()
        


        self.ok_button.clicked.connect(self.on_ok_button_click)


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.result_text)

        layout.addWidget(self.menu_combo)
        layout.addWidget(self.ok_button)


        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.gpa_label)
        layout.addWidget(self.gpa_input)
        layout.addWidget(self.birthdate_label)
        layout.addWidget(self.birthdate_input)
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)
        layout.addWidget(self.skills_label)
        layout.addWidget(self.skills_input)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        
        layout.addWidget(self.job_postings_app)
        layout.addWidget(self.job_postings_combo)
        layout.addWidget(self.username_input_app_label)
        layout.addWidget(self.username_input_app)
        layout.addWidget(self.application_date_input_label)
        layout.addWidget(self.application_date_input)
        layout.addWidget(self.cover_letter_input_label)
        layout.addWidget(self.cover_letter_input)
        layout.addWidget(self.submit_button)
        

        self.setLayout(layout)

        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Wuzzuf Dashboard')
        self.show()
        
    def on_ok_button_click(self):
        self.confirm_button.hide()  
        self.search_button.hide()  
        self.username_label.hide()
        self.username_input.hide()
        self.email_label.hide()
        self.email_input.hide()
        self.gpa_label.hide()
        self.gpa_input.hide()
        self.birthdate_label.hide()
        self.birthdate_input.hide()
        self.gender_label.hide()
        self.gender_input.hide()
        self.skills_label.hide()
        self.skills_input.hide()
        self.search_input.hide()
        self.result_text.hide()
        
        self.job_postings_combo.hide()
        self.job_postings_app.hide()
        self.username_input_app.hide()
        self.username_input_app_label.hide()
        self.application_date_input.hide()
        self.application_date_input_label.hide()
        self.cover_letter_input.hide()
        self.cover_letter_input_label.hide()
        self.submit_button.hide()
        
        
        selected_option = self.menu_combo.currentText()
        self.label.setText(f"")
        self.result_text.setText(f"")

        if selected_option == "Register a user":

            self.username_label.show()
            self.username_input.show()
            self.email_label.show()
            self.email_input.show()
            self.gpa_label.show()
            self.gpa_input.show()
            self.birthdate_label.show()
            self.birthdate_input.show()
            self.gender_label.show()
            self.gender_input.show()
            self.skills_label.show()
            self.skills_input.show()
            self.confirm_button.show()
        
        else:

            self.username_label.hide()
            self.username_input.hide()
            self.email_label.hide()
            self.email_input.hide()
            self.gpa_label.hide()
            self.gpa_input.hide()
            self.birthdate_label.hide()
            self.birthdate_input.hide()
            self.gender_label.hide()
            self.gender_input.hide()
            self.skills_label.hide()
            self.skills_input.hide()
            self.confirm_button.hide()
        
        if selected_option:

            self.execute_query_for_option(selected_option)


    def format_data_query_top_sectors_and_avg_salary(self, data):
        if data:
            result_str = "Top 5 Sectors by Number of Job Posts and Average Salary Range:\n\n"

            for item in data:
                sector, job_postings_count, avg_salary_range = item
                result_str += f"Sector: {sector}\nJob Postings Count: {job_postings_count}\nAverage Salary Range: {avg_salary_range:,.2f}\n\n"

            return result_str
        else:
            return "No data available."
    
    def format_data_query_top_skills_in_demand(self, data):
        if data:
            result_str = "Top 5 skills that are in the highest demand:\n\n"

            for item in data:
                skill, DemandCount = item
                result_str += f"Skill: {skill}\nDemand Count: {DemandCount}\n\n"

            return result_str
        else:
            return "No data available."

    def format_data_query_top_growing_startups(self, data):
        if data:
            result_str = "Top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date:\n\n"

            for item in data:
                Startup, FoundationDate, TotalVacancies, VacanciesPerYear = item
                result_str += f"Startup: {Startup}\nFoundation Date: {FoundationDate}\nTotal Vacancies: {TotalVacancies}\nVacancies Per Year: {VacanciesPerYear:,.2f}\n\n"

            return result_str
        else:
            return "No data available."
        
    def format_data_query_top_paying_companies(self, data):
        if data:
            result_str = "Top 5 most paying companies in the field in Egypt:\n\n"

            for item in data:
                Company, AverageSalary = item
                result_str += f"Company: {Company}\nAverage Salary: {AverageSalary:,.2f}\n\n"

            return result_str
        else:
            return "No data available."
    
    def format_data_query_top_categories_cross_listed(self, data):
        if data:
            result_str = "Top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings:\n\n"

            for item in data:
                Category, PostingsCount = item
                result_str += f"Category: {Category}\nPostings Count: {PostingsCount}\n\n"

            return result_str
        else:
            return "No data available."
        
    def execute_query_for_option(self, option):
        if option == "Register a user":
            self.label.setText("Please fill in the following information to register a user:")
            self.result_text.hide()
        elif option == "Add a new user application for an existing Job posting":
            self.search_input.hide()
            self.search_button.hide()
            self.result_text.hide()
            
            self.job_postings_combo.show()
            self.job_postings_app.show()
            self.username_input_app.show()
            self.username_input_app_label.show()
            self.application_date_input.show()
            self.application_date_input_label.show()
            self.cover_letter_input.show()
            self.cover_letter_input_label.show()
            self.submit_button.show()
        elif option == "Show all the job postings for a given sector":
            self.search_input.show()
            self.search_button.show()
        elif option == "Show all the job postings for a given set of skills":
            self.skills_input.show()
            self.search_button.show()
            self.result_text.hide()
        elif option == "Show the top 5 sectors by number of job posts, and the average salary range for each":
            self.result_text.hide()
            self.label.setText(f"{self.format_data_query_top_sectors_and_avg_salary(self.query_top_sectors_and_avg_salary())}")
        elif option == "Show the top 5 skills that are in the highest demand":
            self.search_input.hide()
            self.result_text.hide()
            self.search_button.hide()
            self.label.setText(f"{self.format_data_query_top_skills_in_demand(self.query_top_skills_in_demand())}")
        elif option == "Show the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date":
            self.search_input.hide()
            self.result_text.hide()
            self.search_button.hide()
            self.label.setText(f"{self.format_data_query_top_growing_startups(self.query_top_growing_startups())}")
        elif option == "Show the top 5 most paying companies in the field in Egypt":
            self.search_input.hide()
            self.result_text.hide()
            self.search_button.hide()
            self.label.setText(f"{self.format_data_query_top_paying_companies(self.query_top_paying_companies())}")
        elif option == "Show all the postings for a given company / organization":
            self.search_input.show()
            self.search_button.show()
        elif option == "Show the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings":
            self.search_input.hide()
            self.search_button.hide()
            self.result_text.hide()
            self.label.setText(f"{self.format_data_query_top_categories_cross_listed(self.query_top_categories_cross_listed())}")
    
    def populate_job_postings_combo(self):
        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                SELECT title, company_name FROM job_posting
            """

            cursor.execute(query)


            job_postings = cursor.fetchall()


            for job_posting in job_postings:
                title, company_name = job_posting
                self.job_postings_combo.addItem(f"{title} ~ {company_name}")


            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error fetching job postings: {e}")

    def submit_application(self):

        selected_job_posting = self.job_postings_combo.currentText()
        title, company_name = selected_job_posting.split(' ~ ')

        username = self.username_input_app.text()
        application_date = self.application_date_input.date().toString("yyyy-MM-dd")
        cover_letter = self.cover_letter_input.toPlainText()

        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                INSERT INTO application (username, title, company_name, application_date, cover_letter)
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(query, (username, title, company_name, application_date, cover_letter))


            connection.commit()


            cursor.close()
            connection.close()


            self.label.setText("Application submitted successfully!")

        except Exception as e:
            self.label.setText(f"Error submitting application: {e}")
    
    
    def on_search_button_click(self):
        if(self.menu_combo.currentText() == "Show all the job postings for a given sector"):
            self.result_text.show()
            sector_value = self.search_input.text()
            
            try:

                connection = mysql.connector.connect(**db_config)


                cursor = connection.cursor()


                query = """
                    SELECT
                        jp.*
                    FROM
                        job_posting jp
                    JOIN
                        company_industry ci ON jp.company_name = ci.company_name
                    WHERE
                        ci.industry = %s
                """

                cursor.execute(query, (sector_value + '\r',))


                result_data = cursor.fetchall()


                cursor.close()
                connection.close()
                if result_data:
                    result_str = f"All job postings in the {sector_value} sector:\n\n"

                    for item in result_data:
                        title, experience_needed, career_level, educational_level, min_salary, max_salary, gender, job_description, requirements, vacancies, company_name, Location_Part1, Location_Part2 = item
                        title_str = f"Title: {title}\n" if title is not None else ""
                        experience_str = f"Experience Needed: {experience_needed} years\n" if experience_needed is not None else ""
                        career_level_str = f"Career Level: {career_level}\n" if career_level is not None else ""
                        educational_level_str = f"Educational Level: {educational_level}\n" if educational_level is not None else ""
                        min_salary_str = f"Min Salary: {min_salary:,.2f}\n" if min_salary is not None else ""
                        max_salary_str = f"Max Salary: {max_salary:,.2f}\n" if max_salary is not None else ""
                        gender_str = f"Gender: {gender}\n" if gender is not None else ""
                        job_description_str = f"Job Description: {job_description}\n" if job_description is not None else ""
                        requirements_str = f"Requirements: {requirements}\n" if requirements is not None else ""
                        vacancies_str = f"Vacancies: {vacancies}\n" if vacancies is not None else ""
                        company_name_str = f"Company: {company_name}\n" if company_name is not None else ""
                        location_str = f"Location: {Location_Part1}, {Location_Part2}\n" if Location_Part1 is not None and Location_Part2 is not None else ""

                        result_str += f"{title_str}{experience_str}{career_level_str}{educational_level_str}{min_salary_str}{max_salary_str}{gender_str}{job_description_str}{requirements_str}{vacancies_str}{company_name_str}{location_str}\n"

                else:
                    result_str = "No data available"
                self.result_text.setPlainText(result_str)
            
            except Exception as e:
                print(f"Error executing query: {e}")
                
        elif (self.menu_combo.currentText() == "Show all the postings for a given company / organization"):
            self.result_text.show()
            company_name_value = self.search_input.text()
            
            try:

                connection = mysql.connector.connect(**db_config)


                cursor = connection.cursor()


                query = """
                    SELECT
                        jp.*
                    FROM
                        job_posting jp
                    WHERE
                        jp.company_name = %s
                """

                cursor.execute(query, (company_name_value,))


                result_data = cursor.fetchall()


                cursor.close()
                connection.close()
                if result_data:
                    result_str = f"All job postings for the company {company_name_value}:\n\n"

                    for item in result_data:
                        title, experience_needed, career_level, educational_level, min_salary, max_salary, gender, job_description, requirements, vacancies, company_name, Location_Part1, Location_Part2 = item
                        title_str = f"Title: {title}\n" if title is not None else ""
                        experience_str = f"Experience Needed: {experience_needed} years\n" if experience_needed is not None else ""
                        career_level_str = f"Career Level: {career_level}\n" if career_level is not None else ""
                        educational_level_str = f"Educational Level: {educational_level}\n" if educational_level is not None else ""
                        min_salary_str = f"Min Salary: {min_salary:,.2f}\n" if min_salary is not None else ""
                        max_salary_str = f"Max Salary: {max_salary:,.2f}\n" if max_salary is not None else ""
                        gender_str = f"Gender: {gender}\n" if gender is not None else ""
                        job_description_str = f"Job Description: {job_description}\n" if job_description is not None else ""
                        requirements_str = f"Requirements: {requirements}\n" if requirements is not None else ""
                        vacancies_str = f"Vacancies: {vacancies}\n" if vacancies is not None else ""
                        company_name_str = f"Company: {company_name}\n" if company_name is not None else ""
                        location_str = f"Location: {Location_Part1}, {Location_Part2}\n" if Location_Part1 is not None and Location_Part2 is not None else ""

                        result_str += f"{title_str}{experience_str}{career_level_str}{educational_level_str}{min_salary_str}{max_salary_str}{gender_str}{job_description_str}{requirements_str}{vacancies_str}{company_name_str}{location_str}\n"

                else:
                    result_str = "No data available"
                self.result_text.setPlainText(result_str)
            
            except Exception as e:
                print(f"Error executing query: {e}")
        
        elif (self.menu_combo.currentText() == "Show all the job postings for a given set of skills"):
            skills = [item.text() for item in self.skills_input.selectedItems()]
            self.result_text.show()
            try:

                connection = mysql.connector.connect(**db_config)


                cursor = connection.cursor()


                query = """
                    SELECT
                        jp.*
                    FROM
                        job_posting jp
                    JOIN
                        job_posting_skills jps ON jp.title = jps.title AND jp.company_name = jps.company_name
                    WHERE
                        jps.skill IN ({})
                """.format(', '.join(['%s' + '\r'] * len(skills)))


                cursor.execute(query, tuple(skills))


                result_data = cursor.fetchall()


                cursor.close()
                connection.close()
                   
                if result_data:
                    result_str = f"All job postings for the selected skills:\n\n"

                    for item in result_data:
                        title, experience_needed, career_level, educational_level, min_salary, max_salary, gender, job_description, requirements, vacancies, company_name, Location_Part1, Location_Part2 = item
                        title_str = f"Title: {title}\n" if title is not None else ""
                        experience_str = f"Experience Needed: {experience_needed} years\n" if experience_needed is not None else ""
                        career_level_str = f"Career Level: {career_level}\n" if career_level is not None else ""
                        educational_level_str = f"Educational Level: {educational_level}\n" if educational_level is not None else ""
                        min_salary_str = f"Min Salary: {min_salary:,.2f}\n" if min_salary is not None else ""
                        max_salary_str = f"Max Salary: {max_salary:,.2f}\n" if max_salary is not None else ""
                        gender_str = f"Gender: {gender}\n" if gender is not None else ""
                        job_description_str = f"Job Description: {job_description}\n" if job_description is not None else ""
                        requirements_str = f"Requirements: {requirements}\n" if requirements is not None else ""
                        vacancies_str = f"Vacancies: {vacancies}\n" if vacancies is not None else ""
                        company_name_str = f"Company: {company_name}\n" if company_name is not None else ""
                        location_str = f"Location: {Location_Part1}, {Location_Part2}\n" if Location_Part1 is not None and Location_Part2 is not None else ""

                        result_str += f"{title_str}{experience_str}{career_level_str}{educational_level_str}{min_salary_str}{max_salary_str}{gender_str}{job_description_str}{requirements_str}{vacancies_str}{company_name_str}{location_str}\n"

                else:
                    result_str = "No data available"
                self.result_text.setPlainText(result_str)
            
            except Exception as e:
                print(f"Error executing query: {e}")                                     
    
    def on_confirm_button_click(self):

        username = self.username_input.text()
        email_address = self.email_input.text()
        gpa = self.gpa_input.text()
        birthdate = self.birthdate_input.date().toString("yyyy-MM-dd")
        gender = self.gender_input.currentText()


        user_insert_query = "INSERT INTO wuzzuf_user (username, email_address, gpa, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        user_data = (username, email_address, gpa, birthdate, gender)
        self.execute_query(user_insert_query, user_data)


        skills = [item.text() for item in self.skills_input.selectedItems()]


        skills_insert_query = "INSERT INTO user_skills (username, skill) VALUES (%s, %s)"
        skills_data = [(username, skill) for skill in skills]
        self.execute_many_query(skills_insert_query, skills_data)



    def execute_query(self, query, data):
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()
            self.label.setText(f"User registered successfully!")
        except Exception as e:
            self.label.setText(f"Error executing query: {e}")

    def execute_many_query(self, query, data):
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.executemany(query, data)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            self.label.setText(f"Error executing query: {e}")


    def query_top_sectors_and_avg_salary(self):
        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                SELECT
                    c.industry AS Sector,
                    COUNT(jp.title) AS JobPostingsCount,
                    AVG(jp.min_salary + jp.max_salary) / 2 AS AverageSalaryRange
                FROM
                    company_industry c
                INNER JOIN
                    job_posting jp ON c.company_name = jp.company_name
                GROUP BY
                    c.industry
                ORDER BY
                    JobPostingsCount DESC
                LIMIT 5;
            """
            cursor.execute(query)


            result_data = cursor.fetchall()


            cursor.close()
            connection.close()

            return result_data

        except Exception as e:
            print(f"Error executing query: {e}")
            return []

    def query_top_skills_in_demand(self):
        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                SELECT
                    jps.skill AS Skill,
                    COUNT(jps.skill) AS DemandCount
                FROM
                    job_posting_skills jps
                GROUP BY
                    jps.skill
                ORDER BY
                    DemandCount DESC
                LIMIT 5;
            """
            cursor.execute(query)


            result_data = cursor.fetchall()


            cursor.close()
            connection.close()

            return result_data

        except Exception as e:
            print(f"Error executing query: {e}")
            return []

    def query_top_growing_startups(self):
        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                SELECT
                    c.company_name AS Startup,
                    c.foundation_date AS FoundationDate,
                    COUNT(jp.vacancies) AS TotalVacancies,
                    COUNT(jp.vacancies) / (YEAR(CURDATE()) - c.foundation_date + 1) AS VacanciesPerYear
                FROM
                    company c
                JOIN
                    job_posting jp ON c.company_name = jp.company_name
                WHERE
                    c.country = 'Egypt\r'
                GROUP BY
                    c.company_name, c.foundation_date
                ORDER BY
                    VacanciesPerYear DESC
                LIMIT 5;
            """
            cursor.execute(query)


            result_data = cursor.fetchall()


            cursor.close()
            connection.close()

            return result_data

        except Exception as e:
            print(f"Error executing query: {e}")
            return []

    def query_top_paying_companies(self):
        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                SELECT
                    jp.company_name AS Company,
                    AVG(jp.min_salary + jp.max_salary) / 2 AS AverageSalary
                FROM
                    job_posting jp
                JOIN
                    company c ON jp.company_name = c.company_name
                WHERE
                    c.country = 'Egypt\r'
                GROUP BY
                    jp.company_name
                ORDER BY
                    AverageSalary DESC
                LIMIT 5;
            """
            cursor.execute(query)


            result_data = cursor.fetchall()


            cursor.close()
            connection.close()

            return result_data

        except Exception as e:
            print(f"Error executing query: {e}")
            return []

    def query_top_categories_cross_listed(self):
        try:

            connection = mysql.connector.connect(**db_config)


            cursor = connection.cursor()


            query = """
                SELECT
                    jpc.category AS Category,
                    COUNT(*) AS PostingsCount
                FROM
                    job_posting_categories jpc
                WHERE
                    jpc.category != 'IT/Software Development\r'
                GROUP BY
                    jpc.category
                ORDER BY
                    PostingsCount DESC
                LIMIT 5;
            """
            cursor.execute(query)


            result_data = cursor.fetchall()


            cursor.close()
            connection.close()

            return result_data

        except Exception as e:
            print(f"Error executing query: {e}")
            return []


    def format_data2(self, data):
        if data:
            return data
        else:
            return "No data available."


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WuzzufDashboard()
    sys.exit(app.exec_())