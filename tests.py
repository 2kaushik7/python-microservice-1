try:
    from Hello import app
    import unittest
except Exception as e:
    print("Some modules are missing {}".format(e))

class Flasktest(unittest.TestCase):
    def test_admin(self):
        tester = app.test_client(self)
        response = tester.get("/admin")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    def test_admin_content(self):
        tester = app.test_client(self)
        response = tester.get("/admin")
        self.assertTrue(b'admin' in response.data)
if __name__ == "__main__":
    unittest.main()