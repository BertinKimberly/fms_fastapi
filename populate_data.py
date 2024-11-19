import requests
import random
from faker import Faker

BASE_URL = "http://127.0.0.1:8000"
fake = Faker()

# Constants for sample data
SKILLS = ["Python", "JavaScript", "React", "Node.js", "Docker", "Kubernetes"]
FIELDS = ["Transport", "Agriculture", "Trade", "Environmental Protection"]
PROJECTS_COUNT = 10
FREELANCERS_COUNT = 50
CLIENTS_COUNT = 30


def create_freelancer():
    data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "phone": fake.phone_number(),
        "skills": random.choice(SKILLS),
        "hourly_rate": round(random.uniform(20, 100), 2),
    }
    response = requests.post(f"{BASE_URL}/freelancers/", json=data)
    if response.status_code == 200:
        print(f"Created freelancer: {data['email']}")
    else:
        try:
            print(f"Failed to create freelancer: {response.json()}")
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to create freelancer: {response.status_code}, Response Text: {response.text}")


def create_project():
    data = {
        "name": fake.bs(),
        "field": random.choice(FIELDS),
        "description": fake.text(max_nb_chars=200),
        "budget": random.randint(1000, 50000),
    }
    response = requests.post(f"{BASE_URL}/projects/", json=data)
    try:
        response_data = response.json()
    except ValueError:
        response_data = {"error": "Invalid JSON response"}
    if response.status_code == 200:
        print(f"Created project: {data['name']}")
    else:
        print(f"Failed to create project: {response.status_code}, Response Text: {response.text}")
        
def create_client():
    projects = requests.get(f"{BASE_URL}/projects/").json()
    if not projects:
        print("No projects available to associate with clients.")
        return

    project_id = random.choice(projects)["id"]
    print(f"Selected project_id: {project_id}")

    data = {
        "name": fake.company(),
        "email": fake.unique.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "project_id": project_id,
    }
    response = requests.post(f"{BASE_URL}/clients/", json=data)
    if response.status_code == 200:
        print(f"Created client: {data['email']}")
    else:
        print(f"Failed to create client: {response.json()}")


def main():
    print("Seeding data...")

    # Seed freelancers
    # for _ in range(FREELANCERS_COUNT):
    #     create_freelancer()

    # # Seed clients
    # for _ in range(PROJECTS_COUNT):
    #     create_project()

    for _ in range(CLIENTS_COUNT):
        create_client()

    print("Seeding completed!")




if __name__ == "__main__":
    main()

