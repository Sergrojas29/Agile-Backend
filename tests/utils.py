from dataclasses import dataclass
from init_db import setup_database, teardown_database
from datetime import date


from app.models.user import User
from app.models.project import Project
from app.models.sprint import Sprint
from app.models.task import Task


from app.database import SessionLocal
from app.models.user import User



#Class Methods to create a testable Project Framework
#Allow API Front end testing
#
class FilloutDataBase:
    
    @classmethod
    def createTestDataBase(cls):
        
        with SessionLocal() as session:
            #Create MANY Users
            many_users: list[User] = [ 
                        User(name="Sergio",   is_admin=True,  username="SergioUsername", email="Sergio@gmail.com", password="Something"),
                        User(name="Carolina", is_admin=True,  username="CarolinaUsername", email="Carolina@gmail.com", password="passsssword"),
                        User(name="Mike",     is_admin=False, username="MikeUssername", email="Mike@gmail.com", password="pass11sssword"),
                        User(name="Andrew",   is_admin=False, username="AndrewUsername", email="Andrew@gmail.com", password="pas$$$$sword"),
                        User(name="Eric",     is_admin=True,  username="EricUsername", email="Eric@gmail.com", password="p@aa$$sssword"),
                        User(name="Sarah",    is_admin=False, username="SarahQA", email="sarah@gmail.com", password="password123"),
                        User(name="David",    is_admin=False, username="DavidDesign", email="david@gmail.com", password="password123"),
                    ]
            
            session.add_all(many_users)
            session.flush()
            
            
            #Creat MANY PROJECT
            many_projects: list[Project] = [ 
                        Project(title="Agile Backend API", description="Building the core API", start_at=date(2026, 3, 1),  end_at=date(2026, 3, 28),    owner_id=many_users[0].id),
                        Project(title="React Frontend", description="Building the web client",  start_at=date(2026, 2, 1),  end_at=date(2026, 2, 28),    owner_id=many_users[1].id),
                        Project(title="Mobile App", description="iOS and Android ports",        start_at=date(2026, 1, 1),  end_at=date(2026, 1, 28),    owner_id=many_users[2].id),
                        Project(title="Project Ideas", description="Backlog for 2027",          start_at=date(2027, 1, 1),  end_at=date(2027, 2, 28),   owner_id=many_users[0].id),
                    ]
            
            #ADD to Database
            session.add_all(many_projects)
            session.flush()

            #Creat ONE SPRINT
            many_sprints: list[Sprint] = [ 
                        # Project 0 Sprints
                        Sprint(title="Initialize Project", start_at=date(2026, 3, 1), end_at=date(2026, 3, 15), project_id=many_projects[0].id),
                        Sprint(title="User Stories & DB", start_at=date(2026, 3, 16), end_at=date(2026, 3, 28), project_id=many_projects[0].id),
                        # Project 1 Sprints
                        Sprint(title="UI Mockups", start_at=date(2026, 2, 1), end_at=date(2026, 2, 15), project_id=many_projects[1].id),
                        Sprint(title="React Components", start_at=date(2026, 2, 16), end_at=date(2026, 2, 28), project_id=many_projects[1].id),
                    ]
 
            
            session.add_all(many_sprints)
            session.flush()

            
            #Create MANY TASKS
            many_task: list[Task] = [ 
                        # Sprint 0 Tasks (Agile Backend - Sprint 1) - Dates fixed to match March 1-15
                        Task(title="Create User Stories", description="Write out Jira tickets", start_at=date(2026, 3, 1), due_at=date(2026, 3, 3), value=2, user_id=many_users[0].id, sprint_id=many_sprints[0].id),
                        Task(title="PLANNING POKER", description="Estimate points", start_at=date(2026, 3, 4), due_at=date(2026, 3, 5), value=1, user_id=many_users[1].id, sprint_id=many_sprints[0].id),
                        Task(title="MoSCoW Prioritization", description="Must, Should, Could, Won't", start_at=date(2026, 3, 5), due_at=date(2026, 3, 7), value=3, user_id=many_users[2].id, sprint_id=many_sprints[0].id),
                        Task(title="Environment Setup", description="Install Python & Postgres", start_at=date(2026, 3, 8), due_at=date(2026, 3, 10), value=5, user_id=many_users[3].id, sprint_id=many_sprints[0].id),
                        Task(title="Init DB Script", description="Write SQLAlchemy models", start_at=date(2026, 3, 10), due_at=date(2026, 3, 15), value=8, user_id=many_users[4].id, sprint_id=many_sprints[0].id),
                        Task(title="Refactor Architecture", description="Tech debt", start_at=date(2026, 5, 1), due_at=date(2026, 5, 10), value=13, user_id=many_users[2].id, sprint_id=many_sprints[0].id),
                        
                        # Sprint 1 Tasks (Agile Backend - Sprint 2)
                        Task(title="User POST Route", description="Register users", start_at=date(2026, 3, 16), due_at=date(2026, 3, 20), value=3, user_id=many_users[0].id, sprint_id=many_sprints[1].id),
                        Task(title="Project GET Route", description="Fetch projects", start_at=date(2026, 3, 21), due_at=date(2026, 3, 25), value=2, user_id=many_users[4].id, sprint_id=many_sprints[1].id),
                        Task(title="Write Documentation", description="Needs to be done eventually", start_at=date(2026, 3, 25), due_at=date(2026, 3, 28), value=1, user_id=many_users[2].id, sprint_id=many_sprints[1].id),
                        Task(title="Add Email Notifications", description="Feature request from client", start_at=date(2026, 4, 1), due_at=date(2026, 4, 15), value=8, user_id=many_users[1].id, sprint_id=many_sprints[1].id),
                        
                    ]
 
            
            session.add_all(many_task)
            session.commit()
            
            
            #COMMIT TO DB
            session.commit()
        