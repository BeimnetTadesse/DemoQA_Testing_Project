from locust import HttpUser, task, between, events

class BookstorePerformanceUser(HttpUser):
    """
    Locust Performance Testing script simulating users hitting the Book Store API endpoints.
    Implements realistic pacing (between 1 and 4 seconds wait time) and endpoint prioritization.
    """
    wait_time = between(1, 4)

    @task(3)
    def view_all_books(self):
        """
        Simulates active catalog browsing (3x weight).
        """
        with self.client.get("/BookStore/v1/Books", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to fetch books: Status {response.status_code}")

    @task(2)
    def view_single_book_detail(self):
        """
        Simulates viewing a specific book details page (2x weight).
        Target: Git Pocket Guide (ISBN: 9781449325862).
        """
        isbn = "9781449325862"
        with self.client.get(f"/BookStore/v1/Book?ISBN={isbn}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to fetch book detail for ISBN {isbn}: Status {response.status_code}")

    @task(1)
    def check_user_authorization(self):
        """
        Simulates POSTing to the authorization check endpoint (1x weight).
        """
        payload = {
            "userName": "testuser123",
            "password": "Test@123"
        }
        with self.client.post("/Account/v1/Authorized", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed auth verification check: Status {response.status_code}")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("🚀 Starting DemoQA Bookstore Performance/Load Test...")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("🏁 Performance/Load Test Finished!")
